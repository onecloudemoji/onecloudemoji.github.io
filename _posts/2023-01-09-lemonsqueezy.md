---
title: "Build you a lemonsqueezy"
date: 2023-09-01
categories:
  - learning
  
tags:
  - study
---

In the start of 2020 I had the brilliant idea of creating my own vulnhub machine. Born out of frustration with the OSCP labs lacking a whole suite of techniques that are in their exam boxes, I created Lemonsqueezy as a direct combination of two exam boxes I had. 

Whilst I had the idea after passing in November, it wasn’t until March of 2020 that I actually started putting it together. A combination of being forced to work from home due to the wuflu doing the rounds and having a low side laptop to access high side training materials (aka being paid to do nothing because ofc those materials were not accessible low side) I decided to put it together.

It took me about a week I think? It wasn’t overly difficult, but it did require a bit of research and general learning to get it over the line; whilst I’ve been a sysad most of my career I’ve never had to deploy Wordpress nor actually go out of my way to mis configure something to make it vulnerable. It’s interesting how far out of your way one has to go to fuck things up badly enough to actually make these contrived scenarios reality.  

So eventually it got built, released and published. A few people including my hacking homie put up writeups for it, and eventually it even made its way onto the [TJ Null OSCP prep vm list!](https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview) That felt like a big deal to me, because I grinded those vulnhub machines hard.

![tjnull](/assets/images/lemonsqueezy/tjnull_list.jpg)

Fast forward to right now and we have chatgpt released in an open beta sort of thing. I have no idea what it’s actual status is nor do I care. I have been very curious about putting it through its paces and seeing where the limits are. I’ve found in my “research” (aka fucking around trying nonsense) that the best results come from extremely specific instructions. Almost…like how real IT works! Fascinating that. 

I have been reading a lot of doom and gloom postings about the coming AI revolution which will displace millions of IT workers, which I think is the biggest bunch of fucking bullshit the industry has come up with since the handwringing and doom and gloom harbingers when virtualisation became a thing. People aren’t losing their jobs in this sector because SCCM and VRO automate away jobs; those servers and pipelines don’t run themselves despite the magic fairy dust salesman say they contain. 

This post was going to be very different before I really hooked into how good these openai models are; I was going to painstakingly walk you through how to set it up manually. I figured a techincal walkthrough how to create the VM would be the perfect sort of closure for that chapter of my life; since releasing the VM I lost all desire to ever do any more boot2roots or standalone HTB machines. I am all about maximum value home labs now, something that single serving vulnhub scenarios do not provide.


