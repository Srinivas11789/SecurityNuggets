import sys

try:
    from pwn import *
except ImportError:
    print("In order to complete this challenge, please install pwntools")
    print("https://pwntools.readthedocs.io/en/stable/install.html")
    sys.exit(1)

flag = ["" for i in range(50)]

def processResponse(data):
    data = data.decode("utf-8").strip()
    print("Got..." + data)
    message = caesarDecode(data)
    print("Sending... " + message)
    if "character" in message:
        # send back this line exactly. character 25 of the flag is 'e'
        m = message.split(" ")
        index = int(m[-6])
        flag[index] = m[-1].strip("'")
    #print(flag)
    return message

def caesarDecode(message):
    cipherText = list(message)
    for i in range(0, 26):
        plainText = ""
        for j in range(len(cipherText)):
            if not cipherText[j].isalpha():
                plainText += cipherText[j]
            else:
                caesar_plain = ord(cipherText[j])+i
                if caesar_plain > 122:
                    caesar_plain = caesar_plain - 122
                    while (caesar_plain - 122) > 122:
                        caesar_plain = caesar_plain - 122
                    caesar_plain = 96 + caesar_plain
                plainText += chr(caesar_plain)
        #print(plainText)
        if "flag" in plainText:
            return plainText
    return ""

def talk(address, port, key):
    connection = remote(address, port)
    response = connection.recvuntil(".\n")
    response = response.decode("utf-8")
    print("Got... " + response)
    connection.sendline(response.strip())
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
            print("".join(flag))
            connection.interactive()
        connection.sendline(processResponse(response))

def main():
    try:
        address = "jh2i.com"
        port = "50034"
        output_key_to_read_until = "\n"
    except:
        print("Usage: ./client.py [IP] [Port] [Key]")
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()