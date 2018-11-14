# Output samples:

# Python to manually extract stream after stream decompress
# Perform qdf to decode the flatdecode from the pdf
# qpdf --qdf --object-streams=disable file.pdf x.pdf
file = open("file.pdf","r")
content = file.read()
stream = content.split("stream")
s = stream[1]
s = s.split("end")[0]
s = s.strip()
file = open("ans1.7z","w")
file.write(s)
file.close()

# Python zlib decompress
import re
import zlib

pdf = open("omg.pdf", "rb").read()
stream = re.compile(r'.*?FlateDecode.*?stream(.*?)endstream', re.S)

for s in stream.findall(pdf):
    s = s.strip('\r\n')
    try:
        print(zlib.decompress(s))
        print("")
    except Exception as e:
        print s
        print e

# Whitespace hack

root@d940a5c2a61e:/# stegsnow -C ans/omg-3.pdf 
inctf{w3lcom3_t0_7h3_w0rld_0f_whit3sp4c3}root@d940a5c2a61e:/#

# Learnings from other writeups

* PKTeam https://ctftime.org/writeup/11541
  - peepdf => to get the rawstream or move through the objects 
  - peepdf rawobject 1 gives a number of whitespaces
  - snow.exe -C omg.pdf

* TeamRocketlist https://teamrocketist.github.io/2018/10/09/Forensics-InCTF-2018-Winter-Sport/
  - binwalk -e file.pdf to get the embedded 7z
  - using sublime to see white space and use stegsnow further
