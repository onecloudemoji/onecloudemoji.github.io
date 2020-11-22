---
title: "Setting up a pivoting and kerberoasting lab"
categories:
  - Hacking
tags:
  - Windows
  - Lab
  - Kerberoast
  - Pivoting
---

TURN THESE NOTES INTO A BLOG POST

install server 2012 on subnet 1
add ad services
add new forest and name it
create service account
add spn

install server 2012 on subnet 2
add a second adapter and put it to subnet 1
put machine onto domain

download wamp
install these runtimes 
https://www.microsoft.com/en-au/download/details.aspx?id=40784
https://www.microsoft.com/en-au/download/details.aspx?id=30679
install wamp
edit conf to put ip into listener
add a rule in fw for 80 and 3306

edit the http-vhost conf to add this
Require all granted
as per https://stackoverflow.com/questions/89118/apache-gives-me-403-access-forbidden-when-documentroot-points-to-two-different-d

open mysql
create user 'root'@'%' identified by '';
grant all privileges on *.* to 'root'@'%'
with grant option;

edit C:\wamp64\bin\mysql\mysql5.7.31\my.conf
secure_file_priv=""

download setacl from https://helgeklein.com/download/
run the following to allow testicles to start the services

setacl.exe -on "wampapache64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace
setacl.exe -on "wampmysqld64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace
setacl.exe -on "wampmariadb64" -ot srv -ace "n:testicles;p:start_stop,read" -actn ace

give testicles full control over the wamp folder, otherwise you get ah00015 unable to open logs

services.msc
properties on mysql
logon as user testicles who has no admin access
restart mysql
