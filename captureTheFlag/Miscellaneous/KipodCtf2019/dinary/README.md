# Dinary

# Recon, Hits and Solve

* recon for images
```
srimbp-623:dinary sri$ file dinary.png 
dinary.png: PNG image data, 6907 x 6907, 8-bit/color RGB, 
non-interlaced


srimbp-623:dinary sri$ exiftool dinary.png 
ExifTool Version Number         : 11.30
File Name                       : dinary.png
Directory                       : .
File Size                       : 8.3 MB
File Modification Date/Time     : 2019:12:20 22:24:07-08:00
File Access Date/Time           : 2019:12:23 20:31:42-08:00
File Inode Change Date/Time     : 2019:12:20 22:25:20-08:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 6907
Image Height                    : 6907
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 6907x6907
Megapixels                      : 47.7


srimbp-623:dinary sri$ string
stringdups    stringdups32  strings       
srimbp-623:dinary sri$ strings dinary.png | grep -i KAF{


srimbp-623:dinary sri$ binwalk dinary.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 6907 x 6907, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, best compression

srimbp-623:dinary sri$ 

root@kali:~/Downloads# pnginfo dinary.png 
dinary.png...
  Image Width: 6907 Image Length: 6907
  Bitdepth (Bits/Sample): 8
  Channels (Samples/Pixel): 3
  Pixel depth (Pixel Depth): 24
  Colour Type (Photometric Interpretation): RGB 
  Image filter: Single row per byte filter 
  Interlacing: No interlacing 
  Compression Scheme: Deflate method 8, 32k window
  Resolution: 0, 0 (unit unknown)
  FillOrder: msb-to-lsb
  Byte Order: Network (Big Endian)
  Number of text strings: 0

root@kali:~/Downloads# pngcheck dinary.png 
OK: dinary.png (6907x6907, 24-bit RGB, non-interlaced, 93.9%).
root@kali:~/Downloads# 
```

* Nothing weird in the recon. So this seems to be a good png file. Diving into stegano.

* Next try --> Histogram, Color inversions/modifications, LSB, MSB steg....

* `Historgram` gave nothing.

* `stegsolve, steganabara, steghide` did not help a lot.

* Maybe color palatte stuff????? but before that.

* LSB or MSB steg --> use tool first to get something weird?
  - `zsteg` gave something. the first flag indeed
```
root@kali:~/Downloads# zsteg dinary.png 
b1,r,lsb,xy         .. text: "Hello World!, Yesterday my kipod went free and i can't find him! KAF{wh3r3_1s_my_k1p0d?}\nMaybe YOU can help me find my kipod? (his name is \"Fibon\")\nHope you'll find him, he should go on a tour really soon.\n1nFr>F3jpYQu@.KNMJPGUC*D$DL5Ky(IV:&{z6B#a7+jX0(u&?"
```