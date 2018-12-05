# Count the boxes with box names having 2 repeating and 3 repeating letters
# * multiply them to obtain the checksum 

# Fetch input from url
import requests, sys
# Sent the cookie set through the environment variable to get this
input = requests.get("https://adventofcode.com/2018/day/2/input")

# Hard Coded inputs
input = open("21.input","r").read()
input = input.split("\n")

# Logic
"""
>>> a = {"s", "r", "i"}
>>> b = {"s", "r", "n"}
>>> a.difference(b)
set(['i'])
""" 

result  = []
# Do worst case brute force to crack this soon
for i in range(len(input)):
    for j in range(i+1, len(input)):
        one = set(input[i])
        two = set(input[j])
        #inter1 = len(one.intersection(two))
        #inter2 = len(two.intersection(one))
        #if (inter1 == len(input[i])-1) and (inter2 == len(input[j])-1):
        if len(one.difference(two)) == 1 and len(two.difference(one)) == 1:
           index = input[i].index(one.difference(two).pop())
           index2 = input[j].index(two.difference(one).pop())
           if index == index2:
              result.append(input[i][:index]+input[i][index+1:])
print set(result)
           
