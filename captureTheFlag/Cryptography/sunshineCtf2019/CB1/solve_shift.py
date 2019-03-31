ciphertext = "hkcgxkznkojkyulsgxin"
ciphertext = ciphertext.upper()
for char in ciphertext:
     limit = ord("A")
     limit2 = ord("Z")+1
     shift = ord(char)-6
     if shift < limit:
        shift = limit-shift
        print chr(limit2-shift),
     else:
        print chr(shift),
