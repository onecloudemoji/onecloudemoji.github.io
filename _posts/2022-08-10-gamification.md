---
title: "Gamification has ruined basically everything"
date: 2022-08-10
categories:
  - learning
  
tags:
  - study
  - rants
---

Games are games and learning is learning. I found out in the second fucking grade that never shall the two meet, because the quality of both declines.

The cyber “industry” (and I use both terms loosely for reasons I wont get into) has really, and I mean REALLY latched onto this gamification concept. Everyone and every platform is competing for higher scores, higher ranks and first bloods in their Fisher Price brightly coloured Play-Doh looking ass platforms. 

![factory](/assets/images/gamification/playdo.png)

These are concepts straight from my days playing quake and CSS competitively; these are for GAMES. Because what’s missing from this race to the top of the ladder, is the learning. Because the reality is it was never about that. You are a product to be bought and sold, your habits too.

The goal is becoming faster at playing the "game" of cyber. No one is in a rush to read more or grind out more knowledge. Ironically, in the quest to "gitgud" as quickly as possible, no one is actually "getting good". If your foundation is built on zapping through CTFs as fast as you can, getting those dopamine receptors revved up to add another point to your online platform ranking, can you honestly expect to be receiving an education?

![education](/assets/images/gamification/education.png)

Its addictive to get those points. I know, because whilst in two separate very expensive training grounds, I tried to get points above the learning. I got addicted to the concept of capturing the flags more than learning. I thought I was king of all shit for popping everything in the PWK labs with eternal blue and just hoovering up roots like a naughty vacuum.

![vacuum](/assets/images/gamification/vacuum.png)

