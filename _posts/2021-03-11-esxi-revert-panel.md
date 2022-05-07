---
title: "Esxi OSCP Lab Type Revert Panel"
date: 2021-03-11
categories:
  - Labbing
  
tags:
  - esxi
  - Lab

---

There is an evergrowing list of shit in a little folder on my desktop, called 'blog posts'.

It is filled with half baked and harebrained projects I have worked on at various times.

![idea](/assets/images/esxi/idea.png)

Quite a few of these are simply the result of me being a cheapskate and refusing to purchase a tool that would benefit me and help me acheive my end aim.  This  is one of those projects.

It is the result of spending some serious time within the OSCP labs, and being impressed with the way the users could manipulate the underlying machines. In my days as a sysad I fielded many calls from clients asking us to kick their machines in the guts for them; a  portal like in the labs was mindblowing.

And naturally, I wanted to recreate it. 

This is a retrospective post. It was not written in 2021, but thats what the timestamps I have on  the python script tell me, so this is being backdated.

![lie](/assets/images/esxi/lie.png)

To help clear it out (and add another throwaway line to my [capstone blogpost](https://onecloudemoji.github.io/labbing/vagrant-ad-lab/)) this small post was written.

It can be found here. I honestly dont even care for it enough to make a whole repo for it. I have moved right on from using esxi as a base. My thinking on  how to ensure the machines were constantly "deployable" was to mark the vhds as read only. That way whenever the machine was re/booted it would go back to its previous state, since nothing can be  written to the file.

This is an actual picture of myself after thinking up this idea.
![stupid](/assets/images/esxi/stupid.png)

Obviously this is fucking retarded. Once again, this comes back to not wanting to spend the money. A SLIGHTLY saner idea would have been to use vcenter to orchestrate and handle snapshotting, with the machine reverting to the known good configuration snapshot on each boot/restart,  but I did not have a license. And when it comes to pirating big boy toys like that, yeah its a no from me.
![pirates](/assets/images/esxi/pirates.png)

But wait, cry the eagle eyed readers of this blog (lol who am i kidding noone reads this shit) dont you use vmware workstation?

Yes fictional reader, I do. 

Are you suggesting you ran vms on an esxi installation inside a vmware workstation installation?

Yes, fictional reader, I did.

As we can see, the issues with this "solution" are mounting up.
