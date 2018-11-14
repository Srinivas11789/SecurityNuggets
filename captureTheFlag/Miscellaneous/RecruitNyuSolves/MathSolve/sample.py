#!/usr/bin/env python
import sys
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    operation = data.split(" ")
    ans = "0"
    if operation[1] == "+":
         ans = int(operation[0]) + int(operation[2])
    if operation[1] == "*":
         ans = int(operation[0]) * int(operation[2])
    if operation[1] == "-":
         ans = int(operation[0]) - int(operation[2])
    if operation[1] == "//":
         ans = int(operation[0]) // int(operation[2])
    return str(ans)

def pwn(address, port):
    connection = remote(address, port)
    # Let's print the data we receive from this server
    print connection.recvuntil(":")
    # Let's send it some data!
    connection.sendline("Name")
    # Let's print the data we receive from this server, but also store it
    for i in range(200):
        response = connection.recvuntil(":")
        print response
        # Hmm, they seem to be asking for some mathematical computations?
        # If we complete all these tasks, we will be rewarded with a flag!
        connection.sendline(processResponse(response))

def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
    except IndexError:
        print "Usage: ./client.py [IP] [Port]"
        sys.exit(1)
    pwn(address, port)

if __name__ == "__main__":
    main()

