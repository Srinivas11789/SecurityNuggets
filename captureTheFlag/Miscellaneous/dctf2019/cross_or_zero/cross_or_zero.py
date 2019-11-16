import itertools
import base64

def string_xor(s, key):
    #print(s, key)
    if len(key) != 1:
        key = key * int(len(s) / len(key) + 1)
        #print(s, key)
        if len(key) != len(s):
            print("something wrong")
        return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(s, key)) 
    return ""

flag = "''"
key = "''"

#print(base64.b64encode(string_xor(flag, key)))

# dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ==

flag = "dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ=="

# Reversing the above

decode_64 = base64.b64decode(flag)

# Get some word list
from nltk.corpus import words
word_list = words.words()

# Single Byte XOR Crack

for k in range(256):
    plaintext = string_xor(decode_64, chr(k))
    #if set(word_list).intersection(plaintext.split(" ")):
    if "DCTF" in plaintext: 
        print(plaintext)
print(decode_64)

# String XOR function
# * matches key to the plaintext data ( rotates keys accordingly )
# * xors each character

# Defeat it by
# * Predicting the key rotation and detect length of key
# * 
