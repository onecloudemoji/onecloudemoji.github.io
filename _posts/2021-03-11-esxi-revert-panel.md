---
title: "Esxi OSCP Lab Type Revert Panel"
date: 2021-03-11
categories:
  - labbing
  
tags:
  - esxi
  - lab

---

There is an evergrowing list of shit in a little folder on my desktop, called 'blog posts'.

It is filled with half baked and harebrained projects I have worked on at various times.

![idea](/assets/images/esxi/idea.png)

Quite a few of these are simply the result of me being a cheapskate and refusing to purchase a tool that would benefit me and help me acheive my end aim.  This  is one of those projects.

It is the result of spending some serious time within the OSCP labs, and being impressed with the way the users could manipulate the underlying machines. In my days as a sysad I fielded many calls from clients asking us to kick their machines in the guts for them; a  portal like in the labs was mindblowing.

And naturally, I wanted to recreate it. 

This is a retrospective post. It was not written in 2021, but thats what the timestamps I have on  the python script tell me, so this is being backdated.

![lie](/assets/images/esxi/lie.png)

To help clear out that folder (and add another throwaway line to my [capstone blogpost](https://onecloudemoji.github.io/labbing/vagrant-ad-lab/)) this small post was written.

It can be found [here](https://raw.githubusercontent.com/onecloudemoji/onecloudemoji.github.io/master/assets/images/esxi/lab_reset_sanitised.py). I honestly dont even care for it enough to make a whole repo for it. I have moved right on from using esxi as a base. My thinking on  how to ensure the machines were constantly "deployable" was to mark the vhds as read only. That way whenever the machine was re/booted it would go back to its previous state, since nothing can be  written to the file.

This is an actual picture of myself after thinking up this idea.
![stupid](/assets/images/esxi/stupid.png)

Obviously this is fucking retarded. Once again, this comes back to not wanting to spend the money. A SLIGHTLY saner idea would have been to use vcenter to orchestrate and handle snapshotting, with the machine reverting to the known good configuration snapshot on each boot/restart,  but I did not have a license. And when it comes to pirating big boy toys like that, yeah its a no from me.
![pirates](/assets/images/esxi/pirates.png)

But wait, cry the eagle eyed readers of this blog (lol who am i kidding noone reads this shit) dont you use vmware workstation?

Yes fictional reader, I do. 

Are you suggesting you ran vms on an esxi installation inside a vmware workstation installation?

Yes, fictional reader, I did.

As we can see, the issues with this "solution" are mounting up.

The script itself is no exception to this dodgy sort of methodology. As stated, I wasnt working with vcenter, so I did not have the ability to add tags to the machines. This means each machine needed to have a marker for which "stage" it was in (the _l1 and _l2  for level 1 and 2 respectively)

The idea was as you progress and get flags, you will find one that will open up a new network, exactly like the corp/student/admin networks in the OSCP lab. The script is then having a form of "persistence" via the use of cookies.

Its rough, and its  shit. But I can say, IT DID WORK! The irony of  why it was put on hold was once again costing; I need more RAM and more SSDs to host this entire lab. It was going to be 4 levels I think from memory. I just dont have the resources to host all of that all the time.

![poor](/assets/images/esxi/poor.png)

I dont have the desire to complete a project like that anymore; standard boot2roots and CTFs just do not interest me anymore. The reality is the real penetration testing work is nothing like the environments offsec, HTB etc put out. It seems pointless to even do those sort of boxes now I have a different skillset I need to sharpen.

 ![sharpen](/assets/images/esxi/sharpen.png)
 
 This probably sounds more negative than it needed to be. The reality is I became adicted to doing boot2roots whilst trying to get my OSCP because I knew every one I did made it more possible for me to pass. Now there is a distinction here that needs to be picked up on; I was studying to pass OSCP, not get into the field. 
 
 Being a sysad I KNEW the reality was not going to be like those boxes. Maybe 15 years ago. I can see some of that shit appearing in 2006. Not when I was doing it in 2018/2019. I knew enough to know environments just arent built that way, and someone (ie the entire cyber industry) was trying to pull a swifty on me. 
 
![waitasecond](/assets/images/esxi/waitasecond.png)

Anyway stay tuned for more remarks on the industry and other half functional projects.

![broken](/assets/images/esxi/broken.png)
