handle = open("users_db","r")
data = handle.readlines()
datum = []
for d in data:
    datum.append(d.strip())
d = "".join(datum)
c = d.decode("hex").strip()
import base64
e = base64.b64decode(c)
print e
