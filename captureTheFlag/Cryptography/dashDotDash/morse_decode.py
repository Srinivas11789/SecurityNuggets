import sys
morse_decode_dict = {
        "di-dah": "A",
        "dah-di-di-dit": "B",
        "dah-di-dah-dit": "C",
        "dah-di-dit": "D",
        "dit": "E",
        "di-di-dah-dit": "F",
        "dah-dah-dit": "G",
        "di-di-di-dit": "H",
        "di-dit": "I",
        "di-dah-dah-dah": "J",
        "dah-di-dah": "K",
        "di-dah-di-dit": "L",
        "dah-dah": "M",
        "dah-dit": "N",
        "dah-dah-dah": "O",
        "di-dah-dah-dit": "P",
        "dah-dah-di-dah": "Q",
        "di-dah-dit": "R",
        "di-di-dit": "S",
        "dah": "T",
        "di-di-dah": "U",
        "di-di-di-dah": "V",
        "di-dah-dah": "W",
        "dah-di-di-dah": "X",
        "dah-do-dah-dah": "Y",
        "dah-dah-di-dit": "Z",
        "dah-dah-dah-dah-dah": "0",
        "di-dah-dah-dah-dah": "1",
        "di-di-dah-dah-dah": "2",
        "di-di-di-dah-dah": "3",
        "di-di-di-di-dah": "4",
        "di-di-di-di-dit": "5",
        "dah-di-di-di-dit": "6",
        "dah-dah-di-di-dit": "7",
        "dah-dah-dah-di-dit": "8",
        "dah-dah-dah-dah-dit": "9"
        }

flag_morse = open("flag.txt", "r")
flag_morse_content = flag_morse.read().strip().split(" ")
result = ""
for word in flag_morse_content:
    if word in morse_decode_dict:
        result += morse_decode_dict[word]
    else:
        print word, morse_decode_dict
print result
print "\n"
print result[2:].decode("hex")

