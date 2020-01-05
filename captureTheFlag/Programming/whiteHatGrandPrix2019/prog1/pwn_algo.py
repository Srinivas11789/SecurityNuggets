# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

# Question
"""
srimbp-623:whiteHatGrandPrix2019 sri$ nc 15.164.75.32 1999

PROGRAMING - WHITEHAT GRANDPRIX 06:

--> COUNT THE NUMBER OF POSSIBLE TRIANGLES <--

HOW MANY TRIANGLES ARE CREATED BY N (1..N) NUMBER. N < 10^6

Example:  N = 5
OUTPUT : 3 

(2,3,4),(3,4,5),(2,4,5)
................/\...................|\...................
.............../  \..................| \..................
............../    \.................|  \.................
............./      \................|   \................
............/        \...............|    \...............
.........../          \..............|     \..............
........../____________\.............|______\.............
	
n = 33
Answer: 
No No! Be a good person !
"""

import sys
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

# harcoded memo 
#memo = {3333: 3081329475, 99999: 83327083474999, 11111: 114262122645, 33333: 3085910516975}
memo = {}

def valid_triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b > c and b+c > a and c+a > b:
        #print(a,b,c)
        return True
    else:
        return False

def processResponse(data):
    # I guess we should do something with this data and send it back!
    data = data.split("\n")
    n = data[-2].split("=")[-1].strip()
    print("N is " + n)
    triangles = 0
    n = int(n)+1
    if n-1 in memo:
        return str(memo[n-1])
    """
    # Brute1 - Naive 3 loop logic - does not work, takes long time
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if valid_triangle([i,j,k]):
                    triangles += 1
    """
    """
    # Brute2 - Itertools - does not work, takes long time
    import itertools
    for comb in itertools.combinations(range(n), r=3):
        if valid_triangle(comb):
            triangles += 1
    """
    """
    # Referring to google/leetcode for a better algorithm - Long time again!
    for i in range(1, n-2):
        for j in range(i+1, n):
            k = j+1
            while k < n and (i+j)>k:
                k += 1
            triangles += k - j - 1
    """
    # 2 pointer technique for the third element
    if n-1 > 20000:
        return ""
    for i in range(1, n):
        for j in range(i+1, n):
            l = j+1
            r = n-1
            while l < n and r < n and l <= r:
                mid = (l+r)//2
                if mid < i+j:
                    triangles += mid - l + 1
                    l = mid + 1
                else:
                    r = mid - 1
    if n-1 not in memo:
        memo[n-1] = triangles     
    print("Sending..." + str(triangles))
    return str(triangles)

def talk(address, port, key):
    while 1:
      connection = remote(address, port)
      while 1:
        try:
            response = connection.recvuntil(key)
        except:
            #connection.interactive()
            continue
        print response
        ans = processResponse(response)
        try:
            if connection:
                connection.sendline(ans)
            else:
                print("Close connection and trying again...")
                break
        except:
            print("Close connection and trying again...")
            break
      connection.close()

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
