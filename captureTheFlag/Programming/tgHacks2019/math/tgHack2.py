# TGHack Programming 2
# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

"""
root@kali:~/Downloads# python tghack2.py  math.tghack.no 10000 "Answer:"
[+] Opening connection to math.tghack.no on port 10000: Done
Level 0/1000
10 + 99
Answer:
Sending... 10 + 99
 Yay!
Level 1/1000
28 / 28
Answer:
Sending... 28 / 28
 Yay!
Level 2/1000
251 * 83
Answer:
Sending... 251 * 83
 Yay!
Level 3/1000
27 * 255
Answer:
Sending... 27 * 255
 Yay!
Level 4/1000
236 - 244
Answer:
Sending... 236 - 244
 Yay!
Level 5/1000
213 / 1
Answer:
Sending... 213 / 1
 Yay!
Level 6/1000
52 - 179
Answer:
Sending... 52 - 179
 Yay!
Level 7/1000
27 - 208
Answer:
Sending... 27 - 208
 Yay!
Level 8/1000
18 - 162
Answer:
Sending... 18 - 162
 Yay!
Level 9/1000
108 * 230
Answer:
Sending... 108 * 230
 Yay!
Level 10/1000
54 * 214
Answer:
Sending... 54 * 214
 Yay!
Level 11/1000
249 + 88
Answer:
Sending... 249 + 88
 Yay!
Level 12/1000
100 * 158
Answer:
Sending... 100 * 158
 Yay!
Level 13/1000
44 - 154
Answer:
Sending... 44 - 154
 Yay!
Level 14/1000
65 / 5
Answer:
Sending... 65 / 5
 Yay!
Level 15/1000

...
...
...
...

Answer:
Sending... 98 - 100
 Yay!
Level 988/1000
128 * 87
Answer:
Sending... 128 * 87
 Yay!
Level 989/1000
90 / 15
Answer:
Sending... 90 / 15
 Yay!
Level 990/1000
107 * 16
Answer:
Sending... 107 * 16
 Yay!
Level 991/1000
249 + 233
Answer:
Sending... 249 + 233
 Yay!
Level 992/1000
204 * 79
Answer:
Sending... 204 * 79
 Yay!
Level 993/1000
231 - 191
Answer:
Sending... 231 - 191
 Yay!
Level 994/1000
92 * 158
Answer:
Sending... 92 * 158
 Yay!
Level 995/1000
60 / 5
Answer:
Sending... 60 / 5
 Yay!
Level 996/1000
144 / 1
Answer:
Sending... 144 / 1
 Yay!
Level 997/1000
218 - 89
Answer:
Sending... 218 - 89
 Yay!
Level 998/1000
200 / 25
Answer:
Sending... 200 / 25
 Yay!
Level 999/1000
55 / 55
Answer:
Sending... 55 / 55
[*] Switching to interactive mode
 Yay!
TG19{calculate_all_the_things}
[*] Got EOF while reading in interactive

"""

import sys
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    # return processed_data
    data = data.split("\n")
    answer = data[-2].strip()
    print "Sending... " + answer
    return str(eval(answer))

def talk(address, port, key):
    connection = remote(address, port)
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
           connection.interactive()
        print response# "Sending.. "+ str(response)
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
