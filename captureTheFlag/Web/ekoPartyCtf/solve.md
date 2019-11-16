### Challenge
* We know there is a secret behind the traffic 

### Recon or What can go wrong?
* Action message format in HTTP
  - Something to do with its property
* TCP Covert ( through flags? ) - Traffic seems to be legitimate though
* Obtained an object as response --> Structure it?
  - Found different TV/News network from Argentina
* Everything seems straight forward --> Lets look if the server is real and can be communicated?
  - experience from past on a cloud ctf one
  - Also this approach is supportive from challenge description `behind the traffic` ???? :-)
  - Accessing https://wtf.eko.cap.tf/ is a success so probably something is...
```
srimbp-623:central sri$ sudo nmap -sS wtf.eko.cap.tf
Starting Nmap 7.70 ( https://nmap.org ) at 2019-09-25 17:22 PDT
Nmap scan report for wtf.eko.cap.tf (52.202.106.196)
Host is up (0.11s latency).
rDNS record for 52.202.106.196: ec2-52-202-106-196.compute-1.amazonaws.com
Not shown: 999 filtered ports
PORT   STATE SERVICE
80/tcp open  http

Nmap done: 1 IP address (1 host up) scanned in 14.34 seconds
```
  - Accessing via browser throws `No valid request received`
  - next thing to try is replay the same HTTP request and access different property ?
  - Using things here https://stackoverflow.com/questions/36545193/transfer-a-wireshark-captured-http-request-to-a-curl-request
  - 

### Raw Payload
```
...........network..
Todo Noticias..country..    Argentina..owner.....availability....   languages...Spanish..   .......network...Cr..nica TV..country.. Argentina..owner.....availability....   languages...Spanish..   .......network...C5N..country.. Argentina..owner.....availability....   languages...Spanish..   .......network...Canal 26..country..    Argentina..owner.....availability....   languages...Spanish..   .......network...Am..rica 24..country.. Argentina..owner.....availability....   languages...Spanish..   .......network...CN23..country..    Argentina..owner.....availability....   languages...Spanish..
```

### Structure it?
* Request 
```
Action Message Format --> EMCA Array --> Property `q` String `arg`
```
* Response
```
network        country    owner   availability  languages
Todo Noticias  Argentina  ....    ...            Spanish  
Crónica TV      Argentina                         Spanish
C5N            Argentina                         Spanish
Canal 26       Argentina                         Spanish
América 24     Argentina                         Spanish
CN23           Argentina                         Spanish

Todo Noticias    
Crónica TV      
C5N            
Canal 26       
Amrice 24      
CN23           
```