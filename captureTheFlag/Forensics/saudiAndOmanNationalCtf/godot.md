# Godot Challenge

### Level: Easy

## Given
* A image (png) 
* Specific question: an hacker has left some info in the png that helps us to track him.

## Thinking...
* Used pnginfo, exifinfo, exif, imginfo, cat image, bin walk (got carried away with the lib file initially)
* Most of the information reveal about a png tailer
* Visually you can see a base64 type string at the end too
* Decoding base64 we get a hex.
  * Try all the tracking possibilities —> latitude + longitude or ip ? 
* Then... after some break --> rethinking this to be an easy problem
* Tried Base32 decode and the Flag was revealed

## Steps
* Visually in a vi editor the tailer of the image is visible else any image info tool would have revealed about a tailer
* Looking at the magic number number for trailer of png images you can separate the data from the png image.

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/saudiAndOmanNationalCtf/asset01.png" title="hexed">

## Flag
* FLAG{Not_Only_Base64}
<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/saudiAndOmanNationalCtf/asset02.png" title="hexed">

## Console

# Proper calc steps
```bash
root@kali:~/Downloads/godot# file godot.png 
godot.png: PNG image data, 64 x 64, 8-bit/color RGBA, non-interlaced

root@kali:~/Downloads/godot# pngcheck godot.png 
godot.png  additional data after IEND chunk
ERROR: godot.png

root@kali:~/Downloads/godot# exiftool godot.png 
ExifTool Version Number         : 11.16
File Name                       : godot.png
Directory                       : .
File Size                       : 3.5 kB
File Modification Date/Time     : 2019:02:09 01:41:06-08:00
File Access Date/Time           : 2019:02:09 01:41:17-08:00
File Inode Change Date/Time     : 2019:02:09 01:41:06-08:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 64
Image Height                    : 64
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Warning                         : [minor] Trailer data after PNG IEND chunk
Image Size                      : 64x64
Megapixels                      : 0.004
```

# Results:
```bash
root@kali:~/Downloads/godot# python
>>> import base64
>>> base64.b64decode("91841df795d78f59587I820VVd4T=")
'\xf7_8\xd5\xd7\xfb\xf7\x97{\xf1\xfe}\xe7\xce\xc8\xf3m\x15U\xde\x13'

root@kali:~/Downloads/godot# base32 -d godot.txt
FLAG{Not_Only_Base64
```

# Overthinking...
```bash
root@kali:~/Downloads/godot# steghide extract -sf godot.png 

root@kali:~/Downloads/godot# binwalk godot.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 64 x 64, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, default compression

root@kali:~/Downloads/godot# img_stat godot.png 
IMAGE FILE INFORMATION
--------------------------------------------
Image Type: raw

Size in bytes: 3539
Sector size:	512

>>> import zlib
>>> h = open("29.zlib","r")
>>> data = h.read()
>>> zlib.decompress(data)
```
