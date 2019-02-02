# 
import sys
import urllib2
cipherText = list("jllnunajcxa")
for i in range(0, 26):
    #print "Caesar Shift: " + str(i)
    plainText = ""
    for j in range(len(cipherText)):
        caesar_plain = ord(cipherText[j])+i
        #print caesar_plain, cipherText[j]
        if caesar_plain > 122:
            caesar_plain = caesar_plain - 122
            while (caesar_plain - 122) > 122:
		caesar_plain = caesar_plain - 122
            caesar_plain = 96 + caesar_plain
        plainText += chr(caesar_plain)
    print "Requesting with caesar shift " + str(i) + ", plaintext: " + plainText
    request = urllib2.urlopen("https://challenges.neverlanctf.com:1160/?deciphered="+plainText)
    response = request.read()
    if "flag" in response:
       print response
       sys.exit()
 
