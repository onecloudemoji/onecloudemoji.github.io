---
title: "Diablo on Linux"
date: 2020-11-22
categories:
  - projects
  
tags:
  - why?
  - games
  - linux
---

One drive home from my ok-in-retrospect-but-very-awful-at-the-time-job I came across [this video](https://www.youtube.com/watch?v=5tADL_fmsHQ). I am not a fan of podcasts; I find youtube videos are always of a higher quality so I like to listen to them like one would a podcast. Eventually it brings to my attention that the Japanese PS1 Diablo port has some source code elements on the disk; a debug symbols file. How this was found is a good question. This file was coupled with more debug info found inside the MPQ archive on the PC version (debug version of the exe with insertion statments), along with 1000 hours of effort to produce a reverse engineered copy of the source. More akin to the [Pokemon Red Disassembly Project](https://github.com/pret/pokered) than just stumbling upon the source ala [this terrible PS1 game which just had the source on the damn disk inside a renamed RAR file](https://tcrf.net/360:_Three_Sixty).

Obviously this is no where near as cool as MVG porting it to a damn switch, nor is this especially unique, but I wanted to do it, so off I went to do it. It took me one work day (minus one very long and very boozy lunch with my [hacking homie](https://kymb0.github.io/) to move through all the different, seemingly unconnected issues I was having. Yes, this looks very, very simple. But when I went through this

- there was no existing Linux template
- I was doing it on Kali Linux because reasons

The simplified cookbook is as follows:

- Obtain GOG Diablo
- Copy diabdat.mpq to a safe place
That has our assets. That is the soul.
- Install the following packages

````cmake g++ libsdl2-dev libsdl2-mixer-dev libsdl2-ttf-dev libsodium-dev cmake-curses-gui````

Ironically the toolset was larger than the game..

- Clone the [github repo](https://github.com/diasurgical/devilutionX)
- Enter build directory
- ````ccmake ..````

This will bring up the ccmake, the user interface for cmake. Rather friendly in all honesty.

It will show the following; this is not an issue.

IMAGE

Press c to enter the configuration screen.

IMAGE

Press c again whilst in the config screen to have the generate option appear

IMAGE

Obviously we want to actually generate our files so we can compile the game.

Once this is done run ````make```` which will take about two or so minutes, then copy your diabdat.mpq file which you put into a safe place into the build folder, and run devilutionx

It takes literal minutes following this recipe.. but the errors were numerous when I was fumbling my way through this process half cut and on a distro entirely unsuited for anything other than boot2roots.

TA DA

IMAGE


