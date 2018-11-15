import json
names = []
yaku = {}

# File 1: Fetch all the existence of the names of the Captain
for i in range(1,2):
    name = str(i)+".csv"
    file = open(name,"r")
    for line in file.readlines():
        if "Yakubovics" in line.strip() or "Yakubovics".upper() in line.strip() or "Yakubovics".lower() in line.strip():
           l = line.strip().split(",")
           yaku["email"] = l[0]
           yaku["role"] = l[1]
           yaku["income"] = l[2]
    file.close()


# File 2
for i in range(2,3):
    name = str(i)+".csv"
    file = open(name,"r")
    for line in file.readlines():
        if "Yakubovics" in line.strip() or "Yakubovics".upper() in line.strip() or "Yakubovics".lower() in line.strip():
           l = line.strip().split(",")
           yaku["state"] = l[1]
    file.close()

# doc has the ssn, address --> Fetch all florida addresses and ssn
name = str(3)+".csv"
file = open(name,"r")
for line in file.readlines():
    if "Florida" in line.strip() or "Florida".lower() in line.strip() or "Florida".upper() in line.strip():
       l = line.strip().split(",")
       # ssn
       yaku[l[2]] = {}
       # street
       yaku[l[2]]["ssn"] = l[0]
file.close()

# Fourth
name = str(4)+".csv"
file = open(name,"r")
for line in file.readlines():
    l = line.strip().split(",")
    if " ".join(l[2:-1]) in yaku and ("Florida" in l[1] or "Florida".upper() in l[1] or "Florida".lower() in l[1]):
       yaku[" ".join(l[2:-1])]["income"] = l[0]
       yaku[" ".join(l[2:-1])]["postal"] = l[-1]
file.close()

# Fifth
name = str(5)+".csv"
file = open(name,"r")
for line in file.readlines():
    l = line.strip().split(",")
    if " ".join(l[1:]) in yaku:
       yaku[" ".join(l[1:])]["name"] = l[0]
       # This assumption doesnt work?
       if l[0][0] != "e".upper() and l[0][0] != "e".lower():
          del yaku[" ".join(l[1:])]
file.close()

print json.dumps(yaku, sort_keys=True, indent=4)


"""
# This logic is not used
# Fourth File
#name = str(3)+".csv"

# Fifth file - First Name and Street
#print names
#print places
 

#for i in range(1,6):
#    name = str(i)+".csv"
#    file = open(name,"r")
#    for line in file.readlines():
#        for s in result:
#           if s in line.strip():
#              result.extend(line.strip().split(" "))
#    file.close()
#print result
"""
print "Done!"
