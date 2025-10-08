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

Whilst a negative sounding title, this is actually a reframing of a negative thought pattern i had for most of the year via posting in a roundabout positive manner. this is the post where i finally discuss the automations i have built myself, as well as all manner of failed experiemnts and home made tools i no longer need.

following the evolution of the twitter posting yugioh bot and we can see it went from using groq keys before they banned me (as of 8/10 2025 i am still banned), to a llama model on my nuc, to a gemma model on my nuc, to a gemini model on the cloud, to a qwen model on my raspberry pi. from the cloud back to the ground, back to the cloud and back to the ground again for what i assume will be the final time i configure that tool. 

but why am i bringing this up? it sets the scene (somewhat) for how a few of my tools have lived - running off a cpu only instance of llama and or gemma (depending on what month it was) running on my nuc. it is december 2024, and i am cranking out post after post and internal tool after internal tool in a manic panic to accomplish things i set out to do earlier in the year and didnt get around to because i was trying very hard to not kill myself. it is december 2024.

after being very, very angry at being banned by groq i decided everything needed to be local, and set out to formulate my own tooling to solve issues and replicate products that are censored. i havent tried it again since then so this may be incorrect information now, but at the time the gpt web browser would for instance refuse to have a look at 4chan. i decided it would be a good idea to build out my own scaffolding to scrape web pages in order to have summaries sent to me. this was partially born from two realisations; i spend far too much time online, and, much like my api key debacle, i will probably get banned for wrongthink at some point in time for simply using the tools in a manner deemed unacceptable (ie putting them over links and articles unfit for corporate consumption).

first plain old beauitfulsoup was employed, and it worked ok, some of the time, sometimes. sites that use heavy amounts of javascript, like 4chan, refused to load properly and as such were not able to be scraped. moving to selenium, i was then able to parse the posts in a random /x/ thread and receive summaries of it after chucking the raw parse to an llm. progress!

but then came sites that put content in particular tags. i know that is not helpful but do keep in mind this was almost a full year ago and i dont recall exactly what the issues were and the artifacts i retained were only the final versions, not the WIPs. this necessatated the combination of BOTH selenium and BS, as i couldnt work out how to control the selenium api enough to get the sort of control i am used to working with with BS (thanks to time spent refactoring the black hat python repo from p2 to p3 back in 2020 (you will have to believe that i did it, the repo has been deleted since the 2nd edition of the books come out, making it unnecessary to keep around)) so i had a strange mechanism that would first try a selenium pass, and if that failed to produce any content move to a bs scrape.

i didnt like this, and in the bath researched what alternatives to selenium existed. every now and then i am surprised who releases foss tools of note, and in this instance i am refering to microsoft and playwright. an excellent tool, but necessetated me to throw out all i had put together thus far and begin anew, which ended up being the right move because it fucking works. i say works, in the current tense, because the code i cobbled together between december 24 and the 2nd of jan 25 when i hoisted it onto its permament home, is still intact. the only changes its received are context length expansions when i found gemma 3 4b was just as smart as llama 3.1 8b and lets me hoist 2x as much context for the same ram usage, and a reduction in the amount of articles i get per day. everything else, has been running smoothly and perfectly except when telegram has an outtage.

wait its sending to telegram? yes, because pop authentication to emails is dead and i was not going to fuck around to get 2fa and imap authentication working over a python script. the past 10/11 months have shown that telegram is a perfectly acceptable distribution channel for this anyway! 

i then find out, a week after its finished, ironically through a summary email, probably the grugqs, that someone else has infact released this entire project online and would have saved me the effort. this displeases me somewhat. 

here is a small tally of the artefacts produced. this list will be updated as the story continues towards its laboured and confused conclusion.

-web scraper
-ability to "see" contents of webpages

