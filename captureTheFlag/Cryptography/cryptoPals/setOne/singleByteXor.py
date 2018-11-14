# Single Byte Xor Challenge

# Cipher text - encrypted
cipherText = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

# To hold all possible plaintext or decrypted text for the different possible single byte keys
strings = []

# Iterating over each of the possible single byte key, which is 0 - 256
for i in range(256): 
    # Result or decrypted text of the current key
    result = ""

    # iterating over each byte data to xor with the key for decryption
    #for ch in bytes.fromhex(cipherText).decode('utf-8'): # Python3
    for ch in cipherText.decode("hex"): # Python2 
        result += chr(i^ord(ch))

    # Store all the result in the memory
    strings.append(result)

# Findin the possible plain text match - using dictionary method/ frequency analysis or counting spaces

# Logic 1: Counting spaces logic... why? research about this
#print max(strings, key=lambda s: s.count(' '))    

# python3 logic --->  Is printable to check if we have printable characters - prints a lot of matches - wrong logic
#for string in strings:
#    if string.isprintable():
#       print(string)

# Frequency analysis or dictionary prediction






