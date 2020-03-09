Srinivass-MacBook-Pro:observeClosely darkknight$ file Griffith_Observatory.png 
Griffith_Observatory.png: PNG image data, 320 x 155, 8-bit/color RGBA, non-interlaced
Srinivass-MacBook-Pro:observeClosely darkknight$ exiftool Griffith_Observatory.png 
ExifTool Version Number         : 10.55
File Name                       : Griffith_Observatory.png
Directory                       : .
File Size                       : 127 kB
File Modification Date/Time     : 2020:03:06 18:37:45-08:00
File Access Date/Time           : 2020:03:06 18:40:02-08:00
File Inode Change Date/Time     : 2020:03:06 18:40:01-08:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 320
Image Height                    : 155
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 320x155
Megapixels                      : 0.050
Srinivass-MacBook-Pro:observeClosely darkknight$ binwalk -e Griffith_Observatory.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 320 x 155, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, default compression
127759        0x1F30F         Zip archive data, at least v2.0 to extract, compressed size: 2587, uncompressed size: 16664, name: hidden_binary
130500        0x1FDC4         End of Zip archive, footer length: 22

Srinivass-MacBook-Pro:observeClosely darkknight$ strings _Griffith_Observatory.png-0.extracted/hidden_binary | egrep -i "utflag{\w+"
utflag{2H
