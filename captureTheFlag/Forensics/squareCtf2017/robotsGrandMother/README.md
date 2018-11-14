## CTF   : Square CTF 
## Value : 50 pointer
## Name  : Robots GrandMother
## Type  : Forensics

# Brief:
* A pcap file was given with a hint about a secret exchanged in mail

# FunFact:
* An RFC was pointed out about using pigeons to transfer packet data. Nice to know!

# Solve:
* Obviously looking for SMTP packets in the pcap
* An authentication with username and password is very obvious
* Everything request and response are base64 encoded
* Decoding gives the request parameters of username and password





