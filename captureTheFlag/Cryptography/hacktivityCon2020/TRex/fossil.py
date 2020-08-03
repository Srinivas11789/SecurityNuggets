#!/usr/bin/env python

import base64
import binascii

h = binascii.hexlify
b = base64.b64encode

c = b'37151032694744553d12220a0f584315517477520e2b3c226b5b1e150f5549120e5540230202360f0d20220a376c0067'

def enc(f):
    e = b(f)
    z = []
    i = 0
    while i < len(e):
        z += [ e[i] ^ e[((i + 1) % len(e))]]
        i = i + 1
    c = h(bytearray(z))
    return c

def dec(c):
    c = binascii.unhexlify(c)
    c = list(c)
    print(c)
    # Reverse Xor c = a^b --> a = c^b
    # i+1 % len will always be i+1 except when i+1 == len
    n = len(c)
    flag = []
    base64OfPrefix = "ZmxhZ3" # base64 of flag{ known plaintext
    plusOne = c[0]
    while n:
        current = c.pop()
        print(current, flag)
        flag.append(current ^ plusOne)
        plusOne = flag[-1]
        n -= 1
    p = ""
    for f in flag:
        p += chr(f)
    print(p)
    return base64.b64decode(p)
print(dec(c))