rumblings begin about this "deep research" business. it sounds pretty fantastic, and the next logical step of the above project; instead of providing the product to distill, have it go and RETREIVE its own product and THEN distill. everything that had been mentioned about it at this point (jan 2025) indicated it was (and it indeed turned out to be true) going to be gatekept behind the $200 USD per month subscription. so a line entry was put onto The Whiteboard (TM) saying i was going to build out a deep research tool of my own. not having used one i was not too sure exactly what it needed, but figured being able to "see" webpages was a great start, and perhaps some sort of OCR capability to read PDFs?

a second function is added to the website; to ingest pdfs, run an ocr tool over them, take each page and summarise, and then reconstitue these summaries into a cohesive whole. i get this working over a few days, grappling with issues with my dev machine and my prod server havig different python versions, yay! eventually this is sorted, and the functionality is live. it works, and it works fucking WELL. initially this is NOT pointing to the nuc cpu llama, as i need it to be free sometimes to process the yugioh shitposts, and instead is pointed at my 3060 dual weilding machine. you may have guessed, based on the previous conclusion and the preamble, upon completing this, i was exposed to another freshly made ready to go solution. the bad vibes continue to pile up.

the tally so far sits at

-web scraper
-ability to "see" contents of webpages
-ability to "see" contents of pdfs

it is february, and i have my nice lime green yeti from my wife and my new ebook reader. i quite like my ebook reader. being eink however, it does have some problems with webpages. not every web page can be properly scraped by my toolset, because i am limited by the context length of the llama 8b model i am hosting; some pages are simply too large. i have a clunky sort of check mechanism in place to validate its under 30k tokens, this works and prevents it fucking out and requiring me to ssh into boxes id rather not touch. so if a site is too big to be summarised, this means its too big for me to read on the computer (i dont like READING on the computer, i SKIM fine, but i want somethign niver to my eyes for long haul reads). so a new addition to the site was generated that will take a website, make a pdf of it and then crunch that through to an epub. it works well but i was really kidding myself cause most of the epubs i have generated i still havent read. cest la vie.

thus far we have 

-web scraper
-ability to "see" contents of webpages
-ability to "see" contents of pdfs
-ability to take sites too big to parse summaries from and crunch to pdf -> epub

