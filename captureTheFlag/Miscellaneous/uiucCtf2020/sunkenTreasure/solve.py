# Command Line Execution of uber/h3
# eg: h3ToGeoBoundary --index 8a5d064eb9affff

from matplotlib import pyplot as plt
import subprocess as s
import json

fileLog = open("log", "r")
content = fileLog.readlines()
#print(content)


fileAns = open("coords", "w")

locations = []
for l in content:
  l = l.strip()
  output = s.check_output(["h3ToGeoBoundary", "--index", l])
  output = output.split("\n")
  for o in output:
    if " " in o:
      print(o.strip().split(" "))
      fileAns.write(str(o.strip().split(" ")))
      locations.append(o.strip().split(" "))
plt.figure(
    figsize=(100, 50),
    dpi=300)
x, y = zip(*locations)
plt.scatter(y, x)
#plt.tight_layout()
#plt.savefig("out.png")
plt.savefig("ans.jpg")
plt.show()
