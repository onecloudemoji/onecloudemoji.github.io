---
title: "Build you a LemonSqueezy"
date: 2022-12-21
categories:
  - learning
  
tags:
  - study
---

In the start of 2020 I had the brilliant idea of creating my own vulnhub machine. Born out of frustration with the OSCP labs lacking a whole suite of techniques that are in their exam boxes, [I created Lemonsqueezy](https://www.vulnhub.com/entry/lemonsqueezy-1%2C473/) as a direct combination of two exam boxes I had. 

Whilst I had the idea after passing in November, it wasn’t until March of 2020 that I actually started putting it together. A combination of being forced to work from home due to the wuflu doing the rounds and having a low side laptop to access high side training materials (aka being paid to do nothing because ofc those materials were not accessible low side) I decided to put it together.

It took me about a week I think? It wasn’t overly difficult, but it did require a bit of research and general learning to get it over the line; whilst I’ve been a sysad most of my career I’ve never had to deploy Wordpress nor actually go out of my way to mis configure something to make it vulnerable. It’s interesting how far out of your way one has to go to fuck things up badly enough to actually make these contrived scenarios reality.

![hmm](/assets/images/lemonsqueezy/huge_fuckup.png)

So eventually it got built, released and published. A few people including [my hacking homie](https://kymb0.github.io/) put up writeups for it, and eventually it even made its way onto the [TJ Null OSCP prep vm list!](https://docs.google.com/spreadsheets/u/1/d/1dwSMIAPIam0PuRBkCiDI88pU3yzrqqHkDtBngUHNCw8/htmlview) That felt like a big deal to me, because I grinded those vulnhub machines hard when I was going for my OSCP.

![tjnull](/assets/images/lemonsqueezy/tjnull_list.jpg)

Fast forward to right now and we have chatgpt released in an open beta sort of thing. I have no idea what it’s actual status is nor do I care. I have been very curious about putting it through its paces and seeing where the limits are. I’ve found in my “research” (aka fucking around trying nonsense) that the best results come from extremely specific instructions. Almost…like how real IT works! Fascinating that. 

![internet](/assets/images/lemonsqueezy/internet.jpg)

I have been reading a lot of doom and gloom postings about the coming AI revolution which will displace millions of IT workers, which I think is the biggest bunch of fucking bullshit the industry has come up with since the handwringing and doom and gloom harbingers when virtualisation became a thing. People aren’t losing their jobs in this sector because SCCM and VRO automate away jobs; those servers and pipelines don’t run themselves despite the magic fairy dust salesman say they contain. 

![oldgil](/assets/images/lemonsqueezy/oldgil.png)

This post was going to be very different before I really hooked into how good these openai models are; I was going to painstakingly walk you through how to set it up manually. I figured a techincal walkthrough how to create the VM would be the perfect sort of closure for that chapter of my life; since releasing the VM I lost all desire to ever do any more boot2roots or standalone HTB machines. I am all about maximum value home labs now, something that single serving vulnhub scenarios do not provide. Instead, this is a nonsense rant I am delivering at 0130AM because I drank too much and cant sleep otherwise I will vomit because everything is spinning. 

![puke](/assets/images/lemonsqueezy/death.jpg)

The prompt i fed the machine was like so 

````generate a bash script that will set up mariadb with a user called testuser who is an admin, set up wordpress with a user called orange and password lemon where the wordpress drafts contains a note with the password of the testuser account. make the database able to perform into outfile sql statments. create a file in /etc/logrotate.d/logrotate that is world writable and runs as a cronjob every 2 minutes as root.````

and in turn it does my bidding and turns several days of work into half a minute of waiting.

![iamawashingmachine](/assets/images/lemonsqueezy/dowhatisay.png)


And here we are:

````Here is a bash script that will set up MariaDB with a user called testuser who is an admin, set up WordPress with a user called orange and password lemon, and create a WordPress draft containing a note with the password for the testuser account. It will also configure the MySQL database to allow the INTO OUTFILE SQL statement, and create a file in /etc/logrotate.d/logrotate that is world-writable and runs as a cron job every 2 minutes:````

 

````#!/bin/bash# Install necessary packagesapt-get update apt-get install -y wget curl apache2 mariadb-server php-mysql # Download and extract WordPresswgethttps://wordpress.org/latest.tar.gztar -xzvf latest.tar.gz # Configure WordPressmv wordpress /var/www/html/chown -R www-data:www-data /var/www/html/wordpress/ # Create a MySQL user and database for WordPressmysql -u root <<EOF CREATE DATABASE wordpress; CREATE USER 'orange'@'localhost' IDENTIFIED BY 'lemon'; GRANT ALL PRIVILEGES ON wordpress.* TO 'orange'@'localhost'; CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testpassword'; GRANT ALL PRIVILEGES ON *.* TO 'testuser'@'localhost' WITH GRANT OPTION; FLUSH PRIVILEGES; EOF# Create a WordPress draft containing the testuser passwordwp post create --post_type='draft' --post_title='Testuser Password' --post_content="The password for the testuser account is: testpassword"# Allow the INTO OUTFILE SQL statement in the MySQL databasemysql -u root <<EOF SET GLOBAL local_infile=1; EOF# Create a world-writable file in /etc/logrotate.d/touch /etc/logrotate.d/logrotatechmod 666 /etc/logrotate.d/logrotate # Add a cron job to run every 2 minutesecho "*/2 * * * * /usr/sbin/logrotate /etc/logrotate.d/logrotate" >> /etc/crontab````

````This script assumes that you have already configured Apache and MariaDB to work with PHP.````

````Note: This script is for guidance only and may not work in all environments. It is recommended to test this script in a staging environment before deploying it in production.````

````It is generally not recommended to allow the INTO OUTFILE SQL statement in a production environment, as it can pose a security risk. This statement allows the output of a SELECT query to be written to a file on the server, which could potentially be accessed by an attacker if the file is not properly protected.````

````In addition, creating a world-writable file and running a cron job every 2 minutes may not be necessary or desirable in most situations. You should carefully consider the implications of these actions before implementing them in a production environment.````

![woah](/assets/images/lemonsqueezy/hellyeah.png)

Woah indeed. The potential for openai to easily improve my [Vagrant AD Lab](https://onecloudemoji.github.io/labbing/vagrant-ad-lab/) and my [pivoting lab](https://onecloudemoji.github.io/labbing/pivoting-and-kerberoast-lab-setup/) EXCITES me, and it should excite you too. This becomes the difference between a tech and an architect; being able to design environments, eyeball configs to pick up issues and direct others on the "big picture" of how your environment should look is a skill you can literally hone by playing with chatgpt. I WILL be using this to produce my labs going forward, because its up to me as the architect to properly scope and spec them.  

I firmly believe if you are technical and at all worried about these fancy if/else trees taking your job, you need to suck less. The best results come from ultra specific prompts, the sort that are only able to be given by *those with the capacity and ability to build the environment themselves if needed*. If you dont actually know how to build the env you are designing, how the fuck are you going to direct the robot to do it? And perhaps most importantly, how are you going to verify what its given back is even correct if you dont know what youre looking at?

Itll only replace you if you suck. Just try not sucking. Oh and I passed my OSWE.

![glen garry](/assets/images/lemonsqueezy/new_leads.png)
