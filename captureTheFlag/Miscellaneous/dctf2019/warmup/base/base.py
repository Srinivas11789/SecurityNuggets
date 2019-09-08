# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

import sys
import re
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    data = data.strip()
    
    # What is the Input?
  
    # strip the input
    #processed_data = data.split(" ")[5].strip("<<>>")
    space = False
    processed_data = re.search("<<(.*)>>", data).group(1)
   
    # Convert input into a respectable form 
    if " " in processed_data:
        space = True
        new = ""
        processed_data = processed_data.split(" ")
        for i in range(len(processed_data)):
            processed_data[i] = chr(int(processed_data[i], 8))
        processed_data = "".join(processed_data)
        print(processed_data)
        return processed_data
    elif re.findall("^[0-9]+$", processed_data):
        processed_data = int(processed_data)
    elif processed_data.isalnum():
       pass # do not change anything, it can be directly converted into ascii    
    
    print(processed_data)
    
    # Output to be hex, binary, Octal or Ascii
    if "hex" in data:
        processed_data = hex(int(processed_data))
    elif "bin" in data:
        processed_data = bin(int(processed_data))
    elif "oct" in data:
        processed_data = oct(int(processed_data))
    else:
        processed_data = str(processed_data).decode("hex")                               
    
    print(processed_data)
    return processed_data

def talk(address, port, key):
    connection = remote(address, port)
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
           print(connection.recv())
           connection.interactive()
        print response
        connection.sendline(processResponse(response))

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
