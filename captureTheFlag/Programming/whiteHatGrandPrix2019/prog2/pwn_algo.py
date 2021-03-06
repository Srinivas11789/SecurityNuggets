# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

# Question
"""
srimbp-623:whiteHatGrandPrix2019 sri$ nc 15.165.30.141 9399



WHITEHAT 2019 - PROGRAMMING

PASSWORD COUNT


We have found a device which have a classic keyboard like below.

+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| * | 0 | # |
+---+---+---+

This device is protected by a secret password. We don't know what the password is,
but after several hours of reversing we know that the password was generated by
following the rules:
1, The password has length of n, and contains characters as shown on the keyboard.
2, The password must end with either *, 8 or #.
3, After one character, the character which is on the knight move pattern (as the
knight in chess) can be the next character. For example, if the current character
is 3, then the next character can be either 4 or 8.

We really want to know how many passwords can be generated given length n, so that
we can know whether to give up brute-force or not. Ah, because that number may be
very large so you just need to give us the answer modulo 1e39.
Please help us, we will give you our flag in exchange :'>
(n <= 1e16)
n = 10
Answer: Don't try to hack me pls :
"""

import sys, json
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

memo = {"10":"6552", "15": "565482", "13": "95144", "8": "1102", "17": "3361422", "19": "19982920"}
flag = []

def backtrack_for_possible_passwords(curr_pass, move, n, key, possible):
    if len(curr_pass) == n and curr_pass[-1] in set(["8", "*", "#"]):
        #print(curr_pass)
        possible += [curr_pass]
    elif len(curr_pass) > n:
        return
    else:
        for nxt in move:
            backtrack_for_possible_passwords(curr_pass+nxt, key[nxt], n, key, possible)
    return 

def processResponse(data):
    # I guess we should do something with this data and send it back!
    data = data.split("\n")
    if len(data) >= 3 and "reward:" in data[-3]:
        flag.append(data[-3].split(":")[-1])
    n = data[-2].split("=")[-1].strip()
    print("N is " + n)
    if n in memo:
        print("Sending..." + " length is " + n + ":" + memo[n])
        return memo[n]
    possible_passwords = 0
    # Rule 1: To satisfy the knight chess pattern lets create a dictionary
    # * choosing a list of key to select from is better but knight move is not tracked
    keys = { 
        "1": ["6", "8"],
        "2": ["7", "9"],
        "3": ["4", "8"],
        "4": ["3", "9", "0"],
        "5": ["*", "#"],
        "6": ["1", "7", "0"],
        "7": ["2", "6", "#"],
        "8": ["1", "3"],
        "9": ["2", "4", "*"],
        "*": ["5", "9"],
        "0": ["4", "6"],
        "#": ["7", "5"]
    }
    possible_passwords = []
    for start in keys.keys():
        backtrack_for_possible_passwords(start, keys[start], int(10), keys, possible_passwords)
    ans = str(int(len(possible_passwords)%1e39))
    if n not in memo:
        memo[n] = ans 
    print("Sending..." + " length is " + n + ":" + ans)
    open("memo", "w").write(json.dumps(memo))
    return ans

def talk(address, port, key):
      global flag
      while 1:
        flag = []
        connection = remote(address, port)
        while connection:
            try:
                response = connection.recvuntil(key)
            except:
                connection.interactive()
                pass
            print(response)
            if response:
                print("".join(flag))
                try:
                    connection.sendline(processResponse(response))
                    print("Connection alive and Sent!")
                except Exception as e:
                    print(str(e))
                    connection.close()
                    break
        connection.close()
      connection.interactive()

def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
        output_key_to_read_until = sys.argv[3]
    except:
        print "Usage: ./client.py [IP] [Port] [Key]"
        sys.exit(1)
    global memo
    log = open("memo", "r").read()
    memo = json.loads(log)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()
