import base64, binascii

# Set of data: Basic conept => cleartext XOR key = Encrypted Text
original_data = "El Psy Congroo"
encrypted_data = base64.b64decode("IFhiPhZNYi0KWiUcCls=").decode("hex")
print encrypted_data

# Flag 
encrypted_flag = base64.b64decode("I3gDKVh1Lh4EVyMDBFo=").encode("hex")

# encrypted xor clear = key
key = bin(int(original_data.encode("hex"),16)) ^ bin(int(encrypted_data,16))
print key

# Flag
flag = int(encrypted_flag,16) ^ key
print str(flag)


