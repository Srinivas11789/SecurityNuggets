filename = "playmeoutput.txt"
handle = file(filename,"r")
content = handle.readlines()
out = []
for line in content:
	out.append("".join(line.strip().split(":")))
print "".join(out)
