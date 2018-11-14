from scapy.all import *
import base64

packets = rdpcap("sniffed-off-the-wire.pcap")
output = open('result', 'w')
out = ""
res = [[""] * 10000] * 10000
max = 0
ans = ""
for packet in packets:
    if packet['TCP'].flags == "PA":
        # print packet.summary()
        # print str(packet)
        stub = str(packet['Raw'])
        # ans += str(packet['Raw'])
        s = stub.split(";")
        t = s[0].split("[")
        q = s[-1].split("H")
        if q[-1] == "":
            q[-1] = "H"
        # print t[-1],s[-1]
        res[int(t[-1])][int(q[0])] += q[-1]
        # output.write(str(packet['Raw']))
        if int(t[-1]) > max:
            max = int(t[-1])

output.write(final)
output.close()

