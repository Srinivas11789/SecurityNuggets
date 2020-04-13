### Challenge

```
One of our agents on the ship recovered this file from a usb-stick found in the pockets of a space bandit. It appears that the space bandits are fans of an antique series of video games. We suspect there might be a flag hidden here. Have a look?
```

### Recon
* Looking at https://www.dcode.fr/tools-list#symbols
* Particularly the symbol substitution cipher
* Iterating through them one by one to check for similarities
* The `Unown Pokemon Alphabet` cipher --> name looks similar to the filename
* Looking at the image confirms the pattern

### Solve
* Decode the unown pokemon cipher
```
REMEMBER TO EXAMINE THE
```

* This does not look like the complete flag. Something more should be dug out.

* Dig more with the file for any forensics. Png data shows extra trailer data is present
```
kali@kali.org$ file downloadunowns.png 
downloadunowns.png: PNG image data, 7200 x 300, 8-bit colormap, non-interlaced
kali@kali.org$ exiftool downloadunowns.png 
ExifTool Version Number         : 10.55
File Name                       : downloadunowns.png
Directory                       : .
File Size                       : 750 kB
File Modification Date/Time     : 2020:04:10 22:02:08-07:00
File Access Date/Time           : 2020:04:10 22:02:15-07:00
File Inode Change Date/Time     : 2020:04:10 22:02:13-07:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 7200
Image Height                    : 300
Bit Depth                       : 8
Color Type                      : Palette
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Gamma                           : 2.2
White Point X                   : 0.3127
White Point Y                   : 0.329
Red X                           : 0.64
Red Y                           : 0.33
Green X                         : 0.3
Green Y                         : 0.6
Blue X                          : 0.15
Blue Y                          : 0.06
Palette                         : (Binary data 363 bytes, use -b option to extract)
Transparency                    : (Binary data 17 bytes, use -b option to extract)
Background Color                : 1
Modify Date                     : 2020:03:05 13:08:26
Datecreate                      : 2020-03-02T14:12:38+00:00
Datemodify                      : 2020-03-02T05:04:08+00:00
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 7200x300
Megapixels                      : 2.2

kali@kali.org$ cat downloadunowns.png
PNG
...
...
...
END
...
sls lqvwdoo vwhjr-ove <3
```

* Looks like shifting crypto --> maybe caesar shift cipher! Bruteforce shift...
  - ROT + 3
```
+3	pip install stego-lsb <3
```

* Trying stegolsb on the image did not retrieve anything. Tried lsbsteg and zsteg

* Binwalk gave more interesting things
```
kali@kali.org$ binwalk --dd='.*' downloadunowns.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 7200 x 300, 8-bit colormap, non-interlaced
565           0x235           Zlib compressed data, best compression
82203         0x1411B         PNG image, 1050 x 520, 8-bit/color RGB, non-interlaced
82322         0x14192         Zlib compressed data, best compression
759448        0xB9698         TIFF image data, big-endian, offset of first image directory: 8
760158        0xB995E         PNG image, 51 x 80, 8-bit/color RGB, non-interlaced
```

* One of the images has `PIKALANG text` in the image. `1411B`
* Decoding the PIKALANG --> BrainFuck --> English text
* Refer `https://github.com/groteworld/pikalang`
```
>>> s
['pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pika', 'pipi', 'pi', 'pipi', 'pi', 'pi', 'pi', 'pipi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pipi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pichu', 'pichu', 'pichu', 'pichu', 'ka', 'chu', 'pipi', 'pipi', 'pipi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'pipi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'pi', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pichu', 'pichu', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pipi', 'pipi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pi', 'pi', 'pi', 'pikachu', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'pichu', 'pichu', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pipi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'pipi', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pi', 'pikachu', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'pichu', 'pichu', 'pikachu', 'pipi', 'pipi', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'pichu', 'pichu', 'pikachu', 'pipi', 'pipi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'ka', 'ka', 'ka', 'pikachu', 'ka', 'pikchu', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu', 'pichu', 'pichu', 'pikachu', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pi', 'pikachu', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'ka', 'pikachu']

>>> 
>>> ans = ""
>>> for t in s:
...   if t == "pi":
...     ans += "+"
...   elif t == "ka":
...     ans += "-"
...   elif t == "pika":
...     ans += "["
...   elif t == "chu":
...     ans += "]"
...   elif t == "pipi":
...     ans += ">"
...   elif t == "pichu":
...     ans += "<"
...   elif t == "pikapi":
...     ans += ","
...   else:
...     ans += "."
... 
>>> ans
'++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++.>+++++++++++.+.-----------.<<++++++++++++++.------------.>>++++++++++++++.----.+++..---------.----.++++++++++++++.<<++++++++++++++.--------------.>++++++.>-----------.+.++++++++++.<<.>>----------.++++++++++.<<.>>++++.-----.---.-.-------.<<.++++++++++++++++++++++++++.---------------------.'
>>> 
```

