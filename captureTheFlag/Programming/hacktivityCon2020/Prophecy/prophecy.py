import sys, time
try:
    from pwn import *
except ImportError:
    print("In order to complete this challenge, please install pwntools")
    print("https://pwntools.readthedocs.io/en/stable/install.html")
    sys.exit(1)

prophecy = []

def talk(address, port, key):
    while 1:
        try:
           connection = remote(address, port)
        except:
            time.sleep(10)
            continue
        new_props = prophecy[:]
        print(new_props)
        while 1:
            try:
                response = connection.recvuntil(key)
            except:
                #connection.interactive()
                response = connection.recv()
            if b"flag" in response:
                print(response)
                sys.exit()
            response = response.split(b"\n")[-3]
            #print(response)
            if b"?" in response and new_props:
                curr = new_props.pop(0)
                if curr:
                    connection.sendline(curr)
            elif b"F A I L U R E" in response:
                d = response.split(b" ")
                prophecy.append(d[-1])
                connection.close()
                break
            else:
                connection.sendline("12345")

def main():
    try:
        address = "jh2i.com"
        port = 50012
        output_key_to_read_until = ">"
    except:
        print("Usage: ./client.py [IP] [Port] [Key]")
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()
