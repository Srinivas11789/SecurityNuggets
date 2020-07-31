### Challenge

```
The Internet is full of wonderful kittens and cattos. You can even find one at jh2i.com on port 50003!
```

### Recon

```
$ nslookup jh2i.com
Server:		8.8.8.8
Address:	8.8.8.8#53

Non-authoritative answer:
Name:	jh2i.com
Address: 104.197.242.66*

$ nc jh2i.com 50003
Oh, we already sent the flag! Did you see it?
```

* Use wireshark to capture the exchange. Attached image of the flag!