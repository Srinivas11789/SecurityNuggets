### Challenge

```
Agent 95
50
They've given you a number, and taken away your name~

Connect here:
http://jh2i.com:50000
```

### Recon
* Checking the web page
* Looks like the hint fro mthe page is 
  * Windows system so we use the user-agent string of win95?
* https://developers.whatismybrowser.com/useragents/parse/2520-internet-explorer-windows-trident
  
### Solve

* Construct request
```
curl -H "User-Agent: Mozilla/4.0 (compatible; MSIE 5.5; Windows 95; BCD2000)" http://jh2i.com:50000/
```

### Flag

```
$ curl -H "User-Agent: Mozilla/4.0 (compatible; MSIE 5.5; Windows 95; BCD2000)" http://jh2i.com:50000/
flag{user_agents_undercover}

<div style="text-align:center">
<br><br><br><br>
<b> NOT CHALLENGE RELATED:</b><br>THANK YOU to Digital Ocean for supporting NahamCon and NahamCon CTF!
<p>
<img width=600px src="https://d24wuq6o951i2g.cloudfront.net/img/events/id/457/457748121/assets/1b5a9739fd31b42fa4eb37ac6b3a6e1c.DOlogo.png">
</p>
</div>
```