i talk a lot about using ai to aid in testing. and i do, in indirect ways. i have no interest in feeding entire dumps of traffic to the tool; as an experiment i tried this and it fucking CHOKED, was a very pointless afternoon. it is march, and i decided to take burpference (https://github.com/dreadnode/burpference) to the nth degree and cobbled my own config together to get it to point to my lmstudio api. escaping all the shit that appears in raw traffic logs was a nightmare. it languished on the "to do list" for a while, because i could feel that with some more work, it was actually going to be an insanely useful tool. surgical, targeted precision instead of asking the poor little palantir to eat the firehose

*homer donut gif*

imagine my disappointment (yes i AM that conceited, how did you know?) when a few weeks later burp ai drops. and it does what i was lookign to do, but within the ui itself instead of via a second rate plugin modified by a third rate hack (me). once again i am beaten to the punch, but this time i choose to not see my experiments through to their conclusion and throw them out.

we have obtained at this point

-a web scraper
-a tool with the ability to "see" contents of webpages
-a tool with the ability to "see" contents of pdfs.
-ability to take sites too big to parse summaries from and crunch to pdf -> epub
-a real hard lesson in the differences in compute between my 3060 and real inference g/tpus

it is may, and i get around to testing the gemma models. these have vision capabilities, but lmstudio does not. i want to be able to feed the model an image and have it describe it and or read whats on it if needed. this feels like another step towards the diy at home deep research capes i am still planning on building out. its felt like a "missing piece" for quite a while now; gpt has had it for ages, why not the at home models? so a new api is written up, that will ingest an uploaded image and retreive a description from gemma. it would be nice for it to keep it in context however, not just discard it. this is a piece i am struggling with, and put it down for a while.

we have obtained at this point

-a web scraper
-a tool with the ability to "see" contents of webpages
-a tool with the ability to "see" contents of pdfs
-ability to take sites too big to parse summaries from and crunch to pdf -> epub
-a real hard lesson in the differences in compute between my 3060 and real inference g/tpus
-a half baked api to truely look at images

it is now june. we have a list of compostable pieces; with enough string and glue, surely we can take all of these seperate pieces and produce a functional deep research agent. it is june, and it has been released to the plus subscribers, of which i am. this is not demoralising; it is infact more impetus to get this project working, as i am blown the absolute fuck away by how good the product is and burn through my queries often. nothing, and i mean fucking NOTHING i have used up to this point, has ever been able to properly address my test question about the yugioh ocg format in the late 90s. its esoteric as all fuck and its intentionally designed to trip the bots up. 

surely, this is enough to string together some sort of research model, right? it can get webpages, read them, get summaries, do the same with pdfs, format sites too big to parse normally, and look at images? this has got to be all thats required to get somethign semi useful up and running (and look i dont disagree - cobbling them together WOULD produce some results of note for sure). but i am exposed to the project local deep research and wouldnt you believe it it actually fucking works. so once again, i am thoroughly beaten to the punch, and become reasonably disappointed again that my work would be pointless upon this task. (see this post for steps to set it up - turns out i would spend about as much time as i figured it would take to BUILD something out trying to TROUBLESHOOT this solution)

-a web scraper
-a tool with the ability to "see" contents of webpages
-a tool with the ability to "see" contents of pdfs
-ability to take sites too big to parse summaries from and crunch to pdf -> epub
-a real hard lesson in the differences in compute between my 3060 and real inference g/tpus
-a half baked api to truely look at images
-a functional deep research tool for when i have burnt my OAI queries

it is september, and i am looking once again at RAG solutions. LM studio has an update, and it adds rag functionality...as well as this little icon. *lm image upload*

two guesses what this does; why yes it allows injection of images into the current chat! unlike my api, it will not call a new chat with each image uploaded. it is september, and i for once, feel relief. "thank fuck" i say, "thank fuck i no longer need to build out that functionality". its here and its been made for me by the hardworking devs who stay on the bleeding edge to provide to me, those ONLY on the cutting edge. "you were beaten to the punch FIVE SEPERATE TIMES, how are you on the cutting edge? have you no shame?" no, i dont have any and yes the fact i am even in this sandpit means i am on the cutting edge. do you know how hard it was not to be condesending when i heard the principal of another team talk about fine tuning a domain related model for his use? thinking he was going to use our internal compute for it? do you not understand i worked out 18 months ago we lack the hardware for this?

i have referenced multiple times the concept of agents being bash loops. this is not a joke to me, this is literally how my site and helpers run, off a bash loop and a cron job. expanding any further here will be trodding already trodden ground, read about it here **

back to the main point here; unless you are actively invested in pushing the boundaries and being a fronteirer in your respective domain, there is little ADVANTAGE to being on the bleeding edge. the truth of all my little experiments, despite their seemingly disapointing conclusions (because for some reason i attributed being a super special unique flower with providing me satisfaction) the undeniable reality of it is i built them because it was fun. the fact they served a purpose is incidental and tangental; these pieces are only getting mentioned because they are the ones actively in use today - other pieces suchg as the novel drafting toolkit and the barebones of a pokemon playing agent and a series of jwt tools in a workflow were built out but sit in a folder called 'zzz_requires sorting' where they will probably be deleted once its been a year since i last touched them.

its fun to build things. its exhausting racing to be first all the time. it is also impossible to be across every piece of new research from every lab. id rather spend time in my own lab tinkering with stupid shit and being delighted and building for the fuck of it. because ultimately, in what has to be the most cruel joke to those chasing the bleeding edge, time will erode that edge. if i ignore what is happening in The Field (an interchangble placeholder for ml/infosec/whatever it is that has my attention this month) for any period of time, whatever is at the forefront when i return will have overrode whatever i missed while i was away, almost as if it never happened, making it extremley futile to even attempt to continually chase the every shifting fronteir. 


this has been a somewhat cleansing musing and in some ways feels spiritually like the end of  year summaries i write into my sigil book every year. things didnt really go to plan most of the time, but only because i have the freedom to potter and fuck around with little doodads and build oddities was i able to even miss the mark. 
