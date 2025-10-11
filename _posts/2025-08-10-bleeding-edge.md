---
title: "Time Dulls the Bleeding Edge"
date: 2025-10-08
categories:
  - learning
  - experiments
  - projects
  
tags:
  - rants
  - AI
---

Whilst at first glance it might read like a depressing sounding title, this is actually a reframing of a negative thought pattern i had for most of the year via posting in a roundabout positive manner. This is the post where I finally discuss the automations I have built myself, as well as all manner of failed experiemnts and home made tools I no longer need.

Following the evolution of the [twitter posting yugioh bot](https://onecloudemoji.github.io/projects/experiments/twitterbot/) and we can see it went from using groq keys before they banned me (as of 8/10 2025 I am still banned), to a llama model on my nuc, to a gemma model on my nuc, to a gemini model on the cloud, to [a qwen model on my raspberry pi](https://onecloudemoji.github.io/learning/projects/rpi-llm/). From the cloud back to the ground, back to the cloud and back to the ground again for what I assume will be the final time I configure that tool. 

This sets the scene (somewhat) for how a few of my tools have lived - running off a cpu only instance of llama and or gemma (depending on what month it was) on my nuc. It is december 2024, and I am cranking out post after post and internal tool after internal tool in a manic panic to accomplish things I set out to do earlier in the year and didnt get around to because I was trying very hard to not kill myself. It is december 2024.

![xmas](/assets/images/edge/xmas.jpg)

After being very, very angry at being banned by groq I decided everything needed to be local, and set out to formulate my own tooling to solve issues and replicate products that are censored. I havent tried it again since then so this may be incorrect information now, but at the time the gpt web browser would for instance refuse to have a look at 4chan. I decided it would be a good idea to build out my own scaffolding to scrape web pages in order to have summaries sent to me. This was partially born from two realisations; I spend far too much time online, and, much like my api key debacle, I will probably get banned for wrongthink at some point in time for simply using the tools in a manner deemed unacceptable (ie putting them over links and articles unfit for corporate consumption).

First plain old beauitfulsoup was employed, and it worked ok, some of the time, sometimes. Sites that use heavy amounts of javascript, like 4chan, refused to load properly and as such were not able to be scraped. Moving to selenium, I was then able to parse the posts in a random /x/ thread and receive summaries of it after chucking the raw parse to an llm. Progress!

![progress](/assets/images/edge/progress.jpg)

But then came sites that put content in particular tags. I will not be elaborating upon this because it was almost a full year ago and I dont recall exactly what the issues were and the artifacts I retained were only the final versions, not the progressions I am describing. This necessatated the combination of BOTH selenium and beauitfulsoup, as I couldnt work out how to control the selenium api enough to get the sort of control I am used to working with with beauitfulsoup (thanks to time spent refactoring the black hat python repo from p2 to p3 back in 2020 (you will have to believe that I did it, the repo has been deleted since the 2nd edition of the books come out, making it unnecessary to keep around (I do need to further my no starch press book additcion and get the 2nd ed))) so I had a strange mechanism that would first try a selenium pass, and if that failed to produce any content move to a bs scrape.

I didnt like what bs (hue) this had turned into, and in the bath researched what alternatives to selenium existed. Every now and then I am surprised who releases foss tools of note, and in this instance I am refering to microsoft and playwright. an excellent tool, but necessetated me to throw out all I had put together thus far and begin anew, which ended up being the right move because it fucking works. I say works, in the current, present tense, because the code I and various gpts (including local ones!) cobbled together between december 24 and the 2nd of jan 25 when I hoisted it onto its permament home, is still intact. The only changes its received are context length expansions when I found gemma 3 4b was just as smart as llama 3.1 8b and lets me have 2x as much context for the same ram usage, and a reduction in the amount of articles I get per day. Everything else, has been running smoothly and perfectly except when telegram has an outtage.

Wait its sending to telegram? Yes, because basic authentication to emails is dead and I was not going to fuck around to get 2fa and or oauth via imap working over a python script. The past 10/11 months have shown that telegram is a perfectly acceptable distribution channel for this anyway! 

I then find out, a week after its finished, ironically through a summary email, probably the grugqs, that someone else had infact released this entire project online and would have saved me the effort. This displeases me somewhat. 

Here is a small tally of the artefacts produced. This list will be updated as the story continues towards its laboured and confused conclusion.

•web scraper
•ability to "see" contents of webpages

It is january 2025. Rumblings begin about this "deep research" business. It sounds pretty fantastic, and the next logical step of the above project; instead of providing the product to distill, have it go and RETREIVE its own product and THEN distill. Everything that had been mentioned about it at this point indicated it was (and it indeed turned out to be true) going to be gatekept behind the $200 USD per month subscription. So a line entry was put onto The Whiteboard (TM) saying i was going to build out a deep research tool of my own. Not having used one i was not too sure exactly what it needed, but figured being able to "see" webpages was a great start, and perhaps some sort of OCR capability to read PDFs?

A second function is added to the website; to ingest pdfs, run an ocr tool over them, take each page and summarise, and then reconstitue these summaries into a cohesive whole. I get this working over a few days, grappling with issues with my dev machine and my prod server having different python versions, yay! Eventually this is sorted, and the functionality is live. It works, and it works fucking WELL. Initially this is NOT pointing to the nuc cpu llama, as I need it to be free sometimes to process the yugioh shitposts, and instead is pointed at my 3060 dual weilding machine. You may have guessed, based on the previous conclusion and the preamble, upon completing this, I was exposed to another freshly made ready to go solution. The bad vibes continue to pile up.

the tally so far sits at

-web scraper
-ability to "see" contents of webpages
-ability to "see" contents of pdfs

It is february, and I have my nice lime green yeti from my wife and my new ebook reader. I quite like my ebook reader. Being eink however, it does have some problems with webpages. Not every web page can be properly scraped by my toolset, because I am limited by the context length of the llama 8b model I am hosting; some pages are simply too large. I have a clunky sort of check mechanism in place to validate its under 30k tokens, this works and prevents it fucking out and requiring me to ssh into boxes id rather not touch. So if a site is too big to be summarised, this means its too big for me to read on the computer (I dont like READING on the computer, I SKIM fine, but I want somethign nicer to my eyes for long haul reads (which is ironic because editing this inside darkmode github is doing bad things to my sight)). So a new addition to the site was generated that will take a website, make a pdf of it and then crunch that through to an epub. It works well but I was really kidding myself cause most of the epubs I have generated I still havent read. cest la vie.

thus far we have 

-web scraper
-ability to "see" contents of webpages
-ability to "see" contents of pdfs
-ability to take sites too big to parse summaries from and crunch to pdf -> epub

It is march and I am talking a lot about using ai to aid in testing. And I do, in indirect ways. I have no interest in feeding entire dumps of traffic to the tool; as an experiment I tried this and it fucking CHOKED, was a very pointless afternoon. it is march, and i decided to take [burpference](https://github.com/dreadnode/burpference) to the nth degree and cobbled my own config together to get it to point to my lmstudio api. Escaping all the shit that appears in raw traffic logs was a nightmare. It languished on the ever present to do list for a while, because I could feel that with some more work, it was actually going to be an insanely useful tool. Surgical, targeted precision instead of asking the poor little palantir to eat the firehose

*homer donut gif*

Imagine my disappointment (yes I AM that conceited, how did you know?) when a few weeks later burp ai drops. And it does what i was lookign to do, but within the ui itself instead of via a second rate plugin modified by a third rate hack (me). Once again I am beaten to the punch, but this time I choose to not see my experiments through to their conclusion and throw them out.

we have obtained at this point

-a web scraper
-a tool with the ability to "see" contents of webpages
-a tool with the ability to "see" contents of pdfs.
-ability to take sites too big to parse summaries from and crunch to pdf -> epub
-a real hard lesson in the differences in compute between my 3060 and real inference g/tpus

It is may, and I get around to testing the gemma models. These have vision capabilities, but lmstudio does not. I want to be able to feed the model an image and have it describe it and or read whats on it if needed. This feels like another step towards the diy at home deep research capes I am still planning on building out. Its felt like a "missing piece" for quite a while now; gpt has had the ability to see images for ages, why not the at home models? So a new api is written up, that will ingest an uploaded image and retreive a description from gemma. It would be nice for it to keep it in context however, not just discard it. This is a piece i am struggling with, and put the project down for a while.

we have obtained at this point

-a web scraper
-a tool with the ability to "see" contents of webpages
-a tool with the ability to "see" contents of pdfs
-ability to take sites too big to parse summaries from and crunch to pdf -> epub
-a real hard lesson in the differences in compute between my 3060 and real inference g/tpus
-a half baked api to truely look at images

It is now june. we have a list of compostable pieces; with enough string and glue, surely we can take all of these seperate pieces and produce a functional deep research agent. It is june, and chatgpts deep research has been released to the plus subscribers, one of which is me. This is not demoralising; it is infact more impetus to get this project working, as I am blown the absolute fuck away by how good the product is and burn through my queries often. Nothing, and i mean fucking NOTHING i have used up to this point (STORM is the only name I can recall from my testing periods) has ever been able to properly address my test question about the yugioh ocg format in the late 90s. its esoteric as all fuck and its intentionally designed to trip the bots up. This is due to the inclusion of three letters - OCG. I will perhaps elaborate in another post another day.

Surely, I have enough pieces to string together some sort of research model, right? It can get webpages, read them, get summaries, do the same with pdfs, format sites too big to parse normally, and look at images? This has got to be all thats required to get somethign semi useful up and running (and look future me genuinely agrees - cobbling them together WOULD produce some results of note for sure). But I am exposed to the project [local deep research](github.com/LearningCircuit/local-deep-research) and wouldnt you believe it it actually fucking works. So once again, I am thoroughly beaten to the punch, and become reasonably disappointed again that my work would be pointless upon this task. (see this post for steps to set it up - turns out i would spend about as much time as i figured it would take to BUILD something out trying to TROUBLESHOOT this solution)

-a web scraper
-a tool with the ability to "see" contents of webpages
-a tool with the ability to "see" contents of pdfs
-ability to take sites too big to parse summaries from and crunch to pdf -> epub
-a real hard lesson in the differences in compute between my 3060 and real inference g/tpus
-a half baked api to truely look at images
-a functional deep research tool for when i have burnt my OAI queries

It is september, and I am looking once again at RAG solutions. LM studio has an update, and it adds rag functionality...as well as this little icon. *lm image upload*

Two guesses what this does; why yes it allows injection of images into the current chat! Unlike my api, it will not call a new chat with each image uploaded. It is september, and I for once, feel relief. "Thank fuck" I say, "thank fuck I no longer need to build out that functionality". Its here and its been made for me by the hardworking devs who stay on the bleeding edge to provide to me, those """only""" on the cutting edge. "You were beaten to the punch FIVE SEPERATE TIMES, how are you on the cutting edge? have you no shame?" No, I dont have any and yes the fact I am even in this sandpit means I am on the cutting edge. Do you know how hard it was not to be condesending when I heard the principal of another team talk about fine tuning a domain related model for his teams use? Thinking he was going to use our internal hash cracking rig for it? Do you not understand I went down this route 18 months ago and worked out we lack the hardware for this?

I have referenced multiple times the concept of agents being bash loops. This is not a joke to me, this is literally how my site and helpers run, off a bash loop and a cron job. Expanding any further here will be trodding already trodden ground, read about me lording over people with my big brain and my big penis [here](https://onecloudemoji.github.io/learning/agents/)

Back to the main point here; unless you are actively invested in pushing the boundaries and being a frontier in your respective domain, there is little ADVANTAGE to being on the bleeding edge. The truth of all my little experiments, despite their seemingly disapointing conclusions (because for some reason I attributed being a super special unique flower with providing me satisfaction) the undeniable reality of it is I built them because it was fun. The fact they served a purpose is incidental and tangental; these pieces are only getting mentioned because they are the ones actively in use today - other pieces suchg as the novel drafting toolkit and the barebones of a pokemon playing agent and a series of jwt tools in a workflow were built out; all of these sit in a folder called 'zzz_requires sorting' where they will probably be deleted once it has been over 12 months since I last touched them.

Its fun to build things. Its exhausting racing to be first all the time. It is also impossible to be across every piece of new research from every lab. Id rather spend time in my own lab tinkering with stupid shit and being delighted and building for the fuck of it. Because ultimately, in what has to be the most cruel joke to those chasing the bleeding edge, time will erode that edge. If I ignore what is happening in The Field (an interchangble placeholder for ml/infosec/whatever it is that has my attention this month) for any period of time, whatever is at the forefront when i return will have overrode whatever was the SOTA that I missed while I was away, almost as if it never happened. 


This has been a somewhat cleansing musing and in some ways feels spiritually like the end of  year summaries I write into my sigil book every year. Things didnt really go to plan most of the time, but only because I have the freedom to potter and fuck around with little doodads and build oddities was I able to even miss the mark. There is a quote I saw I very much like; "you waste years not being able to waste hours". I will not elaborate any further, but end this with a koan - if I wasnt actively building out the toolsets I was supplanted by, would I have ever known about their existence?

I forged a key and found the door already open. Had I not forged, would the hinge have shown itself?





