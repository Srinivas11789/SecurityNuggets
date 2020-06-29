#!/usr/bin/env python3

from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

mod_reverse = {}
for i in range(26):
    mod_reverse[2*i%26] = i 

def encrypt(ptxt, key):
    ptxt = ptxt.lower()
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        ctxt += num_to_chr[(x + y) % 26]
    return ctxt

# As we use the same string as both ptxt and key we just divide
def reverse_key(key):
    key = key.lower()
    key = ''.join(key[i % len(key)] for i in range(len(key))).lower()
    ctxt1 = ''
    ctxt2 = ''
    for i in range(len(key)):
        x = chr_to_num[key[i]]
        #delta = x//2 #(26+x)//2 # v_ghrff_pfehdo_xrlf_nrr_pfrhqb_fepurr
        delta = mod_reverse[x] # i_tuess_csruqb_keys_aee_cseudo_srchee
        ctxt1 += num_to_chr[delta]
        delta = x//2
        ctxt2 += num_to_chr[delta]
        #print(delta, ctxt1, ctxt2)
    return ctxt1, ctxt2

def reverse_cipher(ptxt, key):
    key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
    ctxt = ''
    for i in range(len(ptxt)):
        if ptxt[i] == '_':
            ctxt += '_'
            continue
        x = chr_to_num[ptxt[i]]
        y = chr_to_num[key[i]]
        #print(x, y, x-y, (x-y)%26, num_to_chr[(x-y)%26])
        options = []
        for n in range(26):
            value = ((x-y) + 26*n)
            #print(value)
            if value >= 0 and value < 26:
                options.append(num_to_chr[(x-y) + 26*n])
        #print(options)
        #select = input("Select one? ")
        ctxt += options[0]
        #ctxt += num_to_chr[(x-y) % 26*n]
    return ctxt

"""
with open('flag.txt') as f, open('key.txt') as k:
    flag = f.read()
    key = k.read()

ptxt = flag[5:-1]

ctxt = encrypt(ptxt,key)
"""

key =  "iigesssaemk"
ctxt = "z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut"

pseudo_key = encrypt(key,key)
key1, key2 = reverse_key(key)
reverse_cipher_1 = reverse_cipher(ctxt, key1)
reverse_cipher_2 = reverse_cipher(ctxt, key2)

#print('Ciphertext:',ctxt)
print('Pseudo-key:',pseudo_key)
print("ReversedKey1:", key1)
print("ReversedKey2:", key2)
print("Plain from key1:", reverse_cipher_1)
print("Plain from key2:", reverse_cipher_2)
