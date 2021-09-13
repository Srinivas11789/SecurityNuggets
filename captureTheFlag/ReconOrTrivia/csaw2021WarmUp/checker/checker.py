def up(x):
    x = [f"{ord(x[i]) << 1:08b}" for i in range(len(x))]
    return ''.join(x)

def down(x):
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    return x

def right(x,d):
    x = x[d:] + x[0:d]
    return x

def left(x,d):
    x = right(x,len(x)-d)
    return x[::-1]

def encode(plain):
    d = 24
    x = up(plain)
    x = right(x,d)
    x = down(x)
    x = left(x,d)
    return x

# Solve
"""
% python3 checker.py
What does this mean?
1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100
flag{r3vers!nG_w@rm_Up}
"""
def decode(cipher):
    # reverse te left shift
    cipher = cipher[::-1]
    cipher = right(cipher,24-len(cipher))
    # reverse down which is just a compliement 
    cipher = ''.join(['0' if cipher[i] == '1' else '1' for i in range(len(cipher))])
    # reverse the right shift
    cipher = right(cipher,-24)
    # reverse up
    plain = ""
    for i in range(0,len(cipher),8):
        plain += chr(int(cipher[i:i+8],2)//2)
    return plain

def main():
    flag = "redacted"
    encoded = encode(flag)
    
    print("What does this mean?")
    encoded = "1010000011111000101010101000001010100100110110001111111010001000100000101000111011000100101111011001100011011000101011001100100010011001110110001001000010001100101111001110010011001100"
    print(encoded)

    print(decode(encoded))


if __name__ == "__main__":
  main()
