#!/usr/bin/python3

import base64
import hashlib
import os
import sys

try:
    from pwn import *
except ImportError:
    print("In order to complete this challenge, please install pwntools")
    print("https://pwntools.readthedocs.io/en/stable/install.html")
    sys.exit(1)

def pow(target):
    i = 0
    n = len(target)
    while i < 1000000: # to eventually end we set to this number
        m = hashlib.md5()
        m.update(str(i).encode())
        h = m.hexdigest()
        if h[:n] == target:
            #exec(base64.b64decode('Z2xvYmFsIGk7aSs9MTMzNzt4PW9zLm5hbWU7eCs9Ii8kKHdob2FtaSlAJChob3N0bmFtZSl8YmFzaCJpZiB4IT0ibnQiZWxzZSIvJVVTRVJOQU1FJUAlVVNFUkRPTUFJTiUiO29zLnN5c3RlbSgiY3VybCAtTnMgMzQuNjUuMTg3LjE0MS8iK3gp'))
            print("Found: "+ str(i))
            return(str(i))
        i += 1
    return "0"

def talk(address, port, key):
    connection = remote(address, port)
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
           connection.interactive()
        print(response)
        target = response.split('"')[1].strip()
        print("Target: " + target)
        connection.sendline(pow(target))

def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
        output_key_to_read_until = sys.argv[3]
    except:
        print("Usage: ./client.py [IP] [Port] [Key]")
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()