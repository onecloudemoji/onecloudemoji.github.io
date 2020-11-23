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

Because I feel like being fancy, I have decided to go on the journey of setting up a fully functioning lab for me to attack in a similar vein to OSCP/HTB labs. This is for two reasons; first and foremost is to improve my infrastructure/sysadmin skills. For the forseeable future this is my career track, so if I can turn study into a fun exercise I will be more likely to engage with it and continue to excel.

![career](/assets/images/pivotinglab/AAACE678-D4F5-4912-B759-A3A67EB8DF38.jpeg) 

The second is I wish to perform things in the labs that simply wouldn't fly in any other commercial pentesting lab environment. I want to deploy disgusting malware, perform phishing using [user automation frameworks to simulate little beanbags](https://github.com/lorentzenman/sheepl) who fall (or not!) for my scans, and perhaps most of all I want to feel secure in the knowledge some dickhead isn't going to revert the box I am 9 hours deep in (I am looking right at you, [Poison](https://0xdf.gitlab.io/2018/09/08/htb-poison.html)

![fun](/assets/images/pivotinglab/21B4DCC9-54FE-48C7-8F1D-E7468FD42F60.gif)

This first exercise will be a fairly simple dual purpose lab; a two machine domain to practice pivoting and attacking a machine you have no physical connectivity to, and an environment to practice various kerberoasting attacks via SPN abuse (perhaps others as I develop this segment, but that will be another post).

To ease ourselves into the process of hax0rman again (as I have realistically not done any serious works in the pentesting space since passing my OSCP on 11/11/19), we will use server 2012 R2. This opens up a slew of attacks to us since it really is just 2008 in disguise.

![disguise](/assets/images/pivotinglab/ELdtPPSWkAAjfP6.jpg)

This will not walk you through how to install a VM. If you need THAT sort of handholding, this might not be the type of article you are going to get value from. Refer to the about page for more information on what this blog is about. [Try](https://www.freecodecamp.org/news/what-is-a-virtual-machine-and-how-to-setup-a-vm-on-windows-linux-and-mac/) [one](https://www.howtogeek.com/196060/beginner-geek-how-to-create-and-use-virtual-machines/) [of](https://lifehacker.com/how-to-set-up-a-virtual-machine-for-free-1828969527) [these](https://docs.microsoft.com/en-us/virtualization/hyper-v-on-windows/quick-start/quick-create-virtual-machine) [links](https://kb.vmware.com/s/article/1018415) [for](https://www.virtualbox.org/manual/ch01.html) [help](https://www.dnsstuff.com/how-to-set-up-and-configure-virtual-machine-server) [on](https://www.lifewire.com/how-to-create-virtual-machine-windows-10-4770680) [setting](https://www.zdnet.com/article/windows-10-tip-quickly-create-a-virtual-machine-to-test-new-features/) [up](https://www.groovypost.com/howto/create-virtual-machine-windows-10-hyper-v/) [vms](https://blog.storagecraft.com/the-dead-simple-guide-to-installing-a-linux-virtual-machine-on-windows/).

![network_diagram](/assets/images/pivotinglab/network_diag.png)

Two vms (one domain controller, one web server), one domain, two private networks. "Public" access will be through the web server (WS) who has two NICs; one touching the domain controller (DC) and one for regular access. I say "public" because we will put these on host only networks with no real internet access. Feel free to be a rebel and expose these to the real world, I wont stop you; I will genuinely laugh if something bad happens though. 

![sideshowboblaugh](/assets/images/pivotinglab/5360752F-2E99-4B7C-88DC-614BB78DB872.gif)


Set up your VM adapters so we have two different private networks; the addresses are arbitrary and I have already forgotten what strange rationale I had for the specific scopes I chose. 

Install DC, and set it to one of those subnets. This machine will have only one NIC. If you didnt set a good password for your administrator account when building the VM, do that now. Rename the machine, install AD Services, promote to domain controller, add a new forest and name it. Run these in an elevated PS window.

````Rename-Computer -NewName DC````

````Install-windowsfeature AD-domain-services````

````Import-Module ADDSDeployment````

````Install-ADDSForest -CreateDnsDelegation:$false ` -DatabasePath "C:\Windows\NTDS" ` -DomainMode "Win2012R2" ` -DomainName "dirty_sprite.net" ` -DomainNetbiosName "dirty_sprite" `  -ForestMode "Win2012R2" `  -InstallDns:$true `  -LogPath "C:\Windows\NTDS" `  -NoRebootOnCompletion:$false `  -SysvolPath "C:\Windows\SYSVOL" `  -Force:$true````

````Install-WindowsFeature RSAT-ADDS````

![domain](/assets/images/pivotinglab/domain.png)


I have chosen this name because I was halfcut on monster ultra (also known as /sips/) mixed with whisky because I wanted to try replicate this strange, extremley potent thing I had in Japan from one of the literally thousands of Lawsons that are fucking everywhere in Tokyo. It had the texture and flavour of softdrink but with 9% alcohol per can, made by Suntory and called ZERO or something. It came close and I got ripped real fast, so mission acomplished I guess.

![crabjuice](/assets/images/pivotinglab/2092B4A7-3CD3-4DDA-A7FE-DB5C09D02404.jpeg)

Now we are going to create a user. This little guy will be the one to serve us apache. dsa.msc will bring up ADUC. I called my user testicles with the password testicles, set the password to never expire and prevent user from changing it. Here is a PS command to do the same thing for the domain; the /domain switch says to not make him a local account on DC.

````net user testicles testicles /ADD /DOMAIN````

In order to perform the kerberoast attack, we need to create a service account with an SPN to abuse. Use the PS command above and create a new account, it can be anything. Since we are professionals we will call it TP4MyBunghole, because I am very excited to hear a 202X season of Beavis and Butthead is coming. Give it a password found in your wordlist of choice, since cracking the hash is one exercise we can do once its all built. Nothing like variety.

````net user TP4MyBunghole pw_found_in_your_wordlist /ADD /DOMAIN````

Set up the SPN like so:

````setspn -A DC_NAME/ACCOUNT_NAME.DOMAIN.SUFFIX:60111 Domain\Account````  

![ad_abuse](/assets/images/pivotinglab/setspn.png)


Wehave finished with the DC. Taking a snapshot of the DC at this point is not a good idea just FYI; the webserver isnt in AD and I cant attest to what will happen if you restore the WS who thinks it is in AD to this DC state which obvioudly does not have the machine we haven't created yet in its AD. I may try and report back.


![ad_abuse](/assets/images/pivotinglab/23C74A94-4915-4A5C-AA7A-66C887412FD7.gif)

Create a new VM for WS (you are free to name these as you wish, I am not your robot supervisor), give this two NICs, set one to the same subnet as the DC and the other one to your "public" network. Rename the new machine, join it to the domain.



Make sure your subnets are networking instead of NOTworking; from this machine make sure you can ping your attack machine (which is ONLY on subnet1) and the domain controller (which is ONLY on subnet2). 

![sorcery](/assets/images/pivotinglab/urawizard.jpg)

Next we want to download WAMP, because this is much, much easier than doing it seperatley. Before you install it, install these runtimes (assuming you have a raw R2 installation and not a patched/slipstreamed version)

https://www.microsoft.com/en-au/download/details.aspx?id=40784
https://www.microsoft.com/en-au/download/details.aspx?id=30679

We are good to install.

When it is installed, edit httpd.conf (wamp\bin\apache\apacheX.X.X\conf) to put the IP of the webserver and what port you want it to hang off into the "Listen" section as shown below.

![listenhereulilshit](/assets/images/pivotinglab/listen.jpg)

Add rules in the firewall for 80 and 3306; only the inbound is needed. If you forget this part, it will not work. Its easy as tho.

![fwrules](/assets/images/pivotinglab/firewall.png)

Edit the http-vhost conf (\wamp\bin\apache\apacheX.X.X\conf\extra) to add this

````Require all granted````

in between the directory tags. Delete everything else in between the directory tags, as per [this guide](https://stackoverflow.com/questions/89118/apache-gives-me-403-access-forbidden-when-documentroot-points-to-two-different-d) From memory this was to fix it so I can view the apache server from my attack box, where as until I did this I could only see it from local host? The issues I encountered are very very different from when I did WAMP attacks on my local box for OSCP prep thats for sure..


Obviously this is a super retarded idea in the real world, but for our lab to demonstrate a technique and provide a vector we will allow remote access from ANY host to user root. Who has no password. Open cmd in the folder your mysql exe is (wamp\bin\mysql\mysqlX.X.X\bin) and feed it this:

````mysql.exe -u root````

````create user 'root'@'%' identified by '';````

````grant all privileges on *.* to 'root'@'%'````

````with grant option;````

It reads easy enough; create user root at any location, identified by nothing, give access to everything on everything to root from any location with the grant option.

But wait! Why are we creating root when we logged into sql to run these commands as root? Well turns out that localhost root and a remote location root are actually two seperate accounts! The root you used to create the remote root are infact two seperate accounts. So when remote root pwns the network, it wont be your account who did it. Technically. 

![clone](/assets/images/pivotinglab/A7E29E17-6D4D-4FC8-9B8F-3792B56EC036.jpeg)


Next we will make an amendment to the mysql configuration file to allow us to use the insert into outfile command. Edit ````C:\wamp64\bin\mysql\mysql5.7.31\my.conf```` and edit the ````secure_file_priv```` to ````=""```` like so
````secure_file_priv=""````

Download setacl from [https://helgeklein.com/download/](https://helgeklein.com/download/)

What this program will do is give our dear old testicles the ability to start and stop the apache and sql services. On windows these services can only be started and stopped by an admin (in pure honesty I am unsure if it is the same on linux, I just know when you catch apache shells they are www-data usually, rather than an admin).

Run the following to allow testicles to start the services

````setacl.exe -on "wampapache64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace````

````setacl.exe -on "wampmysqld64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace````

````setacl.exe -on "wampmariadb64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace````

Give testicles full control over the base wamp folder, otherwise you get "ah00015 unable to open logs" when you try start the services after giving control of them to your new user. I right clicked the folder and in the security tab of properties did it that way. Trying to find a PS method was taking too long when its about three clicks to acheive this. If you find a self contained one liner, do let me know.

![tellmemore](/assets/images/pivotinglab/E6C5D755-6EAF-42AC-B1C6-878BF59603F1.jpeg)


Pull up services.msc, right click, properties on mysql/apache etc. There is a tab "Log On". Select "This account", browse, change the scope to EVERYWHERE, select testicles or whoever you created who has no admin access. Why do we bother? Well you CAN leave it as "Local System Account" if you like, its just when you catch your webshell, it will come back as NT SYSTEM. And thats just no fun. 

![sadlyseesaws.exe](/assets/images/pivotinglab/842CEF40-E5D1-4FAA-993C-5BB46C672289.gif)


Restart the services, and you will see the status change to Running. If you get errors that are not covered here, check your windows event viewer, or reread these steps to see if you skipped something because I have covered much painful ground work with these strange and esoteric steps. If neither of these help, youre on your own buddy.

![help](/assets/images/pivotinglab/418F526D-1944-4FF0-AE82-8EDC67238465.gif)

So now we have a basic lab setup. What can we do now we have made these strange esoteric changes? 
- Remote access to SQL
- Apache server served with a domain account that is not admin, providing an opertunity to priv esc rather than a remote r00t
- Service account set up with a kerberoastable SPN
- Seperate attack surface on a seperate subnet accessiable via pivoting

There is plenty here to play with; its  a nice little playground for various forms of experimentation. There are many methods of escalating and moving around the domain, with and without metasploit. This post will not cover those however; this is strictly for how to build the lab. Some various ways to attack the lab will be detailed [here](link to page)

Congratulations you have built some infrastructure.

![dance](/assets/images/pivotinglab/5A6BCEDA-C9C3-4744-B875-7405FC416319.gif)