My [hacking homie](https://kymb0.github.io/) recognised that I was in a messed up mind state a while ago, and wanted to help bring me back out of the void. One of the many things he did was he decided we should both sign up for [Offshore](https://app.hackthebox.com/prolabs/overview/offshore), one of the HTB pro labs, and spend some time together bonding over this. 

![friends](/assets/images/gamification/friends.png)

And much like in the OSCP labs, I could feel myself doing the Zerg rush to get flags again. One prime example is the end game state of the first domain; you are using powerview to abuse some AD rights that bloodhound has shown you. And I vividly remember just half skimming the overview that bloodhound gives you on how to abuse that particular DACL, to get the flag as quickly as possible. 

In the end I did finish the lab, but it was a hollow win. I didn’t learn as much as I expected, because I wasn’t there to learn. I was there to play games. Is this a personal fault? No, the platform literally has the word "gamified" on the front page! It was MADE to be this way. I had spent literal months playing a game, when I could have been studying.

![offshore](/assets/images/vagrant/offshore.png) 
Here is my award for playing the game.

What has been exceptionally helpful however, has been using my [automated AD lab with vagrant](https://onecloudemoji.github.io/labbing/vagrant-ad-lab/)  (and before I got the automated AD lab one set up the [Kerberoast lab](https://onecloudemoji.github.io/labbing/pivoting-and-kerberoast-lab-setup/)) to perform all sorts of zany attacks. Did you honestly expect this to not turn into a fart huffing exercise? 

And do you know why my AD lab works as a great LEARNING platform? Because it’s boring. There’s no flags. There’s no game to play. There’s no point system. There is nothing bright and shiny you can put in your linked in headline. There’s nothing to do, EXCEPT LEARN! 

![library](/assets/images/gamification/library.png)

Everyone wants to play CTFs, but no one wants to hack. As Joe organ says, it’s just high tech procrastination. The achievements and point progression make it SEEM like you’re getting somewhere (“but number go up I must be on the right path!”) but the reality is you are just wanking into the bed sheets.

There is exceptionally little real world crossover between these gamified concepts and the actuality. The IT sphere has never, ever, fucking EVER had a shell be popped by someone uncovering the backdoor that was put there to be a quirky, fun, puzzle. Misconfigurations are not fun, and performing source code analysis to uncover them is always awful. These skills, are the byproduct of dry, rote textbook learning. 

![ctf](/assets/images/gamification/ctfs.jpg)

You cannot learn how an environment works while playing a game, because you will always, ALWAYS, be playing a game when in that environment. Without the feeling of sheer panic as you push a misconfiguration to production, and having to write a root cause analysis on the fuckup which FORCES you to understand what happened, how it happened, WHY it happened, and perhaps most critical, how to prevent it from happening again ("dont do it" is not an acceptable response to how do we prevent this from occuring again), you cannot truely grasp what it is you are doing in your game. 

You cannot gamify the fuckery a misconfigured SYSVOL can cause, because who the fuck is going to provide that scenario, one that runs risk of nuking their entire platform? But you miss out, because the game says it will not be played this way. These are things you can only get from three places; textbooks, building labs, and doing WORK.

![work](/assets/images/gamification/work.png)

If you need bing-bing-wahoo to get interested in a topic, guess what; the problem isn’t the topic. If you wouldn’t on your own dime and time buy a textbook on said topic to read and digest because "that sounds boring", then you’re going through these platforms to play games, not to learn. The Library of Alexandria is readily available for every single human being to digest literally any topic on earth (and beyond). You live in the future people like Leonardo di ser Piero da Vinci could only DREAM of, and you think learning is boring? If this is the mind state you have, you do not deserve the world you live in.

![read](/assets/images/gamification/read.png)

I know of multiple people who unironically were devastated when something came up in their lives and they couldn’t log into a platform one day, and lost their XYZ length streak. What the fuck is going on when an educational platform is putting Snapchat style dark patterns in to coerce and guilt you into using it more? It’s quite clear the intention is NOT “to get the users excited to study more” and everyone whose parroting this is lying to themselves.

![truth](/assets/images/gamification/lie.jpg)

You want some practical, tangible and actionable advice on what you should do instead? Build a small domain, fill your AD with [badblood misconfigurations](https://github.com/davidprowe/BadBlood), download vulnerable software from exploitdb (filter by "has app" on the main page), set up the [OWASP Broken Web Apps](https://sourceforge.net/projects/owaspbwa/) and go to town. When you break your domain, fix it. Try to write some tools to automate things. Spend time configuring a C2 (there are plenty of free options that work you can use, [SILENTTRINITY](https://github.com/byt3bl33d3r/SILENTTRINITY) is one. Empire WAS popular but I stopped paying attention to it when it went read only, I dont know what its status is). You can even do this locally before you complain about AWS and Azure. Run through the [burp academy](https://portswigger.net/web-security). Congratulations, you are now semi useful to an org, in a way playing online flash games all day does not prepare you for.

![congrats](/assets/images/gamification/congrats.png)

Learning is not fun. Anyone who says otherwise is lying and has not actually done any real learning in a long time. Having your brain stretched and reaching new depths of hell trying to gain a new wrinkle or synapse connection is not pleasant. Learning is the same as practicing an instrument; if you are just mindlessly noodling the same shapes and scales you always do, you haven’t practiced shit. You have done nothing. 

![advice](/assets/images/gamification/play.jpg)
 
 That little piece of advice took my guitar playing to another fucking level. I was able to work through Marty Friedmans [melodic control](https://www.youtube.com/watch?v=-OmDoa2SkKY). That was a pivotal moment in my life, as he is one of my last remaining heroes and I had objectively become the best guitarist I knew due to his lessons. It was also one of the single most frustrating experiences I have ever had the misfortune of putting myself through. And in those three gruelling months, my skillset went through the fucking roof; something that did not happen during the many years of fun "practice". 
 
 I want to make something clear incase it was not readily picked up on; something that is hard, frustrating, unpleasent and unfun does not mean it is boring. None of those are synonyms for the word. I think a lot of people would do well to remember that.
 
 ![think](/assets/images/gamification/think.png)

Read this [insane lunatic rant](https://onecloudemoji.github.io/games/2004-gaming/) for an in-depth rant on why games have been shit for the past 15 years or so. And essentially, the same principles apply. Getting humans addicted to something so the creators can literally soak up a) their users money and, here’s the most important one, b) their users time so they can expose them to more ads and or profile them to sell to marketers is a solved concept. It has been distilled to a literal forumla, with the user experience literally coming second to making profits. Our little rat brains have been dissected, taken apart and analysed; the mapped game plan of how to get you hooked was formulated not in Dr Xs basement, but in boardrooms across the globe.

![drx](/assets/images/gamification/dr_x.png)
