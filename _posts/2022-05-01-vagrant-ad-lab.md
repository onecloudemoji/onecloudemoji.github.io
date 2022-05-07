---
title: "Automated Active Directory Lab"
date: 2022-05-01
categories:
  - Labbing
  
tags:
  - Windows
  - Lab
  - Kerberoast
  - Vagrant
---

On a trip away, I caught up with my [hacking homie](https://kymb0.github.io/) for a bit. We commenced work on some personal projects while watching lotr and sipping whisky. What was born from this was the finalisation of a project that’s been on my todo list for literally years; [self deploying AD infrastructure](https://github.com/onecloudemoji/ADLAB).

![frodo](/assets/images/vagrant/it_is_done.png)

The reality is when I started down this path, I avoided doing Active Directory exploitation because it was just too time consuming to set up infrastucture, use a single attack to destroy it, and then need to stand it up again. This is the sort of tool I wanted to exist when I was begining my journey. 

What is most important though, is the deployment of the [badblood project](https://github.com/davidprowe/BadBlood) within the DC. It automatically fills your domain with some wack shit for you to practice your AD techniques on. Heaps of stuff a bloodhound instance will pick up; SPNs, about 2500 users (some whom are ACTUALLY DOMAIN CONTROLLERS), some with weak, weak passwords for kerberoasting superduper random permissions (some that are totally nonsensicle just for experimenting) and the meat of it all, ACLs. This was one of the most interesting parts of doing work in [OFFSHORE](https://www.hackthebox.com/hacker/pro-labs), the strange ways that I had no idea AD could work. Due to the randomization of this tool though, a lot of scenarios not possible to see in those static environments will appear.

![offshore](/assets/images/vagrant/offshore.png)
Here is a casual flex because I cannot find an appropriate picture to put here.

Years beforehand, I had heard of vagrant and their specific vmware workstation plugin. At the time, it was a paid product, so I put it on hold until I had the time to really dig into something with a cost on it. I hadn’t known the plugin had become open source until that study day; I was actually going to present a case to work to have them purchase it for me lol. Was a hell of a convenient coincidence.

![money](/assets/images/vagrant/money.png)

This is the first stage of the project; it will morph into various variants; eventually there will be a fully automated version of the entire [pivot lab project](https://onecloudemoji.github.io/labbing/pivoting-and-kerberoast-lab-setup/) and various other things. There is no timeline for release, but I need it taken off my whiteboard where it has been since 2019.

![todo](/assets/images/vagrant/todo.png)

This project took a lot more work to sort out than I expected. Mostly because I was framing it wrong. This is a two phase execution; first packer creates the base golden image, then vagrant "provisions" the image. Except its not golden images in the sense I’m used to; the .box file that’s created from packer has already had the OS installed, and packer turns the .box into a .vmx, where I was imagining the golden image was the thing being installed by vagrant, like an image being pushed by sccm. If that still seems confusing, try this: packer creates the vm, installs the OS, performs any setup listed in the unattended.xml, and then crunches this all into a compressed vm image. Vagrant then takes this compressed image, powers it up, and runs any provisioning scripts you set. 

![confusing](/assets/images/vagrant/confusing.png)

So how does this all work? Well there is a list of setup instructions and prereqs in the readme. This post will not go into detail about them. Feel free to send me a message on LinkedIn if you need a hand getting it set up.

As seen in the readme, the first command we run from inside the folder is ````packer build DC.json````

Packer takes in the json, which starts setting a few things up. External scripts and shit you want run during build can be hosted on a floppy, such as the unattended.xml etc. Inside the builders section you can specify which hypervisor you are using. there’s a few different options, inc hyper v and other bullshit solutions. There’s ability to provision to esxi, but the only reason I was using esxi in the past for my automated lab was the costing of the vagrant plugin. I think I have released those shitty scripts somewhere XXXX

![esxi](/assets/images/vagrant/esxi.jpg)

Reviewing this json post release and I can see all the variables I have set were completely unnecessary, but may aid others in understanding what’s going on. The post processors section is where you can set the output name and dir of your box file. This is NOT the same thing as output directory; THAT is only a temp space for the vm to be built! It also appears the checksum makes literally 0 difference whether its set correctly; I was accidentally using the md5 hash instead of the sha1 and packer didn’t notice. but it will complain if you leave it empty.

![complain](/assets/images/vagrant/complain.png)

Half the battle in this project was wrangling the unattended.xml. There’s a lot of left over artifacts in there showcasing the development of my logic. There’s quite a few things you can NOT do in the out of box deployment phase. Here we set up part of the work in getting this into a domain controller. We set a scheduled task to change the ip address at every boot so it stays static. We set this because there’s some issue with vagrant. When you set up a dhcp address reservation using vmware, vagrant will not realise an address has been handed out to the machine, and the provisioning process will hang thinking its still waiting for an address to be handed out. tbh I should investigate this a bit more and report it to vagrant, but that can do on the ever increasing to do list.

Getting the badblood folder unzipped has been commented out of the unattended, because SOMETIMES, not always, which was irritating, it wouldn’t unzip completely before the shutdown was triggered, meaning the badblood installation would fail. 
![fail](/assets/images/vagrant/want_to_fail.png)

The vagrant_file.template is where the real fun begins. This is where we manually specify modifications to the .vmx file itself. Setting the vmnetwork it connects to, the cpu count, ram etc etc. There’s no limit to the modifications you can make here. What’s listed was all I needed to get this working, but you can do way more. XXXX site link

Set your winrm.host address to the address you set to be statically assigned in the ip update script. The provisioning process will not allow an ip change after winrm has made a connection. This was an important note I needed to keep track of. I mention it in case I need to know it later.

Ensure the shared folders is disabled. as part of the process I made sure vmware tools was NOT installed. I don’t need it for this, and it was a fucking hassle even attempting to get it working. So I just bypassed it entirely.

![whatsthepoint](/assets/images/vagrant/whatsthepoint.png)

The shell provisioners are scripts executed inline against the box. They are executed in order of listing. The set registry is named so because of my previous idea to use reg keys to know when and when not this machine was a domain controller. I abandoned this for simply setting a new scheduled task during the dc promo stage, which will trigger at next reboot (after the dc has completed its promo entirely)

Whilst this all sounds logical and straightforward, the truth was it took a lot a LOT of tinkering with logic and flow to piece this together in this fashion. Truth be told this all came to me while contemplating death whilst getting part of my leg sleeve coloured in. This is NOT the order WHATSOEVER you’d use if you were deploying this by hand. It certainly was humbling to be plagued by this for so many fucking weeks.

![disabled](/assets/images/vagrant/disabled.png)

So once we have appropriately configured our files (or not! It is not necessary to configure anything to get this working out of the box!) the next think we need to do it have vagrant add our .box file as a full virtual machine image. 

````vagrant box add DC file://EXPLICIT LOCATION YOU CREATED THE BOX INCLUDING DRIVE LETTER/DC.box````
This is the only part of the build that I am not happy with; I do not know how to have vagrant accept the .box file with a relative path. To add a bit of clarity, here is the actual command I was issuing to have my box added whilst building this ````vagrant box add DC file://L:/ADLAB/machines/DC/DC.box````

The last piece of the puzzle is the Vagrantfile within the root. This is what ties it all together. After creating the box with packer, it technically doesnt have a name yet. But if we inspect the previous command we can see ````add DC```` the DC argument is the name vagrant will give the vm. Yes this may be confusing since we named the box DC, inside the OS itself and outside. But it all ties together inside the Vagrantfile. ````    domaincontroller.vm.box = "DC"```` lists the name of the vm that vagrant will power on when issing the final command ````vagrant up````

Good lord that was exhausting to type out.

![exhausting](/assets/images/vagrant/exhausting.png)

Well I got there in the end, and it works. Its a nice standalone piece. I was thinking of having this also provision the workstation, but I am not sure how necessary and useful that would be. A workstation is easy as fuck to move between domains, where as standing up and down a dc is no easy task. There is a hell of a story that I am referencing from my days working at a local MSP that one day I will link here, but it needs heavy sanitization and I may not ever get to it.

![secret](/assets/images/vagrant/topsecret.png)

It is interesting just how much has changed since my last lab post, which was put up when I honestly didn't think I was going to get into sec. I was making mad stacks contracting as a sysad, and thought I was going to stick with that for a the rest of my days. I just enjoyed doing this sort of stuff for fun. Its that wonderful intersection of both my interests; infrastructure and hacking. Turns out that tired, trite shit about money not being everything actually holds some weight. Who would have known that young people are fucking stupid.

It also feels very, very good to complete another project. Makes me want to kick more things off that to do list. Something something object in motion and all that. 

![fin](/assets/images/vagrant/fin.png)

