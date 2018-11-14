# Set 1 - Fixed EXOR

def fixedXor(str1, str2):
    result = ""
    for ch1, ch2 in zip(str1,str2): 
        result += chr(ord(ch1)^ord(ch2))
    return result.encode("hex")

##### Learning - 
# * operate on bytes
# * xor the ord of the characters and re-append them back to the string

 
# Input hex encoded
input = "1c0111001f010100061a024b53535009181c"
input = input.decode("hex")

# other string which is already decoded
input2 = "686974207468652062756c6c277320657965"
input2 = input2.decode("hex")

output = "746865206b696420646f6e277420706c6179"
if  output == fixedXor(input, input2):
    print "Cryptopals - Set1 - YES!!"
else:
    print "Cryptopaks - Set1 - NO!!"

