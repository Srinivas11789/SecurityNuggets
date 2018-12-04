# Calculate the End Frequency Changes from the Freq changes list
# * Start from 0
# * Condition: When first repeating freq result occurs, start from beginning

# Fetch input from url
import requests, sys
# Sent the cookie set through the environment variable to get this
input = requests.get("https://adventofcode.com/2018/day/1/input")

# Hard Coded inputs
input = open("1.input","r").read()
input = input.split("\n")

print input

# freqs list to track the frequency
exp = "0"
freqs = []
while exp:
  for i in input:
    if i:
       print str(exp),i,eval(str(exp)+i)
       exp = eval(str(exp)+i)
       if exp in freqs:
          print exp
          sys.exit()
       else:
          freqs.append(exp)
  #sys.exit()

