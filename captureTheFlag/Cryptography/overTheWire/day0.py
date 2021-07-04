day0 = open("day0.input", "r")
data = day0.readlines()
result = ""
for d in data:
    d = d.strip()
    if "/" in d and "\\" in d:
        d = d.split("/")[-1].strip()
        d = d.split("\\")[0].strip()
        d = "".join(d.split(" "))
        result += d.strip()
print result
#print result.decode("hex")
