# single byte xor

import base64

ciphertextencoded = "IConIT0xdSoldit1GTJ2GTIudRkxdigidTQgMyoZMXY0KiIZdiAZJTQ/NjJ2Zzs="

ciphertext = base64.b64decode(ciphertextencoded)

print ciphertext

ans = ""
for i in range(256):
       for char in ciphertext:
 	   ans += chr(ord(char) ^ i)
       if "flag" in ans:
              print ans
              break
       else:
              ans = ""
              continue

		




