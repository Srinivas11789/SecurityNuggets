## Input
hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

## Output
answer = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

# Code

import base64

# Learning - Always operate on bytes and not on encoded form of data
bytes = hex.decode('hex')

if base64.b64encode(bytes) == answer:
	print "CryptoPals - Challenge 1 - Set 1 - YES!!"
else:
	print "CryptoPals - Challenge 1 - Set 1 - NO!!"
