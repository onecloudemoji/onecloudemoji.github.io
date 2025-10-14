---
title: "Code Execution out of VST Plugins"
date: 2024-06-07
categories:
  - pentesting
  - music
  
tags:
  - pentesting
  - music
---

For the second time this month I have been forced to realise that I need to build up a golden image for a dedicated development machine. Unrelated to this post but will be mentioned anyway is Parrot is not suited for building AFL++ without enormous amounts of effort, and is equally unsuitable for compiling VST plugins.

A nice easy one tldr on what a VST is: “_A VST plugin is a software module for digital audio workstations (DAWs) that adds audio effects or instruments._” Thanks robot overlord. Why do we care about this particular technology? Well, most of you fictional readers probably won’t at all. This is the least likely thing to ever come up in an engagement, but I think it’s neat.

[A blog post by infosecnoodle](https://www.infosecnoodle.com/p/vst-plug-ins-for-initial-access) (excellent name) got me interested, it’s just that nice intersection between two of my favourite things that gets me excited. If the above analogy didn’t clear it up, VSTs are how the [neural network generated drum loops](https://onecloudemoji.github.io/projects/drums-rnn/) are played back. Looking through and the [linked VST repo](https://github.com/steinbergmedia/vst3_example_plugin_hello_world) gives pretty simple instructions. Literally clone and build, right?

Yes, if you are living in dreamland where the mountains are made of chocolate and the sales people get engagements with enough time on them. 

![chocolateland](/assets/images/vst/chocolate.jpg)

This project, that should have taken me about ten minutes from end to end, has been pushed back for WEEKS because of these unhelpful GitHub instructions. This has infact made me go back and amend my [C.A.P.S.U.L.E.S. instructions](https://onecloudemoji.github.io/labbing/projects/learning/capsules/), simply because these were so dogshit I wasted literal portions of my life.

Much, MUCH is missing from these instructions, holy shit. The following tool chain is required to even begin getting this built (on linux) and is absolutely not mentioned anywhere in the repo.

````apt-get install build-essential cmake git libx11-dev libxrandr-dev libxinerama-dev libxcursor-dev libxi-dev libgl1-mesa-dev libglu1-mesa-dev libfreetype6-dev pkg-config libxcb-util-dev libxcb-cursor-dev libxcb-keysyms1-dev libxcb-xkb-dev libxkbcommon-dev libxkbcommon-x11-dev libcairo2-dev libpango1.0-dev libgtkmm-3.0-dev libsqlite3-dev````

We build, and we wait. My goodness, this takes an enormous amount of time to compile. Oh would you look at that, the vague instructions did not say that those are the commands to compile it ON windows, I assumed these were the instructions to compile it FOR windows, excellent thank you for my error at 94% of the compilation!

![fuckmylife](/assets/images/model_location/2021-03-05_19h59_10.png)

After finally realising how STUPID I was being for applying LOGIC to this repo, I get it built. And already we have a problem. I had assumed, because I am a fucking moron, that Linux and Windows both used the __vst3__ format, because the _vst3 project_ I am compiling is indeed SUPPOSED to be a _vst3 project_, and all my _vst3 plugins on windows_ are, you guessed it, __vst3__ format! But no, they are infact __.so__ on Linux and I am __.so__ fucking over this project already. The only reason I am continuing is because it is on the whiteboard, and things do not get taken off the whiteboard until they are completed. This is simple logic me and my [hacking homie](https://kymb0.github.io/) have used to brute force our ways into being champions of the universe. It cannot come off until it’s done.

![champions](/assets/images/vst/champion.jpg)

One may ask why did I even bother compiling this on Linux when it was always going to be used in a windows based daw? Because the last time I opened visual studio to compile a c# proxy server to reproduce [this blog on NetNTLM relaying](https://badoption.eu/blog/2024/04/25/netntlm.html), it bitched and moaned about needing updates like every modern game does when I open steam. Giving in i update, and imagine my disappointment and resentment for the steinberg repo maintainers (and myself) for not just starting with the windows compilation; it just fucking works. Flawlessly. No issues. Amazing. nothing required at all, it just works. I have wasted so much time trying to jam this project into linux for no good reason, other than I was too lazy to press update.

![disappointment](/assets/images/vst/disappointment.jpg)

Fantastic, where’s the code execution? Well here’s the thing, this is just a cpp application, and we can make it do anything. Because we are compiling an application, essentially. Is it especially tricky to smuggle in some post reqs to a webhook to exfil data? No, not really. As I said this won’t ever come up on a client engagement.

onto the real star of the show, is inserting 

````#include <cstdlib>````
````system("calc.exe");````
	
where the plugin gets created. Astute readers will note I am not using calc in my example.

![code](/assets/images/vst/code.jpg)

Thats it you say? I sat through this nonsense to read about you inserting a call to system? Remember this blog isn’t for you, it is for me. And it is interesting the ways that you can get fucked even by little technologies you don’t even think have the capacity to handle baked in malware. Here is it pushing the response to hostname out to a webhook. Not terribly exciting, but it took 6 seconds to insert and now every single time open this vst, the call is made. Because this is simply code that does not mess with the inner workings of the plugin, it (the plugin) continues to function without any issue.

![champions](/assets/images/vst/webhook.jpg)

What’s going on here is this is an interesting test bed for me to try some interesting vectors in the future, beyond just chucking some c# into __msbuild__ and __csc__. For funsies I shall in a future instalment implement some shellcode runners in cpp, but the pressing need is not there right now since its really got no applicability to work or any thing other project. 

This blog post has been written in the bathtub to satisfy my own personal need to publish. It’s not especially novel or ground breaking, but the other little bits of research I am pursuing are taking a lot longer than I expected. As such I felt a need to publish SOMETHING, and I am just mad that this something, that should have been a 30 minute exercise to put up a 75 word at the maximum post, turned into a slog thats taken most of Q2 to get out and a 1000 word+ diatribe of vitriol.

Also, the [C.A.P.S.U.L.E.S.](https://github.com/onecloudemoji/C.A.P.S.U.L.E.S.) project is now up to 4 independent modules. A regular cadence of one module a quarter has been applied; it will begin to grow out more. 

Back into the lab we go, the research wont conduct itself.

![lab](/assets/images/vst/lab.jpg)


