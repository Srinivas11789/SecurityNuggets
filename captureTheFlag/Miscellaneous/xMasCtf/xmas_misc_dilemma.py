import sys
import hashlib

try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponseHash(data):
    # I guess we should do something with this data and send it back!
    # return processed_data
    #data = data.split("\n")
    print data
    data = data.split("=")[1].strip(".")
    i = 0
    print data
    while 1:
        if hashlib.md5(str(i)).hexdigest()[:5] == data:
           print str(i)
           return str(i)
        i += 1
    #return ""

def processResponseMaximum(data):
    print data
    return 1 

def talk(address, port, key):
    connection = remote(address, port)
    try:
      while 1:
        try:
           response = connection.recvline()
        except:
           connection.interactive()
        #print response
        response = response.strip()
        if "digest" in response:
            connection.sendline(processResponseHash(response))
        if "maximum" in response:
           response = response.split("(")
           print response
        if "[2]" in response:
            #response += connection.recvuntil("\n")
            connection.sendline(processResponseMaximum(response))
        #sys.exit()
    except:
        connection.interactive()

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
