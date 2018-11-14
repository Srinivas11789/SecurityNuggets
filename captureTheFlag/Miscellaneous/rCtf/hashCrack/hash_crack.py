import hashlib,random
import sys, itertools, socket
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    sys.exit(1)

#
# sha256(****+qGyQcgR1pPT637Ls) == 36aff7c0201fe6633cdb7bdb471fc51350ac1dd86fff4d83d6d3e38c3d59e3fe
#

# Takes forever - try for only alphabets only - try lower characters alone - did not work 
# Tried for all the lowercase, highercase, and special characters - takes long time but worked - 33,123
# Seems the pattern of the string contains only lowercase and uppercase characters, try reducing the string pattern to those range - 65,123

def hashGen(s, h):
    # BruteForce
    for i in range(48,123):
	for j in range(48,123):
		for k in range(48,123):
			for l in range(48,123):
				curr = chr(i)+chr(j)+chr(k)+chr(l)
                                curr_str = curr+s
				#print curr_str
				if hashlib.sha256(curr_str).hexdigest() == h:
 					print curr_str
					return curr_str


def hashGen2(s, h, comb):
     for c in comb:
	if hashlib.sha256(c+s).hexdigest() == h:
		print c
		return c

# pwnlib to track the netcat function
def attack(address, port):
    possibilities = [chr(i) for i in range(48,58)]
    possibilities.extend([chr(j) for j in range(65,91)])
    possibilities.extend([chr(k) for k in range(97,123)])
    #print possibilities
    combination = ["".join(i) for i in itertools.product(possibilities, repeat=4)]
    try:
          connection = remote(address, port)
          #while 1:
          response = connection.recv()
          print response
          res_string = response.split("\n")[0].split("==")
          h = res_string[1].strip(" ")
          s = res_string[0][12:-2]
 	  print h,s  
    	  connection.sendline(hashGen2(s,h,combination))
          response = connection.recv()
          #print response
          #print "=============>"
          res_string = response.split("\n")[-1]
          print res_string
          """
          for i in range(6):
          	connection.sendline(random.randint(0,10))
                response = connection.recv()
                print response
          response = connection.recv()
          print response
          """  
    except:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.connect(address, port)
      data = s.recv(1024)
      print data


# Driver Function
def main():
	s = "qGyQcgR1pPT637Ls"
        h = "36aff7c0201fe6633cdb7bdb471fc51350ac1dd86fff4d83d6d3e38c3d59e3fe"
	print hashGen(s,h)

#main()
attack("149.28.139.172","10002")
