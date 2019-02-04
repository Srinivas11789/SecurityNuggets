### Cloud

* SubDomain enumeration of a AWS cloud at `neverlanctf.cloud`

Thoughts:
```
The Cloud Capture the flag:

* Level1  —> SubDomain Enumeration (Given a website hosted from GCP or AWS, Find all subdomains —> they assured there is no xss, csrf or anything else…)
    * The page has a comment not to shortcut using `Sublist3r - A subdomain enumeration tool` and that it won’t help us
    * Recon for the cloud:
        * Read through the source code
        * Read through the content
        * Possible subdomains already listed somewhere?
        * Checked an error page —> we get a key and some details in the error page. The error has a key which is base64 encoded and decoding that is also garbage….
            * Could we leverage the error page to find the cloud provider?
            * The error 404 said there was no error.html so it return NoSuchKey
                *  Ok, google for the error returns AWS S3  Bucket
                * Research how AWS S3 handles the subdomains or configures them…
                * Searching for /robots.txt threw this issue
                    * Robots.txt ensure they are now seen by web crawlers
    * http://neverlanctf.s3.amazonaws.com
        * Providing a s3 type url throws —> access denied
    * AWS S3 Recon:
        * AWS S3 domains names == bucket names
        * Its is unique and has a global scope
        * Each subdomains has a separate s3 bucket for it with the same name
            * Subdomains have its own s3 buckets with exact names as subdomains.
    * The level hints that using subdomain enumeration tools won’t be a success like sublist3r

NMAP Scan:
root@kali:~/Desktop/KeyZ# nmap -sS -A neverlanctf.cloud
Starting Nmap 7.70 ( https://nmap.org ) at 2019-02-03 13:59 PST
Stats: 0:00:18 elapsed; 0 hosts completed (1 up), 1 undergoing Traceroute
Traceroute Timing: About 32.26% done; ETC: 13:59 (0:00:00 remaining)
Nmap scan report for neverlanctf.cloud (52.218.192.219)
Host is up (0.047s latency).
rDNS record for 52.218.192.219: s3-website-us-west-2.amazonaws.com
Not shown: 999 filtered ports
PORT   STATE SERVICE VERSION
80/tcp open  http    Amazon S3 httpd
|_http-server-header: AmazonS3
|_http-title: NeverLAN CTF.cloud
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: 3Com SuperStack 3 Switch 3870 (95%), OSRAM Lightify ZigBee gateway (93%), Satel ETHM-2 intruder alarm (92%), HP ProCurve 2524 switch or 9100c Digital Sender printer (92%), Apple TV 5.2.1 or 5.3 (91%), Denver Electronics AC-5000W MK2 camera (91%), NEC UNIVERGE SV8100 PBX (88%), Cisco SG 500 switch (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 22 hops

TRACEROUTE (using port 80/tcp)
HOP RTT      ADDRESS
1   4.92 ms  192.168.0.1
2   24.17 ms 142.254.236.153
3   13.16 ms agg62.lsaicaev01h.socal.rr.com (24.30.168.9)
4   19.99 ms agg11.lsaicaev01r.socal.rr.com (72.129.18.192)
5   18.77 ms agg26.lsancarc01r.socal.rr.com (72.129.17.0)
6   17.66 ms bu-ether16.lsancarc0yw-bcr00.tbone.rr.com (66.109.6.102)
7   14.39 ms 0.ae0.pr1.lax00.tbone.rr.com (107.14.17.248)
8   14.41 ms 24.27.236.33
9   ... 13
14  38.49 ms 205.251.232.61
15  ... 21
22  75.63 ms s3-website-us-west-2.amazonaws.com (52.218.192.219)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 26.55 seconds

Nslookup:

Dig:
* Soa
* Axfr
* dynadot

Whois:

* Used some online subdomain pentest-tools, shodan as well
* It should always be a security misconfiguration or some property of AWS as there must be no obvious bugs in cloud
    * Read about amazon s3 bucket subdomains
* Full name:
    * http://neverlanctf.cloud.s3-website-us-west-2.amazonaws.com

* An easy scan of www.neverlanctf.cloud has a different 404 error while other subdomains are not reachable
* Also, dnscan results show www as a subdomain and stale dns entries of a lot more which were not useful

* Virtual hosting?
    * VH it is
    * Tried Virtual hosting?https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html
    * Tried s3.amazonaws.com
    * http://neverlanctf.cloud.s3.amazonaws.com/
    * Got a new asset
    * Flagxxxx.html
    * Got the level1 flag
    * —> flag-e8ff76090aefae7a958175254ccae055ed0ab6c3.html 
        * List bucket lists
```
