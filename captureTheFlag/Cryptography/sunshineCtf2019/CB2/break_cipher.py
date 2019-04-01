ciphertext = "dbdalphaalphabeddddcdealphacalphadbbddalphaddealphabbb".upper()
key = "clarinet".upper()

while len(key) < len(ciphertext):
      key = key + "clarinet".upper()
key = key[:len(ciphertext)]

print "Cipher is " + ciphertext
print "Key is " + key

print "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(ciphertext, key)])
