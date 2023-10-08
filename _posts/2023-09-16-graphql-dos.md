---
title: "GraphQL Denial of Service with DVGA"
date: 2023-09-16
categories:
  - pentesting
  
tags:
  - pentesting
---

In an act of sheer irony, after passing my OSWE, I have been on all manner of odd, bespoke testing but not as much web work as I was doing before taking the course. And its occured to me in this absense from that realm that I actually **really** like web work. I needed another project for the blog to skew the content ratio back towards infosec, and figured some of the rather interesting ways we can cause service degredation and denial of service using GraphQL would be good.

Like most things I write in here, this isnt for you, it is for me.
![respect](/assets/images/graphql/respect.jpg)

For these exercises we will use [Damn Vulnerable GraphQL project](https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application). I 100000% recommend using the docker instance, otherwise youre really going to be DOSing yourself.

````docker container run --rm -p 5013:5013 -e WEB_HOST=0.0.0.0 dvga````

This post will not go into what GraphQL is, will only reference introspection in the context of abusing it for a DOS, and will not cover most other important but general GraphQL information. For that, I genuinely and unironically suggest the Blackhat GraphQL No Starch Press book. It covers pretty much everything you need, including filling in a few gaps the Portswigger GraphQL academy doesnt. 

As consistent readers may have gathered, I have a massive hardon for No Starch; their books formed the basis of mine and my [hacking homies](https://kymb0.github.io/) careers and continue to aid me along to this day. Please send me 1x copy of your deep learning book if you are reading this No Starch.

DOS on APIs? Cant we just put rate limiting in place and be done with this?

Short answer, no. Long answer, also no. Each of these attacks can be performed in a single query. We are not doing yeolde 'blast the shit out of the endpoint to take it offline' type attacks; we are using/abusing functionality baked into the GraphQL spec.

I want to hammer this one home; we are (for the most part) not relying on the API dev making a misconfiguration, these are all functionalites built into GraphQL by the FB devs. The end client we are testing has practically 0 tangiable control over locking these down.

Lets start off with a good one, that made me sit the fuck up and pay attention. Id never seen anything quite like it before, and is a great showcase why we use the docker container.

Fragments! Essentially these prevent you from having to individually type out the same subset of field names over and over in extended length queries.

They are defined like so
````
fragment NAMEYOUMADEUP on Object_type_name_that_exists {
	field1
	field2
}
````
This is a real example we can use in DVGA
````
fragment CommonFields on PasteObject {
	title
	content
}
````

Lets showcase this in use on a query to retreive pastes

````
query {
    pastes{
      ...CommonFields
    }

}

fragment CommonFields on PasteObject {
  title
  content
  id
}
````
![fragment1](/assets/images/graphql/fragment1.png)

it MUST be noted the ... prior to the fragment name IS NOT FILLER!! it will not run without it! its called a spread operator, a pretty stupid name if you ask me.

![fragment2](/assets/images/graphql/fragment2.png)

By now I imagine your spidey sense is going apeshit and you have an inkling what is coming next. If we create circular fragments, then call them, we are essentially creating infinite loops with 0 chance to resolve. Much like using teamviewer to hit a machine with teamviewer open.

This query, or one like it, will cause DVGA to shit the bed entirely.
````
query {
    pastes{
      ...CommonFields
      ...TestFields
    }

}

fragment CommonFields on PasteObject {
  ...TestFields
}

fragment TestFields on PasteObject {
  ...CommonFields
}
````
![fragment3](/assets/images/graphql/fragment3.png)

Arent you glad we ran it in docker? The entire instance has been taken offline because of this circular query!

This, is spec complient. This does not techincally break any rules of the way GraphQL was designed, and the API dev has not done anything wrong with his implementation for this to occur. It requires third party frameworks to be installed to mitigate, because according to GraphQL, it is simply working by design in this instance.

What if you find a recursive object relationship in graphql voyager, like so? 

![recurse1](/assets/images/graphql/recurse1.png)

What we need to do when we come across things like this is ASSUME ITS VULNERABLE UNTIL YOUVE TESTED IT. The fact there even IS a recursive relationship is a good indication something might be kinda off in here.

It should be noted! This is NOT a fault with the GraphQL spec unlike circular fragments. This is for all intents and purposes a business logic flaw; the API devs introduce these type of flaws, not the GraphQL devs.

if we make a circular request like so 

````
query{
  pastes{
    owner{name}
  }
}
````
this takes 40ms to respond. 

but what if we keep stacking it up like so?

![recurse2](/assets/images/graphql/recurse2.png)


this takes 1211ms

What if we go even further beyond? By doubling the number of queries we made it take so long that I literally cancelled the request because I was sick of waiting for a response to measure it; it was over 5 minutes when I qq. That is legit service degredation. Interesting to note here is that this does NOT crash the container, whilst the circular fragment DID.

Is this even realistic? well these examples are small time baby shit with 40 recursive queries. A hackerone payout for a DOS using this exact same technique had over FIFTEEN THOUSAND stacked queries! ***get report***


field duplication is SIMILAR to circular queries, except instead of performing this on bi directional fields, we just chuck the same field in a bunch of times.

Here is a nice normal request.
![dup1](/assets/images/graphql/dup1.png)

And here is me stacking up the content a thousand times. This returns in 900ms instead of 64.
![dup2](/assets/images/graphql/dup2.png)


And if I do it 5k times, it takes 13510ms. 
![dup3](/assets/images/graphql/dup3.png)

we can really begin to be stupid. This is most DEF something to keep in mind when doing testing, if the client has agreed to DOS testing in the ROE. Unless the client has implemented query cost analysis, you should expect to see this in ***ALL*** graphql implementations. Remember, we are simply loading up a SINGLE request. Traditional rate limiting canNOT touch this. 

Is THIS real world? Surely not? In 2019 [gitlab was found to infact BE vulnerable to this](https://gitlab.com/gitlab-org/gitlab/-/issues/30096). Very real world indeed.


Introspection is also vulnerable to circular issues, right out the gate anywhere its enabled. inside the __schema, we can request the types. this takes fields as an input, which can be given type as an input, which can be given fields as an input, which can be given type as an input and so on and so forth. here is a small poc. just keep repeating these loops until it shits the bed.



````query{
  __schema{
    types{
      fields{
        type{
      fields{
        type{
        fields{
          name
        }
        }
      }
        }
      }
    }
  }
}
````
Here is a nice innococous query, nothing bad happening here!
![intro1](/assets/images/graphql/intro1.png)

Here we start to stack it up and see it getting a bit wobbly; the response takes over 3x as long to do 2x the work.
![intro2](/assets/images/graphql/intro2.png)

And here we send a shitload to it at once. Nearly 3seconds, we have again proven service degredation.
![intro3](/assets/images/graphql/intro3.png)

Once again, this is spec complient! We are doing nothing here except using introspection in the way it was made! This is why when you find a client with introspection enabled, you have automatically found a bunch of findings. All clients should be disabling introspection, and if they do not, this will happen.


What about some of the more..bizare features of GraphQL? How about stacking directives?

As it turns out, there is no limit to the number of directives you can stack onto a field. Zero! AND! The server MUST process all directives given to it, in order to determine what is a real directive. Meaning we can literally feed the robot garbage until its sick and it cannot do anything about it.

Here is I believe 100 fake directives being attached to this query, making it take nearly 5 seconds.

![directive1](/assets/images/graphql/directive1.png)


I decided to put 40,000 fake ones onto a field, and made the query take almost a minute. Whilst the response was a 400, the fact we actually adjusted the response time by a measurable amount says this is most certainly a viable dos.

![directive2](/assets/images/graphql/directive2.png)


batchql can help us find batching issues. you cant issue these from altair, youll need to form up some curl to test them. This is because we are sending multiple queries inside our onw query, something that altair does not accept, because it only lets you send queries inside your queries, not queries inside your queries. Ensure you keep up. 

Lets send a curl to retreuve the system health.

````curl http://localhost:5013/graphql -H "Content-Type: application/json" -d '[{"query":"query {systemHealth}"},{"query":"query {systemHealth}"}]'````

![batch1](/assets/images/graphql/batch1.png)

lets add that in 30 times.

![batch2](/assets/images/graphql/batch2.png)

Tada, once again we have proven we can degrade the server with a single request.

time for your example, this was used to abuse a wordpress graphql implementation, also in april 21. sending through 10k duplicate fields in 100 chained queries was found to be enough to take most offline. ***find cve***


This is the last example, and it is a little funny. Before we get into it is important to know that the systemUpdate function on DVGA is designed to run for a random amount of time. So you may find your response times dont quite line up with mine, like at all. But if you do the experiments youll find that this vector DOES work.

Rather than batching queries, we can stack queries using aliases. 

Remember, when run individually update will take a random amount of time (but never an EXCESSIE amount of time. 

30 sec for it on its own, 
![stack1](/assets/images/graphql/stack1.png)

50 for a stacked query. surely this 20 sec variance means it worked? NO. keep running the stacked query and youll see that it infact is not multiplying the response time.
![stack2](/assets/images/graphql/stack2.png)

If we stack them with aliases however, we see it takes just shy of 4 minutes for a response. This is NOT in line with the random return intervals you receive for a single query.
![stack3](/assets/images/graphql/stack3.png)

Well what about this attack mr smarty pants? Surely THIS does not have a real world example? yep, it sure does! april 2021 magento (an ecommerce platform that funnily enough my oscp exam in 2019 had built a replica of) was hit by a combination of these techniques in a single attack; aliases were used to send the same query thousands of times, with each query requesting thousands of the same field.

This has by far been one of the most interesting and fulfilling side projects I have done in a while. It genuinely got my excited that theres still fun work to be had out there. Pentesting is pretty fucking dry sometimes, and it starts to wear on your soul when youre seeing the same applications from the same devs written on the same frameworks year after year. These discoveries, combined with IOT research, keep the field from feeling stale. 

![wolfcastle](/assets/images/fable/mcbain.jpg)
