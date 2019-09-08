# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

import sys
from pwn import *
try:
    from pwn import *
except ImportError:
    print("In order to complete this challenge, please install pwntools")
    print("https://pwntools.readthedocs.io/en/stable/install.html")
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    # return processed_data
    return 100    

def talk(address, port, key):
    connection = remote(address, port)
    response = connection.recvuntil("name?")
    print(response)
    connection.sendline("A")
    response = connection.recvuntil("Ready? Y/N")
    print(response)
    connection.sendline("Y") 
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
           connection.interactive()
        print(response)
        connection.sendline(processResponse(response))

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