* The decoded output is `Nope, sorries. This is wrong :%`. Uhh!!
* Another image `B995E` has hidden LSB as per the trailer, I Hope!
  * Lets try `ZSTEG`

```bash
kali@kali.org$:_downloadunowns.png.extracted darkknight$ zsteg -a B995E.png 
[?] 25 bytes of extra data after image end (IEND), offset = 0x2080
extradata:0         .. text: "sls lqvwdoo vwhjr-ove <3\n"
b2,g,msb,xy         .. text: "}7;@h__UU"
b2,rgb,lsb,xy       .. text: "pwd is 58growliness\n"
b2,rgb,msb,xy       .. text: "VUUUUUUUUUUU"
b2,bgr,msb,xy       .. text: "VUUUUUUUUUUU"
b4,r,msb,xy         .. text: "w7UUywwwwwww"
b4,g,msb,xy         .. text: "Uywwwwwww"
b4,b,msb,xy         .. text: "Uywwwwwww"
b4,rgb,msb,xy       .. text: "ywwwwwwwwwwwwwwwwwwwwwww"
b4,bgr,msb,xy       .. text: "ywwwwwwwwwwwwwwwwwwwwwww"
b8,g,msb,xy         .. text: "??????___"
b4,g,msb,xy,prime   .. text: "g,tR@xMn`_"
b4,rgb,msb,xy,prime .. text: "3WUwwwwww"
b4,bgr,msb,xy,prime .. text: ";7SUwwwwww"
b1,bgr,lsb,yx       .. <wbStego size=192, ext="\x00\x00\x00", data="\x00\x00\x00\xE0\x00\x00b\xA9\x8B\x85"..., even=false>
b2,r,msb,yx         .. file: GEM GDOS font UUVU3????<u?zu? 21845, ID 0x5554
b2,g,msb,yx         .. file: GEM GDOS font UUVUҍ??ڳԿ?? 21845, ID 0x5556
b2,b,msb,yx         .. file: GEM GDOS font UUVU1˞?j??? 21845, ID 0x5556
b2,rgb,msb,yx       .. file: GEM GDOS font UUUUUUUUUUUUUUjUUUUU3u?-?)r[? 21845, ID 0x5568
b2,bgr,msb,yx       .. file: GEM GDOS font UUUUUUUUUUUUUUjUUUUU9p3??F???G? 21845, ID 0x554a
b4,r,msb,yx         .. text: "swwwwwwwwwww{www=?u"
b4,g,msb,yx         .. text: "{wwwwwwwwwww{www;"
b4,b,msb,yx         .. text: "{wwwwwwwwwww{www5/"
b4,rgb,msb,yx       .. text: "{wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
b4,bgr,msb,yx       .. text: "swwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
b8,rgb,msb,yx       .. text: "%%%%%%???"
b8,bgr,msb,yx       .. text: "%%%%%%???"
b1,b,msb,yx,prime   .. file: hp200 (68010) BSD
b2,r,lsb,yx,prime   .. file: SoftQuad DESC or font file binary
b2,r,msb,yx,prime   .. file: VISX image file
b2,g,lsb,yx,prime   .. file: SoftQuad DESC or font file binary - version 4523
b2,g,msb,yx,prime   .. file: VISX image file
b2,b,lsb,yx,prime   .. file: SoftQuad DESC or font file binary
b2,b,msb,yx,prime   .. file: VISX image file
b2,rgb,lsb,yx,prime .. file: 5View capture file
b2,rgb,msb,yx,prime .. file: VISX image file
b2,bgr,lsb,yx,prime .. file: 5View capture file
b2,bgr,msb,yx,prime .. file: VISX image file
b4,r,msb,yx,prime   .. text: "E(ww_6Hw"
b4,rgb,msb,yx,prime .. text: ["w" repeated 17 times]
b4,bgr,msb,yx,prime .. text: ["w" repeated 16 times]
b5,rgb,lsb,yx,prime .. text: "uy:ok[)K"
b5,bgr,lsb,yx,prime .. text: "e}>nk[)K"
b8,r,msb,yx,prime   .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,g,msb,yx,prime   .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,b,msb,yx,prime   .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,rgb,msb,yx,prime .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b8,bgr,msb,yx,prime .. file: RDI Acoustic Doppler Current Profiler (ADCP)
b3,bgr,msb,XY       .. text: "hG]WSd*i"
b4,b,lsb,XY         .. text: "s<#yaqkr[!"
b8,rgb,msb,XY       .. text: "kkkGGG777Gg"
b8,bgr,msb,XY       .. text: "kkkGGG777"
b4,g,lsb,XY,prime   .. text: "u!(>U[EoOq"
b4,bgr,msb,XY,prime .. text: "n:Iwg]t{"
b8,b,lsb,XY,prime   .. text: "{u:4<HR="
b8,rgb,msb,XY,prime .. file: 777 archive data
b8,bgr,msb,XY,prime .. file: 777 archive data
b1,bgr,msb,YX       .. text: "J{t/!1wBl"
b2,rgb,msb,YX       .. text: "PUjUUUUUUUUUUU"
b2,bgr,msb,YX       .. text: "PUjUUUUUUUUUUUO"
b4,r,msb,YX         .. text: "u{wwwwwww"
b4,g,msb,YX         .. text: "u{wwwwwww"
b4,b,msb,YX         .. text: "u{wwwwwwwo"
b4,rgb,msb,YX       .. text: "{wwwwwwwwwwwwwwwwwwwwww"
b4,bgr,msb,YX       .. text: "{wwwwwwwwwwwwwwwwwwwwww"
b8,rgb,msb,YX       .. text: "???______"
b8,bgr,msb,YX       .. text: "???______"
b1,bgr,lsb,YX,prime .. <wbStego size=252, ext="\x18\xFB\x9F", data="\xF7\xE1\xF8\x00Zm\x7F\x8E8\x01"..., even=false>
b4,rgb,lsb,YX,prime .. file: MPEG ADTS, AAC, v4 Main, 44.1 kHz, surround + LFE
b4,rgb,msb,YX,prime .. text: "qwwwwwwww7"
b4,bgr,lsb,YX,prime .. file: MPEG ADTS, AAC, v4 Main, 44.1 kHz, surround + LFE
b4,bgr,msb,YX,prime .. text: "qwwwwwwww"
b8,b,lsb,YX,prime   .. text: "+P<>oWeNDO"
b2,b,lsb,Xy         .. text: "{voct8$F"
b2,rgb,msb,Xy       .. text: "_UUUUUUUUUUUU"
b2,bgr,lsb,Xy       .. text: "h3sVnZNw~cvK"
b2,bgr,msb,Xy       .. text: "_UUUUUUUUUUUU"
b4,r,msb,Xy         .. text: ["w" repeated 8 times]
b4,g,msb,Xy         .. text: ["w" repeated 8 times]
b4,b,msb,Xy         .. text: ["w" repeated 8 times]
b4,rgb,msb,Xy       .. text: "[UUUU33s;"
b4,bgr,msb,Xy       .. text: "SUUUU3s3?"
b8,r,msb,Xy         .. text: "???___??"
b8,g,msb,Xy         .. text: "___??????"
b8,rgb,msb,Xy       .. text: "_________?????"
b8,bgr,msb,Xy       .. text: "?_________???"
b4,r,lsb,Xy,prime   .. file: PARIX executable
b4,g,msb,Xy,prime   .. file: PGP Secret Key -
b4,rgb,lsb,Xy,prime .. file: SoftQuad DESC or font file binary
b4,rgb,msb,Xy,prime .. file: VISX image file
b4,bgr,msb,Xy,prime .. text: "ww7w\nw<'"
b7,g,lsb,Xy,prime   .. file: AIX core file fulldump 32-bit, 
b8,b,lsb,Xy,prime   .. text: "\\L>OQ:6y"
b8,rgb,lsb,Xy,prime .. file: MIT scheme (library?)
b1,rgb,lsb,yX       .. text: "lBw1!/t{J"
b2,rgb,msb,yX       .. text: ["U" repeated 11 times]
b2,bgr,msb,yX       .. text: "?UUUUUUUUUUU"
b4,r,msb,yX         .. text: "?wwwwwww"
b4,g,msb,yX         .. text: "1eqwwwwwww"
b4,rgb,msb,yX       .. text: ["w" repeated 22 times]
b4,bgr,msb,yX       .. text: "?wwwwwwwwwwwwwwwwwwwwww"
b8,rgb,msb,yX       .. text: "______???"
b8,bgr,msb,yX       .. text: "______???"
b8,rgb,msb,yX,prime .. text: "___kkk???"
b8,bgr,msb,yX,prime .. text: "___kkk???_"
b4,b,lsb,xY         .. text: "+R{aqis,3y"
b4,bgr,msb,xY       .. text: "F3CDf&\"U"
b5,g,lsb,xY         .. text: "N|FS%[R4"
b6,b,msb,xY         .. text: "4\r\tsW^\t3l"
b8,rgb,msb,xY       .. text: "###sss+++["
b8,bgr,msb,xY       .. text: "###sss+++"
b2,rgb,lsb,xY,prime .. file: mc68k COFF executable not stripped
b2,bgr,lsb,xY,prime .. file: mc68k COFF executable
b8,bgr,msb,xY,prime .. text: "###+++gW"
b2,rgb,msb,Yx       .. text: ["U" repeated 17 times]
b2,bgr,msb,Yx       .. text: "UUUUUUUUUUUUUUUUU)@"
b4,r,msb,Yx         .. text: "wwwwwwwwwww7RQ:R"
b4,g,msb,Yx         .. text: ["w" repeated 11 times]
b4,b,msb,Yx         .. text: ["w" repeated 11 times]
b4,rgb,msb,Yx       .. text: "[wwwwwwwwww"
b4,bgr,msb,Yx       .. text: ["w" repeated 10 times]
b4,rgb,lsb,Yx,prime .. file: MPEG ADTS, layer III, v2,  16 kbps, 22.05 kHz, JntStereo
b4,rgb,msb,Yx,prime .. text: "uwwwwwwww7"
b4,bgr,lsb,Yx,prime .. file: MPEG ADTS, layer III, v2,  16 kbps, 22.05 kHz, JntStereo
b4,bgr,msb,Yx,prime .. text: "}wwwwwwww"
```

* This sounds `pwd is 58growliness` resonable.

* Still flag does not work!

* Relooking for one last time over the existing images we obtained 2 new ones. Especially the ones which failed us last time with the pika text!

```
kali@kali.org$:_downloadunowns.png.extracted darkknight$ exiftool 1411B.png 
ExifTool Version Number         : 10.55
File Name                       : 1411B.png
Directory                       : .
File Size                       : 670 kB
File Modification Date/Time     : 2020:04:11 01:22:30-07:00
File Access Date/Time           : 2020:04:11 09:37:26-07:00
File Inode Change Date/Time     : 2020:04:11 09:37:26-07:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1050
Image Height                    : 520
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Gamma                           : 2.2
White Point X                   : 0.3127
White Point Y                   : 0.329
Red X                           : 0.64
Red Y                           : 0.33
Green X                         : 0.3
Green Y                         : 0.6
Blue X                          : 0.15
Blue Y                          : 0.06
Background Color                : 255 255 255
Datecreate                      : 2020-03-03T09:16:46+00:00
Datemodify                      : 2020-03-03T09:16:46+00:00
Warning                         : [minor] eXIf chunk should be exIf
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 72
Y Resolution                    : 72
Resolution Unit                 : inches
Y Cb Cr Positioning             : Centered
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
User Comment                    : UEsDBBQACQAIAKZcfVBDHT+yawAAAA0DAAAPABwAaGlkZGVuX3Bpa2EudHh0VVQJAANoiIBeaIiA.XnV4CwABBAAAAAAEAAAAAN3lNuROgH+YPpAXM7WLWrA+e0XFFuOqQusLwjhYH/1+YYE06DlWKp+A.ZbSezbVPGmbO2n/CL1coFGeKS9EV4RWfAvw4SwkNcDtH2BjBS5ESvEKfztOv+FmKUNDFvgkO/VXS.R/W0USAgz62PUEsHCEMdP7JrAAAADQMAAFBLAQIeAxQACQAIAKZcfVBDHT+yawAAAA0DAAAPABgA.AAAAAAEAAACkgQAAAABoaWRkZW5fcGlrYS50eHRVVAUAA2iIgF51eAsAAQQAAAAABAAAAABQSwUG.AAAAAAEAAQBVAAAAxAAAAAAAYUhSMGNITTZMeTlpZFd4aVlYQmxaR2xoTG1KMWJHSmhaMkZ5WkdW.dUxtNWxkQzkzYVd0cEwxWjFiSEJwZUY5Y0tGQnZheVZETXlWQgpPVzF2Ymx3cENnPT0K
Flashpix Version                : 0100
Color Space                     : Uncalibrated
Image Size                      : 1050x520
Megapixels                      : 0.546
```

* The base64 encoded comment looks interesting. Removing the dots and decoding --> ZIP file
```
kali@kali.org$:_downloadunowns.png.extracted darkknight$ echo "UEsDBBQACQAIAKZcfVBDHT+yawAAAA0DAAAPABwAaGlkZGVuX3Bpa2EudHh0VVQJAANoiIBeaIiAXnV4CwABBAAAAAAEAAAAAN3lNuROgH+YPpAXM7WLWrA+e0XFFuOqQusLwjhYH/1+YYE06DlWKp+AZbSezbVPGmbO2n/CL1coFGeKS9EV4RWfAvw4SwkNcDtH2BjBS5ESvEKfztOv+FmKUNDFvgkO/VXSR/W0USAgz62PUEsHCEMdP7JrAAAADQMAAFBLAQIeAxQACQAIAKZcfVBDHT+yawAAAA0DAAAPABgAAAAAAAEAAACkgQAAAABoaWRkZW5fcGlrYS50eHRVVAUAA2iIgF51eAsAAQQAAAAABAAAAABQSwUGAAAAAAEAAQBVAAAAxAAAAAAAYUhSMGNITTZMeTlpZFd4aVlYQmxaR2xoTG1KMWJHSmhaMkZ5WkdWdUxtNWxkQzkzYVd0cEwxWjFiSEJwZUY5Y0tGQnZheVZETXlWQgpPVzF2Ymx3cENnPT0K" | base64 -d > new_file
kali@kali.org$:_downloadunowns.png.extracted darkknight$ file new_file 
new_file: Zip archive data, at least v2.0 to extract
```

* Zip was password protected and using the password already obtained. Another pika text which completes the original form

kali@kali.org$:_downloadunowns.png.extracted darkknight$ unzip new_file 
Archive:  new_file
[new_file] hidden_pika.txt password: 
  inflating: hidden_pika.txt         
kali@kali.org$:_downloadunowns.png.extracted darkknight$ cat hidden_pika.txt 
pi pi pi pi pi pi pi pi pi pi pika pipi pi pipi pi pi pi pipi pi pi pi pi pi pi pi pipi pi pi pi pi pi pi pi pi pi pi pichu pichu pichu pichu ka chu pipi pipi pipi pipi pi pi pikachu pi pi pi pi pi pi pi pi pi pikachu pikachu pichu pichu pi pi pikachu pipi pipi ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu ka pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu pichu pichu pikachu pipi pipi ka ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pi pi pikachu ka ka ka ka ka ka ka ka pikachu pichu pichu pikachu pipi pipi ka ka ka ka pikachu pi pi pi pi pi pi pi pi pi pikachu pi pi pi pikachu pi pi pi pi pikachu ka ka ka ka ka ka ka ka ka ka ka ka ka ka pikachu pi pi pi pi pi pi pi pikachu pi pi pi pi pi pi pi pi pi pi pi pi pi pikachu

kali@kali.org$:_downloadunowns.png.extracted darkknight$
```

* Decodes to `foo bar dog closely`

* Flag: 
```
REMEMBER TO EXAMINE THE FOO BAR DOG CLOSELY
```

--> CTF was over! could not submit the answers!