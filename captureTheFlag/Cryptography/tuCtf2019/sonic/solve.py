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
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)
from nltk.corpus import words
word_list = words.words()

def processResponse(data):
    # I guess we should do something with this data and send it back!
    # Caesar shift decoding
    global word_list
    #print(word_list)
    #encoded = data.split(" ")[-1]
    encoded = data.strip()
    for i in range(1, 27):
      shift = i
      decoded = ""
      for c in encoded:
        target = ord(c)+shift
        while target > ord("Z"):
          target -= ord("Z")
          target = ord("A")+target-1
        decoded += chr(target)
      print(decoded, shift)
      if decoded.lower() in word_list:
        print("Sending... " + decoded)
        return decoded
    print("Sending... " + "no match!")
    return "noMatch"

def talk(address, port, key):
    connection = remote(address, port)
    # Handle first response differently
    #response = connection.recvuntil("Hey")
    #print("Header is " + response)
    response = ""
    while 1:
        try:
           #response = connection.recvuntil(key)
           response = connection.recv()
        except:
           connection.interactive()
        print(response)
        response = response.split(" ")
        print(response)
        connection.sendline(processResponse(response[-1]))

def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
        output_key_to_read_until = sys.argv[3]
    except:
        print "Usage: ./client.py [IP] [Port] [Key]"
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()
