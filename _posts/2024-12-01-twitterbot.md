---
title: "LLM Powered Yu-Gi-Oh! Card Posting Twitter Bot"
date: 2024-12-01
categories:
  - projects
  - experiments
  
tags:
  - why?
  - AI
---

Alternatively titled "DIY self licking icecream cone", "Spend a weekend building the worlds worst Pojos Forum clone", and other very unclever titlings.

It has dawned on me that I am actually entering another manic period, much like in June when I went through a number of projects in a period of weeks, I am doing the same thing again. It is like I have woken up from sleepwalking and am aware how much ground I have lost while trying to not kill myself, so I must produce and conquer projects at a rapid pace just to not move backwards. The list of items in my blog post list is increasing at an insane rate; armed with token generation machines and a fresh perspective I am the most powerful version of myself I could have ever imagined.

Imitation is the sincerest form of flattery or something to that effect I am lifting this project almost verbatim from my hacking homie, who had the idea of a GPT powered shitpost bot months before I did. However he has gone into the void and I dont know if he will return. As such, I have had to forge my own pathway to this project as his blog on it has not gone up.

The twitter API docs are missing a fuckload of info. Perhaps their postman collections were in better shape, I do not know because I chose to not look at them. It probably may have saved me effort, but who knows, theres a chance they suck too. This [github repo](https://github.com/michael-stajer/twitter-oauth2-howto) helps with a lot of the issues I was having. As it says, tweepy does NOT handle the oauth2 flow, and my friendly robot overlord was pushing me to use tweepy at every turn.

So what is the problem we are trying to solve here (regarding oauth)?

Essentially we want one of these to popup, and we want to authenticate it, in order to receive a bunch of tokens we can use to post etc.

Sounds pretty simple on the surface, but I had to jump through a LOT of hoops to get to the end state because the docos seem to want to frustrate you and seem to dislike the idea of you choosing to perform this locally.

Here is the complete script I used to stand up the request and token capture server. There are amendments from the github repo; these are necessary for the way I handle refresh tokens (I dont). I will elaborate later on.

Obvs the port number listed in the script must reflect what is set in the twitter dev portal. It is no matter what you set, it just must match. Now this is the interesting part: the callback URI must be a complete URL. You canNOT just put in the callback URI, it must be the entire http://127.0.0.1:5000 if using my script. For the website URL section however, put literally anythign, as long as its a valid URL. I put mine down as the blog URL lol.

Remember: if you are developing a posting bot, you must give the app permissions to post.

Host the script, navigate to it, click the big ass URL, allow the app to manage the account, and scoop up all your tokens. We will be needing them. 

You will note that the github example only collects the access token/bearer. Which is fine, if all you want to do is use the api for 2 hours. We need to also receive the refresh token, so we can grab new bearers.

YOU WILL ALSO NOTE THAT I HAVE ADDED A SCOPE THAT THE GITHUB WRITEUP DOES NOT. offline.access allows us to request the refresh token in the first instance. If we do not specify, and in turn authenticate with this scope listed, there will be NO granting of refresh tokens. Given this entire bots purpose is to sit on my rpi and shitpost autonomoslouly withOUT user interaction, we need the bearers to be able to be refreshed constantly.

So now we have authenticated, and you have some nice tokens you can use for shit. Your access token lasts 90 days, so you have some time to work out what the app is going to do. 

Given the API documentation does not say theres anything against this, I decided the simplest way to deal with the bearers expiring was to simply request a new one every single time I post. I dont need to worry about the 2 hour expiration, because I dont care if its valid or not; it will be valid as I make the call for the updated bearer!

Now this is a sticky one that you should be aware of (its worth pointing out because I got stuck here) you are exchanging your refresh token for the bearer. Just because you have 90 days to use it, does not mean you can use it for 90 days. Important distinction. 

We make a request to the token endpoint, sending off the current access token, and it returns a new bearer and a new refresh token. A two for one deal. Easy enough, just do this before every post post (huehuehue) and you will stay accessed.

Cool now we can post! But we can only post posts, we cannot upload images, because for some reason that functionality has not been ported over to the v2 api and does not support oauth2 authentication. Fucks sake. 

Fortunately its actually pretty easy, we just generate api keys, access tokens and their secrets in the dev portal. These do NOT need to be autnehticated with a workflow like the v2 api keys, nor do they need rotating. 

Two seperate steps need to occur; the image is uploaded to the server, and then the uploaded media is posted. It makes sense in a way, kind of, if you squint a bit. I have attached to demonstrate.

This is 1/3rd of the toy; yes it posts to twitter, but we need it to select a card out of the Yu-Gi-Oh! card database, and get a tweet from an LLM. I have attached here the scripts I used to pull the card listings from the ygoprodb API. Theres not a lot to it. Next a little function is run that will randomely select one out of the CSV file I have of all pre-5DS cards, make a call to the DB to get full card art and saves it. I probably need to add a function to clean up the saved files before it tips my RPI over.

The irony is in all of this, the actual easiest part was the LLM. I have never heard of them before, and only stumbled upon them because I literally googled free llm api, and found groq. I like it, it looks like grugq. And they provide a fucking LOT for free, half a million daily tokens. I am going to use all of them in an upcoming project, but for now I am happy that this service exists for my shitposting bot.

Heres an example to send and retreive from the site. Its DEAD SIMPLE. You literally feed it your api key, what model you want to use and what your prompt is.

So putting this all together, what do we end up with? Well our efforts reward with a shit poster. The space is intentional. I present the following post from last night that had me in absolute fucking fits of laughter at the absurdity of it.

This is another of those silly ideas that floated into my conciousness while on a flight a while ago, something dredged up out of my past desires I had long forgotten about. Originally I wanted to get an LCD hat for my rpi and have it display the card of the day on the hat (somehow I dont think I am using that word right) but given it lives connected to a USB port behind my television, I most certainly will not be looking at it.

Could this be done via an LLM on the rpi? It could, in theory. But these shit tweets are generated with am 80b param model; anything capable of fitting on an rpi would be an order of magnitude worse.

Here is the final script. Somehow, despite pumping project after project out, my to do list keeps fucking growing. 

