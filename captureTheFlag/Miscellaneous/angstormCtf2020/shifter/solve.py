# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

import sys
try:
    from pwn import *
except ImportError:
    print("In order to complete this challenge, please install pwntools")
    print("https://pwntools.readthedocs.io/en/stable/install.html")
    sys.exit(1)

# Global Memo to Speed up Fibonacci calculation
memo = [0, 1]

def fibonacci_of_n(n):
    global memo
    if n < len(memo):
        return memo[n]
    else:
        memo.append(fibonacci_of_n(n-1) + fibonacci_of_n(n-2))
        return memo[-1]

def caesar_shift(text, shift):
    text = text.decode()
    if shift > 26:
        shift = shift%26
    caesar_text = []
    #print(text, shift)
    for char in text:
        shft = ord(char) + shift
        if shft > 90: # greater than Z, then rotate
            shft = 64 + (shft-90)
        caesar_text.append(chr(shft))
        #print(caesar_text)
    return "".join(caesar_text)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    data = data.strip(b":")
    data = data.split(b"\n") # Big response split by lines
    #print(data)
    data = data[0].strip() # Get the last line with the shift key string
    #print(data)
    data = data.split(b" ")  # Split by spaces to get all the values separated
    #print(data)
    plain_text = data[1]
    #print(plain_text)
    n = data[-1].split(b"=")[-1]
    #print(n)
    fibn = fibonacci_of_n(int(n))
    print(plain_text, fibn)
    cipher = caesar_shift(plain_text, fibn)
    print(cipher)
    return cipher

def talk(address, port, key):
    connection = remote(address, port)
    response = connection.recvuntil(b"-\n")
    print(response)
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
           connection.interactive()
        print(response)
        connection.sendline(processResponse(response))

def main():
    try:
        address = "misc.2020.chall.actf.co"
        port = 20300
        output_key_to_read_until = "\n"
    except:
        print("Usage: ./client.py")
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()