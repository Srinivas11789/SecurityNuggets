import sys
cipherText3 = "MKXU IDKMI DM BDASKMI NLU XCPJNDICFQ! K VDMGUC KW PDT GKG NLKB HP LFMG DC TBUG PDTC CUBDTCXUB. K'Q BTCU MDV PDT VFMN F WAFI BD LUCU KN KB WAFI GDKMINLKBHPLFMGKBQDCUWTMNLFMFMDMAKMUNDDA"
cipherText2 = cipherText3.split(" ")
cipherText = list("".join(cipherText2).lower())
print cipherText
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
 
