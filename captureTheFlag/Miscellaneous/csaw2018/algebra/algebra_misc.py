#!/usr/bin/env python
import sys
from sympy import *
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    d = data.split("\n")
    print d
    check = 0
    if len(d[-2]) > 20:
      operation = d[-2].split("=")
      check = 1
    if check == 0:
      try:
        operation = d[-2].split(" ")
      except:
        operation = d[-1].split(" ")          
      try:
       operand = int(operation[0])
       front = 1
      except:
       operand = int(operation[2])
       front = 0
      ans = 0
      if operation[1] == "+":
         ans = int(operation[4]) - operand
      if operation[1] == "*":
         ans = int(operation[4]) / float(operand)
         if ans.is_integer():
            ans = str(ans).split(".")[0]
      if operation[1] == "-":
         if front == 1:
         	ans = -(int(operation[4]) - operand)
         else:
                ans = int(operation[4]) + operand
      if operation[1] == "/":
         if front == 0:
            	ans = int(operation[4]) * operand
         else:
                ans = operand / float(int(operation[4]))
                if ans.is_integer():
            		ans = str(ans).split(".")[0]  
    else:
       operand = operation[0]+"-"+"("+operation[1].strip()+")"
       ans = solve(operand, "X")[0]
    print str(operation) + " ==> " +  str(ans)
    return str(ans)

def pwn(address, port):
    connection = remote(address, port)
    for i in range(200):
        try:
           response = connection.recvuntil(":")
        except:
           connection.interactive()
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

