name = "hexdump"
result = open("extract.zip", "w")
content = ""
for i in range(1,4):
    f = open(name+str(i)+".txt", "r")
    content += f.read()
    content = content.strip()
print content
result.write(content.decode("hex"))
