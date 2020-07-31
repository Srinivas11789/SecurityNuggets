content = open("caesarmirror.txt", "r").readlines()
reverse = open("rev_caesar.txt", "w")
for c in content:
    c = c.strip()
    data = c.split("   ")
    data[1] = data[1][::-1]
    reverse.write("   ".join(data))
reverse.close()
