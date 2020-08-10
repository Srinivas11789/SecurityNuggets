#!/usr/bin/python
import random, os, requests, socket, time

def make_random_key(key_length):
    key = ''
    for index in range(key_length):
	magicnumber = random.randint(0, 94)
	key = key + chr(int(126)-magicnumber)
    return key

def encrypt_file(the_key):
    input_file = open('secret.pdf', 'rb')
    output_file = open('App.sec', 'wb')
    key_index = 0
    for byte in input_file.read():
        encrypted_byte = chr(ord(the_key[key_index]) ^ ord(byte))
        output_file.write(encrypted_byte)
        key_index = key_index + 1
        if key_index >= len(the_key):
            key_index = 0
    output_file.close()
    input_file.close()

def test_enc(the_key):
    input_file = open('secret.pdf', 'rb')
    output_file = open('AppTest.sec', 'wb')
    key_index = 0
    for byte in input_file.read():
        encrypted_byte = chr(ord(the_key[key_index]) ^ ord(byte))
        output_file.write(encrypted_byte)
        key_index = key_index + 1
        if key_index >= len(the_key):
            key_index = 0
    output_file.close()
    input_file.close()


def transmit_key(key):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 31337))
    s.sendto('{|3361|\|}', ('1.3.3.7', 31337))
    for ch in key:
        delay = ord(ch)*0.1
        print delay
	time.sleep(delay)
        s.sendto(' A P P 5 3 C ', ('1.3.3.7', 31337))
    s.sendto('|TRANSMITTED VIA SAFE-MODE', ('1.3.3.7', 31337))

def decrypt_file(enc, the_key):
    flag = open("flag.pdf", "wb")
    key_index = 0
    l = 0
    for byte in enc.read():
        #print(byte, the_key[key_index])
        dec_byte = chr(ord(byte) ^ ord(the_key[key_index]))
        #print(dec_byte)
        flag.write(dec_byte)
        key_index = key_index + 1
        #if l > 5:
        #    break
        l += 1
        if key_index >= len(the_key):
            key_index = 0
    enc.close()
    flag.close()

password = make_random_key(10)
print("Test Random password is")
print str(password)

# FINDING RANDOM KEY --> KEY LENGTH 10
detect_key = ""
delays = [6.106013324, 8.004647840, 12.012643363, 11.502981443, 12.112982136, 11.713276829, 6.507175955, 8.609829538, 5.706807207, 3.304042612]
for i in range(10):
   import math
   detect_key += chr(int(delays[i]*10))
print(detect_key)

#encrypt_file(password)
encrypted = open("App.sec", "rb")
#transmit_key(password)
decrypt_file(encrypted, detect_key)

# test_enc(" A P P 5 3 C ")
#encrypted = open("AppTest.sec", "rb")
#decrypt_file(encrypted, " A P P 5 3 C ")
