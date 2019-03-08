from scapy.all import *
capture_read = rdpcap("out.pcapng")
for packet in capture_read:
    if ICMP in packet:
        data = str(packet[Raw]).encode("hex")
        print data[-16:].decode("hex")

