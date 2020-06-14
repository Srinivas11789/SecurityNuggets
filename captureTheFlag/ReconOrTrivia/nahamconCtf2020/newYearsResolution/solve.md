### Challenge

```
New Years Resolution
50
This year, I resolve to not use old and deprecated nameserver technologies!

There is nothing running on port 80. This is an OSINT challenge.

Connect here: jh2i.com
```

### Recon

* Resorting to DNS lookup / WhoIs / Dig
* Checking all the flags of DNS through nslookup 
* The reference below made sense, ANY record revealed the flag
* Just in case did the nmap scan to not miss anything
* Reference: This made sense
```
* https://blog.cloudflare.com/deprecating-dns-any-meta-query-type/
```

### Solve

```
kali@kali.org$ nslookup jh2i.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	jh2i.com
Address: 161.35.252.71
    
kali@kali.org$ whois jh2i.com
% IANA WHOIS server
% for more information on IANA, visit http://www.iana.org
% This query returned 1 object

refer:        whois.verisign-grs.com

domain:       COM

organisation: VeriSign Global Registry Services
address:      12061 Bluemont Way
address:      Reston Virginia 20190
address:      United States

contact:      administrative
name:         Registry Customer Service
organisation: VeriSign Global Registry Services
address:      12061 Bluemont Way
address:      Reston Virginia 20190
address:      United States
phone:        +1 703 925-6999
fax-no:       +1 703 948 3978
e-mail:       info@verisign-grs.com

contact:      technical
name:         Registry Customer Service
organisation: VeriSign Global Registry Services
address:      12061 Bluemont Way
address:      Reston Virginia 20190
address:      United States
phone:        +1 703 925-6999
fax-no:       +1 703 948 3978
e-mail:       info@verisign-grs.com

nserver:      A.GTLD-SERVERS.NET 192.5.6.30 2001:503:a83e:0:0:0:2:30
nserver:      B.GTLD-SERVERS.NET 192.33.14.30 2001:503:231d:0:0:0:2:30
nserver:      C.GTLD-SERVERS.NET 192.26.92.30 2001:503:83eb:0:0:0:0:30
nserver:      D.GTLD-SERVERS.NET 192.31.80.30 2001:500:856e:0:0:0:0:30
nserver:      E.GTLD-SERVERS.NET 192.12.94.30 2001:502:1ca1:0:0:0:0:30
nserver:      F.GTLD-SERVERS.NET 192.35.51.30 2001:503:d414:0:0:0:0:30
nserver:      G.GTLD-SERVERS.NET 192.42.93.30 2001:503:eea3:0:0:0:0:30
nserver:      H.GTLD-SERVERS.NET 192.54.112.30 2001:502:8cc:0:0:0:0:30
nserver:      I.GTLD-SERVERS.NET 192.43.172.30 2001:503:39c1:0:0:0:0:30
nserver:      J.GTLD-SERVERS.NET 192.48.79.30 2001:502:7094:0:0:0:0:30
nserver:      K.GTLD-SERVERS.NET 192.52.178.30 2001:503:d2d:0:0:0:0:30
nserver:      L.GTLD-SERVERS.NET 192.41.162.30 2001:500:d937:0:0:0:0:30
nserver:      M.GTLD-SERVERS.NET 192.55.83.30 2001:501:b1f9:0:0:0:0:30
ds-rdata:     30909 8 2 E2D3C916F6DEEAC73294E8268FB5885044A833FC5459588F4A9184CFC41A5766

whois:        whois.verisign-grs.com

status:       ACTIVE
remarks:      Registration information: http://www.verisigninc.com

created:      1985-01-01
changed:      2017-10-05
source:       IANA

# whois.verisign-grs.com

   Domain Name: JH2I.COM
   Registry Domain ID: 2438848180_DOMAIN_COM-VRSN
   Registrar WHOIS Server: whois.google.com
   Registrar URL: http://domains.google.com
   Updated Date: 2019-09-30T18:01:15Z
   Creation Date: 2019-09-30T18:01:13Z
   Registry Expiry Date: 2020-09-30T18:01:13Z
   Registrar: Google LLC
   Registrar IANA ID: 895
   Registrar Abuse Contact Email: registrar-abuse@google.com
   Registrar Abuse Contact Phone: +1.8772376466
   Domain Status: clientTransferProhibited https://icann.org/epp#clientTransferProhibited
   Name Server: NS-CLOUD-A1.GOOGLEDOMAINS.COM
   Name Server: NS-CLOUD-A2.GOOGLEDOMAINS.COM
   Name Server: NS-CLOUD-A3.GOOGLEDOMAINS.COM
   Name Server: NS-CLOUD-A4.GOOGLEDOMAINS.COM
   DNSSEC: unsigned
   URL of the ICANN Whois Inaccuracy Complaint Form: https://www.icann.org/wicf/
>>> Last update of whois database: 2020-06-13T20:30:38Z <<<

# whois.google.com

Domain Name: jh2i.com
Registry Domain ID: 2438848180_DOMAIN_COM-VRSN
Registrar WHOIS Server: whois.google.com
Registrar URL: https://domains.google.com
Updated Date: 2019-09-30T18:01:15Z
Creation Date: 2019-09-30T18:01:13Z
Registrar Registration Expiration Date: 2020-09-30T18:01:13Z
Registrar: Google LLC
Registrar IANA ID: 895
Registrar Abuse Contact Email: registrar-abuse@google.com
Registrar Abuse Contact Phone: +1.8772376466
Domain Status: clientTransferProhibited https://www.icann.org/epp#clientTransferProhibited
Registry Registrant ID:
Registrant Name: Contact Privacy Inc. Customer 1245566205
Registrant Organization: Contact Privacy Inc. Customer 1245566205
Registrant Street: 96 Mowat Ave
Registrant City: Toronto
Registrant State/Province: ON
Registrant Postal Code: M4K 3K1
Registrant Country: CA
Registrant Phone: +1.4165385487
Registrant Phone Ext:
Registrant Fax:
Registrant Fax Ext:
Registrant Email: y8zsqdxbpa1f@contactprivacy.email
Registry Admin ID:
Admin Name: Contact Privacy Inc. Customer 1245566205
Admin Organization: Contact Privacy Inc. Customer 1245566205
Admin Street: 96 Mowat Ave
Admin City: Toronto
Admin State/Province: ON
Admin Postal Code: M4K 3K1
Admin Country: CA
Admin Phone: +1.4165385487
Admin Phone Ext:
Admin Fax:
Admin Fax Ext:
Admin Email: y8zsqdxbpa1f@contactprivacy.email
Registry Tech ID:
Tech Name: Contact Privacy Inc. Customer 1245566205
Tech Organization: Contact Privacy Inc. Customer 1245566205
Tech Street: 96 Mowat Ave
Tech City: Toronto
Tech State/Province: ON
Tech Postal Code: M4K 3K1
Tech Country: CA
Tech Phone: +1.4165385487
Tech Phone Ext:
Tech Fax:
Tech Fax Ext:
Tech Email: y8zsqdxbpa1f@contactprivacy.email
Name Server: NS-CLOUD-A1.GOOGLEDOMAINS.COM
Name Server: NS-CLOUD-A2.GOOGLEDOMAINS.COM
Name Server: NS-CLOUD-A3.GOOGLEDOMAINS.COM
Name Server: NS-CLOUD-A4.GOOGLEDOMAINS.COM
DNSSEC: unsigned
URL of the ICANN WHOIS Data Problem Reporting System: http://wdprs.internic.net/
>>> Last update of WHOIS database: 2020-06-13T20:29:46Z <<<

kali@kali.org$ sudo nmap -A -sS --top-ports 100 jh2i.com

Starting Nmap 7.80 ( https://nmap.org ) at 2020-06-13 13:32 PDT
Nmap scan report for jh2i.com (161.35.252.71)
Host is up (0.063s latency).
All 100 scanned ports on jh2i.com (161.35.252.71) are closed
Too many fingerprints match this host to give specific OS details
Network Distance: 15 hops

TRACEROUTE (using port 1025/tcp)
HOP RTT      ADDRESS
1   3.84 ms  192.168.0.1
2   3.25 ms  104.192.204.1
3   6.97 ms  te-4.er1.sea180.atlasonnet.com (66.171.189.161)
4   6.99 ms  cr1-sttlwawb-a-te-0-0-0-0.bb.as20055.net (107.191.238.105)
5   7.30 ms  cr2-sttlwawb-a-be16.bb.as20055.net (107.191.236.42)
6   4.29 ms  sea-b2-link.telia.net (62.115.187.118)
7   48.74 ms chi-b21-link.telia.net (62.115.117.49)
8   ...
9   64.17 ms nyk-b3-link.telia.net (62.115.139.151)
10  ... 14
15  62.28 ms 161.35.252.71

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 20.58 seconds
kali@kali.org$ nslookup -type=txt jh2i.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
*** Can't find jh2i.com: No answer

Authoritative answers can be found from:
jh2i.com
	origin = ns-cloud-a1.googledomains.com
	mail addr = cloud-dns-hostmaster.google.com
	serial = 48
	refresh = 21600
	retry = 3600
	expire = 259200
	minimum = 300

kali@kali.org$ nslookup -type=any jh2i.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	jh2i.com
Address: 161.35.252.71
jh2i.com	nameserver = ns-cloud-a1.googledomains.com.
jh2i.com	nameserver = ns-cloud-a2.googledomains.com.
jh2i.com	nameserver = ns-cloud-a3.googledomains.com.
jh2i.com	nameserver = ns-cloud-a4.googledomains.com.
jh2i.com
	origin = ns-cloud-a1.googledomains.com
	mail addr = cloud-dns-hostmaster.google.com
	serial = 48
	refresh = 21600
	retry = 3600
	expire = 259200
	minimum = 300
jh2i.com	rdata_99 = "flag{next_year_i_wont_use_spf}"

Authoritative answers can be found from:

```