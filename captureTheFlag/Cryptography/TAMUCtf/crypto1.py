import base64
"""
original data: "El Psy Congroo"
encrypted data: "IFhiPhZNYi0KWiUcCls="
encrypted flag: "I3gDKVh1Lh4EVyMDBFo="

The flag is not in the traditional gigem{flag} format.
"""

data = base64.b64decode("IFhiPhZNYi0KWiUcCls=")
flag = base64.b64decode("I3gDKVh1Lh4EVyMDBFo=")
original = "El Psy Congroo"

print data
print flag
print original

key = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(original,data))
flag = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(key,flag))

print key
print flag



