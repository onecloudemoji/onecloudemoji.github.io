---
title: "Using mona with windbg preview"
date: 2023-04-07
categories:
  - projects
  
tags:
  - windbg
  - mona
---

The next thing on my todo list is move into exploit dev. There is a strong amount of crossover between exploit dev and game hacking, which is where my real aim is. All of these require using debuggers. Because I do not wish to go any more blind than I already i am, I refuse to touch the standard version of windbg, nor do I wish to ever in my life fire up immunity again. 

![blind](/assets/images/mona/cheese.png)

windbg preview looks nice, REAL nice. Its a good tool. I WANT to like it, but because its a windows store application, its a fucking nightmare to manipulate. This is another of those trustedinstaller situations, things I thought I had left behind in my sordid sysadmin past. Any problem that repeatedly has the solution "use hirens boot cd" can get absolutley fucked, I am not dealing with bullshit like that.

![old](/assets/images/mona/old.png)

Thankfully, due to some strange oversight that I am not in the mood to investigate any further, whilst changes cant be made INSIDE the windbg preview folder itself, I can do shit TO the windbg folder after taking ownership of it and all sub files (but as mentioned, this somehow excludes the files and folders relating to windbg preview), since it is inside the windowsapps folder. 

So armed with this information, I decided I wasnt going to play MSs game anymore, and simply shipped the files somewhere else. The permissions are just zany, so I zipped up the windbg folder, which put itself into the windowsapps folder, and moved it to a fresh VM. Following a strange mishmash of every set of instructions on [corelans windbglib readme](https://github.com/corelan/windbglib), I was able to get mona running on a bastardised windbg preview.

I seem to be having a lot of issues with the internet lately. There are three possibilities I think are occuring; something is wrong with my google account and my search results are slowly becoming poisoned and results are related to my previous searches, or google search is steadily becoming worse and worse with every passing year, or I have [ONCE AGAIN stumbled upon a problem no other human being has had](https://onecloudemoji.github.io/projects/model-location/). As special as I think I am, the odds of me being the only human being in the infosec sphere who has fucking HAD IT with how hard to read the common debugging tools are and wanting to implement the mona suite into the preview version seem incredibly low. 

![internet](/assets/images/mona/internet.png)

Theres two parts to solving this dillema, each with their own set of problems. The first part is actually getting getting the debugger.

- install windows 10 32bit
- update it to the limit
- install the Windows 10 SDK, version 2004 (10.0.19041.0) from [here](https://go.microsoft.com/fwlink/?linkid=2120735)
- install the windbg preview from the app store
- run an admin cmd prompt with ````takeown /F "C:\Program Files\WindowsApps" /r````
- find the windbg preview folder (mine was Microsoft.WinDbg_1.2210.3001.0_x86__8wekyb3d8bbwe) and send it to a zip folder.
- yeet that zip into a safe space
- trash the vm

Everything Ive read suggests the minute you start messing with the windowsapps folder, the machine is fucked.

![rekt](/assets/images/mona/rekt.png)

Part two, installing mona.

So far I have gotten this working on a windows 32bit machine with the 32bit version of windbg. I have not tried it on anything else, but will certainly update this with different version recipes if I ever feel the need to use them.

- install [python 2.7.18](https://www.python.org/downloads/release/python-2718/) and MAKE SURE you tell it to add to the path
- grab the [corelan repo from here](https://github.com/corelan/windbglib), it has a lot of pieces we require 
- install vcredist from the repo
- open an admin cmd session in ````c:\program files\common files\microsoft shared\vc```` and do ````regsrv32 msdia90.dll````
- put your acquired windbg folder somewhere and extract it in its new home
- put mona.py and windbglib.py from the repo into the ````x86```` folder
- put pykd from the repo into the ````x86\winext```` folder
- ???
- profit


Now we can run it. Attach something to the debugger, run ````.load pykd.pyd```` and issue your mona commands with ````!py mona```` as the prefix instead of the traditional ````!mona````

![dbg](/assets/images/mona/dbg.png)

Delightful.

I have wasted my entire day (which by the way was actually good friday) forcing this shitful program to accept whats good for it, all in a bid to ensure that [my template for buffer overflows](https://github.com/onecloudemoji/BOF-Template) still works. Which it does by the way. Expect a new seh version to arrive soon.

Another mystery solved and another strange project for the blog. See you in the next perhaps slightly useful rant.

![wolfcastle](/assets/images/fable/mcbain.jpg)
