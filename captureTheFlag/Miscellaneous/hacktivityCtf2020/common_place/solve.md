### Challenge

```
asd7138: can you find the flag here?
tcm3137: no, i dont see it
jwh8163: i cant find it either
rfc5785: i found it
asd7138: what!? where?!
jwh8163: tell us!


Connect here:
http://jh2i.com:50007
```

### Solve

* After a few looking at the source, robots.txt, network and dirb
* Relooking the challenge description
* rfc5785: i found it <-- says he found it
* RFC5785 https://tools.ietf.org/html/rfc5785

```
$ curl http://jh2i.com:50007/.well-known/flag.txt
flag{rfc5785_defines_yet_another_common_place}
```