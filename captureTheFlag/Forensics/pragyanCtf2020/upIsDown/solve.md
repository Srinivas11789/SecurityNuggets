Srinivass-MacBook-Pro:pragyanCtf2020 darkknight$ exiftool mrRobot.jpg 
ExifTool Version Number         : 10.55
File Name                       : mrRobot.jpg
Directory                       : .
File Size                       : 857 kB
File Modification Date/Time     : 2020:02:22 09:09:10-08:00
File Access Date/Time           : 2020:02:22 09:29:18-08:00
File Inode Change Date/Time     : 2020:02:22 09:10:49-08:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Exif Byte Order                 : Big-endian (Motorola, MM)
X Resolution                    : 28
Y Resolution                    : 28
Resolution Unit                 : cm
Artist                          : 8f068b017cd807fd3b8c684dea2f8156
Y Cb Cr Positioning             : Centered
XMP Toolkit                     : Image::ExifTool 11.70
Format                          : U29tZSBTSEEgbWF5YmUhISEh
Comment                         : c82358dfb202ce9cfddc34e13d403fa3
Image Width                     : 2560
Image Height                    : 1920
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 2560x1920
Megapixels                      : 4.9

root@beeBeeEight:~/ctfs# 
root@beeBeeEight:~/ctfs# steghide info robot.jpg 
"robot.jpg":
  format: jpeg
  capacity: 51.1 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "flag.txt":
    size: 84.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
root@beeBeeEight:~/ctfs# steghide extract -sf robot.jpg 
Enter passphrase: 
the file "flag.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "flag.txt".
root@beeBeeEight:~/ctfs# 
root@beeBeeEight:~/ctfs# cat flag.txt 
Congrats! This was way too wasy :P

This is the key:

p_ctf{@_r0b0t_c@n_help_u_t00}
root@beeBeeEight:~/ctfs# 
