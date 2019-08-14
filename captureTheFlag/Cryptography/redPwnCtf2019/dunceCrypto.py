# Clearly a classic caesar shift crypto 
cipher = "mshn{P_k0ua_d4ua_a0_w4f_tf_ahe3z}"
# Known plaintext is "flag" in the beginning so -7 
flag = ""
for char in cipher:
    if (ord(char) >= 97 and ord(char) <= 122):
        if ord(char)-7 < 97:
            diff = 7 - (ord(char) - 97)
            flag += chr(123-diff)
        else:
            flag += chr(ord(char)-7)
    elif (ord(char) >= 65 and ord(char) <= 90):
        if ord(char)-7 < 65:
            diff = 7 - (ord(char) - 65)
            flag += chr(91-diff)
        else:
            flag += chr(ord(char)-7)
    else:
        flag += char
print(flag)


