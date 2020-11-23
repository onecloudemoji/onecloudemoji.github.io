---
title: "Setting up a pivoting and kerberoasting lab"
categories:
  - Labbing
tags:
  - Windows
  - Lab
  - Kerberoast
  - Pivoting
---

Because I feel like being fancy, I have decided to go on the journey of setting up a fully functioning lab for me to attack in a similar vein to OSCP/HTB labs. This is for two reasons; first and foremost is to improve my infra/sysadmin skills. For the forseeable future this is my career track, so if I can turn study into a fun exercise I will be more likely to engage with it. The second is simply I wish to perform things in the labs that simply wouldn't fly in any other commercial pentesting lab. I want to deploy disgusting malware, perform phishing using user automation frameworks to simulate little beanbags who fall (or not!) for my scams, and perhaps most of all, I want to feel secure in the knowledge some dickhead isnt going to revert the box I am 9 hours deep in (I am looking right at you, [Poison](poison HTB link)

This first exercise will be a fairly simple double purpose lab; a two machine domain to practice pivoting and attacking a machine you have no physical connectivity to, and to practice various kerberoasting attacks via SPN abuse (perhaps others as I develop this segment, but that will be another post).

To ease ourselves into the process of hax0rman again (as I have realistically not done any serious works in the pentesting space since passing my OSCP on 11/22/19), we will use server 2012 R2. This opens up a slew of attacks to us, and is new enough to support some of the quality of life features I find missing from earlier server versions.

