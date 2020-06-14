message = 'kwfv tsuc lzak dafw wpsuldq. uzsjsulwj 6 gx lzw xdsy ak "g"'
message = 'coxn lkmu drsc vsxo ohkmdvi. xy pvkq robo, tecd psvvob.\n'
message = b'eqzp nmow ftue xuzq qjmofxk. za rxms tqdq, vgef ruxxqd.\n'
message = 'amvl jiks bpqa tqvm mfikbtg. vw ntio pmzm, rcab nqttmz.'
message = str(message)
cipherText = list(message)
print(cipherText)
for i in range(0, 26):
    plainText = ""
    for j in range(len(cipherText)):
        if not cipherText[j].isalpha():
           plainText += cipherText[j]
           continue
        caesar_plain = ord(cipherText[j])+i
        if caesar_plain > 122:
            caesar_plain = caesar_plain - 122
            while (caesar_plain - 122) > 122:
               caesar_plain = caesar_plain - 122
            caesar_plain = 96 + caesar_plain
        plainText += chr(caesar_plain)
    if "flag" in plainText:
      print(plainText)
print("None")


