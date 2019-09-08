import itertools
import base64

def string_xor(s, key):
    key = key * (len(s) / len(key) + 1)
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in itertools.izip(s, key)) 

flag = "''"
key = "''"

print base64.b64encode(string_xor(flag, key))

# dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ==

flag = "dHNkdktUAFMBA1MIBglWBgkFCFEGBQlUCQRRBAgIBgQAVVRUAwkEBFEAAVRVVVRTBFRWBQdUBlMAB1YJVQYIBwIIBFVSTQ=="

# Reversing the above

decode_64 = base64.b64decode(flag)

print(decode_64)

# String XOR function
# * matches key to the plaintext data ( rotates keys accordingly )
# * xors each character

# Defeat it by
# * Predicting the key rotation and detect length of key
# * 
