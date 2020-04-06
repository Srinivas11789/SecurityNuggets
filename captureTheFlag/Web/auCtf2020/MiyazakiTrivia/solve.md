### Challenge
```
Miyazaki Trivia
50
http://challenges.auctf.com:30020

Here's a bit of trivia for you vidya game nerds.
```

### Recon
* Connect to the web url - this asks to find a special file
```
kali@kali:~$ curl http://challenges.auctf.com:30020                                                                                                                                                                                       
<doctype html>                                                                                                                                                                                                                            
<html>                                                                                                                                                                                                                                    
        <title>AUCTF</title>                                                                                                                                                                                                              
        <body>                                                                                                                                                                                                                            
                <h1>Find this special file.</h1>
        </body>
</html>
kali@kali:~$ 
```

* Directly running dirbuster or dirb
```
kali@kali:~$ dirb http://challenges.auctf.com:30020/

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Sat Apr  4 00:15:53 2020
URL_BASE: http://challenges.auctf.com:30020/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://challenges.auctf.com:30020/ ----
+ http://challenges.auctf.com:30020/index.html (CODE:200|SIZE:104)                                                                                                                                                                       
+ http://challenges.auctf.com:30020/robots.txt (CODE:200|SIZE:146)                                                                                                                                                                        
+ http://challenges.auctf.com:30020/server-status (CODE:403|SIZE:311)                                                                                                                                                                                                               
-----------------                                                                                                                                                                                                    
END_TIME: Sat Apr  4 00:21:01 2020                                                                                                                                                                                                        
DOWNLOADED: 4612 - FOUND: 3                                                                                                                                                                                                               
kali@kali:~$               
```

* I should have checked some default files before, it is --> `robots.txt`

* Next, 
```
kali@kali:~$ curl http://challenges.auctf.com:30020/robots.txt
VIDEO GAME TRIVIA: What is the adage of Byrgenwerth scholars?

MAKE a GET request to this page with a header named 'answer' to submit your answer.
kali@kali:~$ 
```

### Solve  
```
kali@kali:~$ curl -H "answer: Fear the Old Blood" http://challenges.auctf.com:30020/robots.txt
Master Willem was right.auctf{f3ar_z_olD3_8l0oD}kali@kali:~$ 
```