This will not walk you through how to install a VM. If you need THAT sort of handholding, this might not be the type of article you are ready for. [Try](https://www.freecodecamp.org/news/what-is-a-virtual-machine-and-how-to-setup-a-vm-on-windows-linux-and-mac/) [one](https://www.howtogeek.com/196060/beginner-geek-how-to-create-and-use-virtual-machines/) [of](https://lifehacker.com/how-to-set-up-a-virtual-machine-for-free-1828969527) [these](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine) [links](https://kb.vmware.com/s/article/1018415) [for](https://www.virtualbox.org/manual/ch01.html) [help](https://www.dnsstuff.com/how-to-set-up-and-configure-virtual-machine-server) [on](https://www.lifewire.com/how-to-create-virtual-machine-windows-10-4770680) [setting](https://www.zdnet.com/article/windows-10-tip-quickly-create-a-virtual-machine-to-test-new-features/) [up](https://www.groovypost.com/howto/create-virtual-machine-windows-10-hyper-v/) [vms](https://blog.storagecraft.com/the-dead-simple-guide-to-installing-a-linux-virtual-machine-on-windows/).

Two vms (one domain controller, one web server), one domain, two private networks. "Public" access will be through the web server (WS) who has two NICs; one touching the domain controller (DC) an one for regular access. I say "public" because we will put these on host only networks with no real internet access. Feel free to be a rebel and expose these to the real world, I wont stop you. 

![network_diagram](/assets/images/pivotinglab/network_diag.png)

Set up your VM adapters so we have two different private networks; the addresses are arbritray and I have already forgotten what strange rationale I had for the specific numbers I chose.

IMAGE OF NETWORKS


Install DC, and set it to one of those subnets. This machine will have only one NIC. Rename the machine (it will reboot), install AD Services, promote to domain controllrt, add a new forest and name it. I have chosen this name because I was halfcut on monster ultra (also known as /sips/) mixed with whisky because I had fuck all else.


PS COMMAND TO RENAME MACHINE, TEST IF IT ASKS FOR AUTH WITH NO PW LOL
Rename-Computer -NewName DC

IMAGE OF ADS ADD AND FOREST AD


Now we are going to create a user. This little guy will be the one to serve us apache. dsa.msc will bring up ADUC. I called my user testicles with the password testicles, set the password to never expire and prevent user from changing it. Here is a PS command to do the same thing for the domain; the /domain switch says to not make him a local account on DC.

````net user testicles testicles /ADD /DOMAIN````

create service account
add spn

PHOTOS OF SUCCESSFUL ADD


Create a new VM for WS (you are free to name these as you wish, I am not your robot supervisor), give this two NICs, set one to the same subnet as the DC and the other one to your "public" network. 

Once it has installed, rename the new machine, join it to the domain. Here is some PS to get it on. It also works by going control panel, system, etc. 

````Rename-Computer -NewName "WS" -DomainCredential dirty_sprite\administrator -Restart````
````Add-Computer -DomainName dirty_sprite -Restart````

Next we want to download WAMP, because this is much, much easier than doing it seperatley. Before you install it, install these runtimes (assuming you have a raw R2 installation and not a patched/slipstreamed version)
https://www.microsoft.com/en-au/download/details.aspx?id=40784
https://www.microsoft.com/en-au/download/details.aspx?id=30679

We are good to install.

edit conf to put ip into listener
GET CLEAR INSTRUCTIONS FOR THIS

add a rule in fw for 80 and 3306
TEST IF THE WEB SERVER WILL STILL PUNCH A HOLE IF YOU DO NOT OPEN THESE PROTS?

edit the http-vhost conf to add this
Require all granted
as per https://stackoverflow.com/questions/89118/apache-gives-me-403-access-forbidden-when-documentroot-points-to-two-different-d
GET MORE INSTRUCTIONS


Obviously this is a super retarded idea in the real world, but for our lab to demonstrate a technique and provide a vector we will allow remote access from ANY host to user root. Who has no password. Run mysql and feed it this:

PUT INSTRUCTIONS ON HOW TO OPEN A SHELL

````create user 'root'@'%' identified by '';````

````grant all privileges on *.* to 'root'@'%'````

````with grant option;````

It reads easy enough; create user root at any location, identified by nothing, give access to everything on everything to root from any location with the grant option.

But wait! Why are we creating root when we logged into sql to run these commands as root? Well turns out that localhost root and a remote location root are actually two seperate accounts! The root you used to create the remote root are infact two seperate accounts. So when remote root pwns the network, it wont be your account who did it. Technically. 

Next we will make an amendment to the mysql configuration file to allow us to use the insert into outfile command. Edit ````C:\wamp64\bin\mysql\mysql5.7.31\my.conf```` and edit the secure_file_priv to = "" like so
````secure_file_priv=""````

Download setacl from [https://helgeklein.com/download/](https://helgeklein.com/download/)

What this program will do is give our user testicles the ability to start and stop the apache and sql services. On windows these services can only be started and stopped by an admin (in pure honesty I am unsure if it is the same on linux, I just know when you catch apache shells they are www-data usually, rather than an admin)

Run the following to allow testicles to start the services

````setacl.exe -on "wampapache64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace````

````setacl.exe -on "wampmysqld64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace````

````setacl.exe -on "wampmariadb64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace````

Give testicles full control over the wamp folder, otherwise you get "ah00015 unable to open logs" when you try start the services after giving control of them to your new user.

Pull up services.msc, right click, properties on mysql/apache etc. There is a tab "Log On". Select "This account", browse, change the scope to EVERYWHERE, select testicles or whoever you created who has no admin access. Why do we bother? Well you CAN leave it as "Local System Account" if you like, its just when you catch your webshell, it will come back as NT SYSTEM. And thats just no fun. Restart the services, and you will see the status change to Running. 

If you get errors that are not covered here, check your windows event viewer, or reread these steps to see if you skipped something because I have covered much painful ground work with these strange and esoteric steps.

So now we have a basic lab setup. What can we do now we have made these strange esoteric changes? 
- Remote access to SQL
- Apache server served with a domain account that is not admin, providing an opertunity to priv esc rather than a remote r00t
- Service account set up with a kerberoastable SPN
- Seperate attack surface on a seperate subnet accessiable via pivoting

There is plenty here to play with; its  a nice little playground for various forms of experimentation. There are many methods of escalating and moving around the domain, with and without metasploit. This post will not cover those however; this is strictly for how to build the lab. Some various ways to attack the lab will be detailed [here](link to page)

Congratulations you have built some infrastructure.

![dance](/assets/images/pivotinglab/5A6BCEDA-C9C3-4744-B875-7405FC416319.gif)
