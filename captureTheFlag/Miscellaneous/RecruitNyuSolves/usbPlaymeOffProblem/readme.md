# Interesting Forensics Problem

## USB Packet Capture

## USB URB
* USB Request Block is the data exhcanged between USB Devices and OS.
* The messages have an interrupt being called and leftover capture data is the data sent over by the device

## Solution
* Could be keyboard or mouse movements.
* Extract co-ords and plot them

### Helpers:
* https://www.rootusers.com/google-ctf-2016-forensic-for2-write-up/
* https://medium.com/@forwardsecrecy/hackmethod-july-2017-challenges-write-up-1303f414c8d6

### Commands
* tshark -r playemoff.pcapng -T fields -e usb.capdata > playmeoutput.txt
* https://github.com/ctfs/write-ups-2015/tree/master/boston-key-party-2015/school-bus/riverside
