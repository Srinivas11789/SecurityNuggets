# TGHack Programming 4
# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

"""
root@kali:~/Downloads# python tghack4.py hash.tghack.no 2001 
[+] Opening connection to hash.tghack.no on port 2001: Done
Your task is to hash a bunch of spells using different hash functions
hexlify the hash before sending it back!
Good luck!
Hash me using MD5, please: Finite Incantatem
Answer:
Sending... dba36028df0047688d7b2c78c2adcda2 MD5
 Hash me using MD5, please: Erecto
Answer:
Sending... 9ca04bbd8d430a6b0c735b8306b11a36 MD5
 Hash me using SHA512, please: Incarcerous
Answer:
Sending... fa8ec4e7e3922016ca870e5f4a0a87f61d40a90a284b83e5b4f157724f88c191560cda4f12044e46540700b4c71d0394e87e948a7baa14036c3a787a986a4f6e SHA512
 Hash me using MD5, please: Obscuro
Answer:
Sending... 93bd68a002fdda6b325edba945495668 MD5
 Hash me using MD5, please: Avada Kedavra
Answer:
Sending... 872d0765118a77e5b1066ed88ed8212a MD5
 Hash me using SHA256, please: Oppugno
Answer:
Sending... b2e27b7983c2082b5431564189af3d22505c74da0c1d57cfa99da1e9795985be SHA256
 Hash me using SHA512, please: Anapneo
Answer:
Sending... 58b55d881b2ed767a84cb918477af0dd0b3de9bfe8d74587185d797e689cd10674658e5be87093a93f0358f664726050e614e7d3a2393a653233d970a4d04f15 SHA512
 Hash me using SHA512, please: Stupefy
Answer:
Sending... ca821f5340d0a34a28a6253dfd5dac5d0792f04df7976248ff1718345cb43f1c160ced74d13abdb4f40db22b9facec43d8a0526279e94e76b3ea513e94e3da1e SHA512
 Hash me using SHA256, please: Confundo
Answer:
Sending... 5d3135883cdfc0445686921efea00151d15bc9de901a97b6e4029fc7b6fbc7f1 SHA256
 Hash me using SHA256, please: Deprimo
Answer:
Sending... 407b07533630e3c526acdf551cfc53d436cf5e4219e3a2ad0649f66cc2d615e1 SHA256
 Hash me using SHA512, please: Aguamenti
Answer:
Sending... 0bc8a004e56b9db2f188986508db1064965447d175756dad2d6635d3746cf430134f2a7fa9ae9894af26330dab87260b3eec3177aa00c001b7d6c282e4bde41f SHA512
 Hash me using SHA512, please: Confundo
Answer:
Sending... 001298c7a462487308a38795d11c0f2f3b6ddddb7cee71b3b699db0c711dd32a3838aa7c6a4f99d1d189bb22d97a3940a9920dc0f6431956e206fda1788f7bfd SHA512
 Hash me using SHA512, please: Flipendo
Answer:
Sending... 2d777375744172d6706c354adb7e01674c14d8c29faa20abcbe44c06dc83aafcf397d67ab55edf9f1b002e99635b58f544c05bdf622c89ac59159f7b2291fe6e SHA512
 Hash me using MD5, please: Finite Incantatem
Answer:
Sending... dba36028df0047688d7b2c78c2adcda2 MD5
 Hash me using MD5, please: Confringo
Answer:
Sending... 22f813399ffe3a5ffe4cc014a318486a MD5
 Hash me using SHA256, please: Locomotor
Answer:
Sending... cb547694753f5c5547f59698ea7be1e3b1100d7a636d96ab1246c3544d672e43 SHA256
 Hash me using SHA256, please: Deprimo
Answer:
Sending... 407b07533630e3c526acdf551cfc53d436cf5e4219e3a2ad0649f66cc2d615e1 SHA256
...
...
...
...
Sending... bd595efe8adf45464cc075c3e2416d646d2356e1de6254165e27a2881899b068 SHA256
 Hash me using SHA512, please: Stupefy
Answer:
Sending... ca821f5340d0a34a28a6253dfd5dac5d0792f04df7976248ff1718345cb43f1c160ced74d13abdb4f40db22b9facec43d8a0526279e94e76b3ea513e94e3da1e SHA512
 Hash me using MD5, please: Aguamenti
Answer:
Sending... 00d8e812ae9277db5e3d90fc66b67f8e MD5
 Hash me using MD5, please: Mobiliarbus
Answer:
Sending... 95206cf5f28c5c475a64e51f25bf1d9b MD5
 Hash me using SHA512, please: Wingardium Leviosa
Answer:
Sending... 9e3d03197e48172be26710283dba9d7f27a8cc387f09dd8912b7dea3e7244973df9661086815bb1a9d21f69bc9c4743573fdd63a9f98d50ebfa6a45cc187ea98 SHA512
 Hash me using MD5, please: Stupefy
Answer:
Sending... ed4a1d1a7019c1a8045e7c3f09eac5c9 MD5
 Hash me using MD5, please: Wingardium Leviosa
Answer:
Sending... 7dc6d4550f8421416d55eeceb1e46d2a MD5
[*] Switching to interactive mode
 Congrats! Here's the flag: TG19{one_order_of_sha256_hashbrowns_please}
[*] Got EOF while reading in interactive
$  
"""

import sys
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    # return processed_data
    data = data.split("\n")
    answer = data[-2].strip().split(",")
    hash_algo = answer[0].split(" ")[-1] 
    word = answer[1].strip()
    word = " ".join(word.split(" ")[1:])
    import hashlib
    result = ""
    if hash_algo.lower() == "md5":
        result += hashlib.md5(word).hexdigest()
    elif hash_algo.lower() == "sha256":
        result += hashlib.sha256(word).hexdigest()
    elif hash_algo.lower() == "sha512":
        result += hashlib.sha512(word).hexdigest()
    elif hash_algo.lower() == "sha1":
        result += hashlib.sha1(word).hexdigest()
    elif hash_algo.lower() == "sha224":
        result += hashlib.sha224(word).hexdigest()
    elif hash_algo.lower() == "sha384":
        result += hashlib.sha384(word).hexdigest()
    else:
        print hash_algo
    print "Sending... " + result + " " + hash_algo
    return result

def talk(address, port, key):
    connection = remote(address, port)
    while 1:
        try:
           response = connection.recvuntil(key)
        except:
           connection.interactive()
        print response
        connection.sendline(processResponse(response))

def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
        output_key_to_read_until = "Answer:"
    except:
        print "Usage: ./client.py [IP] [Port] [Key]"
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()
