import sys

if sys.argc != 3:
    print "Enter the ciphertext, knowntext to crack using caeser cipher!"
    print "python caeser.py <known_possible> <ciphertext>"
    sys.exit(0)

# Arguments
known = sys.argv[1]
ciphertext = sys.argv[2]

# Find the proper delta



# Crack the string 
for ch in str:
     if ord(ch) >= 97 and ord(ch) <= 122:
             s = ord(ch) - 13
             if s < 97:
                     s = 13 - (ord(ch)-97)
                     str1 += chr(123 - s)
             else:
                     str1 += chr(s)
     else:
             str1 += ch

print str1
