### Challenge
* Breakable
```
Okay...this one's better, but still be careful!

Dev: Sri
```

### Solve
```
kali@kali:breakable$ javac breakable.java 
kali@kali:breakable$ java  breakable
Enter flag: [Ljava.lang.String;@42a57993
What you inputed is: 
[Ljava.lang.String;@42a57993
Stripped flag is:
a.lang.String;@42a5799
Reversed answer is: 
28
16
[, , , , , , , , , , , , , , , ]
[0, m, g, _, 1, m, _, s, 0, _, p, r, 0, u, , ]
[0, m, g, _, 1, m, _, s, 0, _, p, r, 0, u, d, _]
Access denied!


kali@kali:breakable$ javac breakable.java 
kali@kali:breakable$ java  breakable
Enter flag: rtcp{0mg_1m_s0_pr0ud_}          
What you inputed is: 
rtcp{0mg_1m_s0_pr0ud_}
Stripped flag is:
0mg_1m_s0_pr0ud_
Reversed answer is: 
28
16
[, , , , , , , , , , , , , , , ]
[0, m, g, _, 1, m, _, s, 0, _, p, r, 0, u, , ]
[0, m, g, _, 1, m, _, s, 0, _, p, r, 0, u, d, _]
Access granted.
```

* Flag: rtcp{0mg_1m_s0_pr0ud_}