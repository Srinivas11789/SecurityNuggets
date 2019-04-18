# TGHack Programming 1
# Helpers for Capture the flag to breeze through the ground work
# - Updating Ctf helper gists to have a fun ctf and reuse some basic ground work
# - For use in Binary exploitation/ Reverse engineering / Pwning / Remote server Interaction
# - "Usage: ./client.py [IP] [Port] [output_key_to_read_until]"
# - output_key_to_read_until ==> ">" or ":" or "?" or "$"
#

"""
root@kali:~/Downloads# python tghack1.py echo.tghack.no 5555 ""
[+] Opening connection to echo.tghack.no on port 5555: Done
Nox Sending.. Nox
Orchideous Sending.. Orchideous
Legilimens Sending.. Legilimens
Tarantallegra Sending.. Tarantallegra
Lumos Sending.. Lumos
Scourgify Sending.. Scourgify
Stupefy Sending.. Stupefy
Erecto Sending.. Erecto
Protego Totalum Sending.. Protego Totalum
Expecto Patronum Sending.. Expecto Patronum
Aparecium Sending.. Aparecium
Relashio Sending.. Relashio
Aguamenti Sending.. Aguamenti
Impedimenta Sending.. Impedimenta
Incarcerous Sending.. Incarcerous
Rictusempra Sending.. Rictusempra
Deletrius Sending.. Deletrius
Densaugeo Sending.. Densaugeo
Rennervate Sending.. Rennervate
Morsmordre Sending.. Morsmordre
Incendio Sending.. Incendio
Expulso Sending.. Expulso
Glisseo Sending.. Glisseo
Molliare Sending.. Molliare
Alohomora Sending.. Alohomora
Pack Sending.. Pack
Accio Sending.. Accio
Petrificus Totalus Sending.. Petrificus Totalus
Confringo Sending.. Confringo
Levicorpus Sending.. Levicorpus
Fulgari Sending.. Fulgari
Reducio Sending.. Reducio
Crucio Sending.. Crucio
Flagrate Sending.. Flagrate
Repello Muggletum Sending.. Repello Muggletum
Impervius Sending.. Impervius
Tergeo Sending.. Tergeo
Locomotor Sending.. Locomotor
Mobiliarbus Sending.. Mobiliarbus
Portus Sending.. Portus
Homenum Revelio Sending.. Homenum Revelio
Protego Horribilis Sending.. Protego Horribilis
Liberacorpus Sending.. Liberacorpus
Waddiwasi Sending.. Waddiwasi
Evanesco Sending.. Evanesco
Muffliato Sending.. Muffliato
Salvio Hexia Sending.. Salvio Hexia
Piertotum Locomotor Sending.. Piertotum Locomotor
Reparo Sending.. Reparo
Furnunculus Sending.. Furnunculus
Good job! Here's your flag: TG19{behold_the_echo_chamber_of_secrets} Sending.. Good job! Here's your flag: TG19{behold_the_echo_chamber_of_secrets}
[*] Switching to interactive mode
[*] Got EOF while reading in interactive
$ z 
[7]+  Stopped                 python tghack1.py echo.tghack.no 5555 ""
root@kali:~/Downloads# 

"""

import sys
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def processResponse(data):
    # I guess we should do something with this data and send it back!
    # return processed_data
    #print "Sending... " + str(data)
    return data

def talk(address, port, key):
    connection = remote(address, port)
    while 1:
        try:
           response = connection.recvline().strip()
        except:
           connection.interactive()
        print response, "Sending.. "+ str(response)
        connection.sendline(response)

def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
        output_key_to_read_until = sys.argv[3]
    except:
        print "Usage: ./client.py [IP] [Port] [Key]"
        sys.exit(1)
    talk(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()
