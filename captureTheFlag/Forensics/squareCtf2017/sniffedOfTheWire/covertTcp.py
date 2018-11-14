from scapy.all import *
import base64

packets = rdpcap("sniffed-off-the-wire.pcap")
output = open('result', 'w')
out = ""
res = [[""]*10000]*10000
max = 0
ans = ""
final = ""

for packet in packets:
    if packet['TCP'].flags == "PA":
       #print packet.summary()
       #print str(packet)
       stub = str(packet['Raw'])
       #ans += str(packet['Raw'])
       s = stub.split(";")
       t = s[0].split("[")
       q = s[-1].split("H")
       print s, t, q
       if q[-1] == "":
           q[-1] = "H"
       #print t[-1],s[-1]
       res[int(t[-1])][int(q[0])] += q[-1]
       #output.write(str(packet['Raw']))
       if int(t[-1]) > max:
          max = int(t[-1])

for r in res[:max+1]:
    print r,

#print final


"""
final = ""
#print ans

for r in res[:max]:
    #print r
    arr = [""]*len(r)
    for ele in r:
        i = ele.split("H")
        if i[1] == "":
            i[1] = "H"
        arr[int(i[0])] += i[1]
    print arr
    print "-------------------------\n"
    #output.write("".join(arr))
    final += "".join(arr)
"""
#print res[4]
#print out
#print base64.b64decode(out)
#print res
#final = "".join(res[:max+1])
#print base64.b64decode(final)
#final = final.encode("hex")

#output.write(final)
output.close()
       
