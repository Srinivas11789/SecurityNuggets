# Solve

**Steps**

* Look at comments on the PNG using exiftool
```
srimbp:takeItToTheCleaners sri$ exiftool ritsec_logo2.png 
ExifTool Version Number         : 11.30
File Name                       : ritsec_logo2.png
Directory                       : .
File Size                       : 4.3 kB
File Modification Date/Time     : 2019:11:15 17:08:10-08:00
File Access Date/Time           : 2019:11:15 17:09:48-08:00
File Inode Change Date/Time     : 2019:11:15 17:08:10-08:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 328
Image Height                    : 154
Bit Depth                       : 8
Color Type                      : Palette
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Palette                         : (Binary data 129 bytes, use -b option to extract)
Exif Byte Order                 : Big-endian (Motorola, MM)
Image Description               : Hi there! Looks like youre trying to solve the forensic_fails challenge! Good luck!
Resolution Unit                 : inches
Artist                          : Impos73r
Y Cb Cr Positioning             : Centered
Copyright                       : RITSEC 2018
Exif Version                    : 0231
Components Configuration        : Y, Cb, Cr, -
User Comment                    : RVZHRlJQe1NCRVJBRlZQRl9TTlZZRl9KQkFHX1VSWUNfTEJIX1VSRVJ9
Flashpix Version                : 0100
GPS Latitude Ref                : North
GPS Longitude Ref               : West
Image Size                      : 328x154
Megapixels                      : 0.051
```

* Comment looks like a base64 encoded string
```
srimbp:takeItToTheCleaners sri$ python -c 'import base64; print(base64.b64decode("RVZHRlJQe1NCRVJBRlZQRl9TTlZZRl9KQkFHX1VSWUNfTEJIX1VSRVJ9"))'
EVGFRP{SBERAFVPF_SNVYF_JBAG_URYC_LBH_URER}
```

* Obviously Caesar Shift Cipher - ROT13
```
RITSEC{FORENSICS_FAILS_WONT_HELP_YOU_HERE}
```

* Things that did not work!
```
srimbp:takeItToTheCleaners sri$ binwalk ritsec_logo2.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 328 x 154, 8-bit colormap, non-interlaced
182           0xB6            Zlib compressed data, default compression
4063          0xFDF           Zlib compressed data, default compression

srimbp:takeItToTheCleaners sri$ strings ritsec_logo2.png 
```
