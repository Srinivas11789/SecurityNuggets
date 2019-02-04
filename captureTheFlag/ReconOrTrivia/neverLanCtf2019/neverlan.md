### Trivia

```
* The oldest SQL Injection Vulnerability. The flag is the vulnerability ID.
Ans: `CVE-2000-1233`

* In MSSQL Injection Whats the query to see what version it is?
Ans: `SELECT @@version`

* A domain-specific language used in programming and designed for managing data held in a relational database management system, or for stream processing in a relational data stream management system.
Ans: `SQL`

* A group of similar binary-to-text encoding schemes that represent binary data in an ASCII string format by translating it into a radix-64 representation.
Ans: `base64`

* A small piece of data sent from a website and stored on the user's computer by the user's web browser while the user is browsing.
Ans: `cookie`

* A standard used by websites to communicate with web crawlers and other web robots. The standard specifies how to inform the web robot about which areas of the website should not be processed or scanned
Ans: `Robots Exclusion Standard`

* Why make bacon when you can make a cipher instead?
If only I could remember what it's called...
Ans: ``
Notes:
* https://puzzling.stackexchange.com/questions/8143/one-word-bacon

* A command line tool that tells you whois hosting a particular website?
Ans: `whois`

* What is the common name for a single element of Amazon Simple Storage Service?
Ans: S3 Bucket

* When hosting a site as an S3 bucket, the bucket name must ____ the domain name.
Ans: Match

* What type of namespace prevents two AWS S3 buckets having the same name?
Ans: global

* What does AWS stand for?
Ans: Amazon Web Services

* what does sudo stand for?
Ans: Super User Do

* What is $PATH on linux?
Ans: Environmental Variable
Note: I knew it represents the path but wanted the answer to be brief so tried a simplet env and that was the answer.

* When bash is invoked as an interactive login shell it first reads and executes commands from this file.
Ans: bash_profile

* When bash is invoked as an interactive non-login shell it first reads and executes commands from this file
Ans: bashrc
```

### Recon
```
* occurring in Chicago, Illinois, United States, on the evening of November 22. There was an interruption like nothing we had ever seen before.
What was the name of the Intruder?
Ans: `Max Headroom`

* I love Github. Use it all the time! Just wish they could host a webpage...
Ans: `flag{Th1s_g1thub_l00ks_a_l1l_sparc3}`
Notes: `Assumed it should be githubPages or username.github.io or even thought it should be (assuming title of this challenge purvesta being a hint) --> purvesta.github.io and then found the flag in the repo as lol..`

* Back in the day, Zesty hid a flag in the first version of our website.
Ans: ``

* This organizations creation was announced Mon Sep 24 2001
What is the full name of the organization?
Ans: `Open Web Application Security Project`

* It looks like N30 has been keeping passwords secret with some software he wrote, but he should know better than to rely on proprietary software for security. It looks like he left the repo public too!

Ans: 
root@kali:~/Desktop/KeyZ# ./key -n passwords.keyz 
32 64 331
root@kali:~/Desktop/KeyZ# ./key -g passwords.keyz 
ERROR(key): no key was specified for key file 'passwords.keyz'
root@kali:~/Desktop/KeyZ# ./key -d passwords.keyz 
DEBUG(key): opening passwords.keyz for reading
DEBUG(key): magic bits are: KEYZ
root@kali:~/Desktop/KeyZ# ./key -n passwords.keyz 
32 64 331
root@kali:~/Desktop/KeyZ# ls
HOWTO.md  key.cpp      key.o    makefile        README.md  smaz.h        smaz.o
key       key-man.txt  LICENSE  passwords.keyz  smaz.cpp   smaz-LICENSE
root@kali:~/Desktop/KeyZ# ./key -g passwords.keyz 
ERROR(key): no key was specified for key file 'passwords.keyz'
root@kali:~/Desktop/KeyZ# ./key -g passwords.keyz flag 
flag{bu7_1ts_pr0pr1etary}
�Proot@kali:~/Desktop/KeyZ# 

Notes: 
  * Unrelated research
    - Mobef ransomware trojan 
    - Encrypts all the sensitive info files (predefined file extensions) with RSA 2048 AES CBC 
    - Reference: https://malwaretips.com/blogs/remove-mobef-virus/
    - Changes wallpaper into a ransom note
    - Delievered by: 
      * Email
  * So, Mobef ransomware encrypted file...Decrypt it?
  * neverLan website --> Creators --> N30 (Given in the problem) --> Track N30 in twitter (as no github was given) --> Get real name --> Search + Goto Github account --> Owner of neverLanCtf so we are on right path --> Keyz project --> Make project --> Read readme --> Operating with --n worked giving some values --> It stores key value pairs so we want flag --> get flag 
```