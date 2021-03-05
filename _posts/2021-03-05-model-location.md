---
title: "Defining Model Location; aka why the FUCK does the internet not have the answer"
date: 2021-03-05
categories:
  - projects
  
tags:
  - AI
---

This will be another short one. Seems I alternate between massive unwieldly things that will never get read and teeny one sentence posts that are incredibly useless. 

![watchme](/assets/images/model_location/cantpost.gif)

Having a 10GB lump of stuff on my desktop to generate infinitesimally smaller MIDI files in the KBs was driving me mad, so I set up a proper dir for it all to live. Enter stage left, tensorflow not being able to locate my model anymore, despite it LITERALLY being fed to magenta as part of the run command.

![deadbart](/assets/images/model_location/2021-03-05_19h59_10.png)

An arduous look at dr google and a consult with a mate whose an AI enthusiast and I had come up empty handed. I decided out of desperation to open the model checkpoint files in notepad and see what was in there.

![oldgil](/assets/images/model_location/old-gil.jpg)

There the answer lies; in the file so poignantly titled "checkpoint". For some reason this file was statically linking to the files with their absolute path, not their relative. WHY, I dont know. This was the cause of my grief. For some reason, this was not info I could find anywhere. Unhelpful python error messages led me absolutely nowhere.

![mfw](/assets/images/model_location/1su4QZD.jpg)

This is being documented simply so I dont forget it later on. I have plans for that simple little model, and its dependant on being unchained from its static location on my damn desktop.

![chained](/assets/images/model_location/2021-03-05_20h08_53.png)

Also just a reminder that time is slipping away at a more and more frantic pace. It is now the third month of the year. It is 25% through. Things wont ever get more 'manageable ' or more 'under control'. With this in mind I will now spend the entire weekend in my underpants playing Fable, because that is a good use of my time.
