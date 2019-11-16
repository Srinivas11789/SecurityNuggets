# Solve

* JPEG steganography --> it should be either LSB, MSB steg or image layer steg

* Beefore that, we should start with some ground work so that we dont miss any,

```
srimbp-623:stego_the_doge sri$ exiftool the_doge.jpg 
ExifTool Version Number         : 11.30
File Name                       : the_doge.jpg
Directory                       : .
File Size                       : 21 kB
File Modification Date/Time     : 2019:11:16 09:45:25-08:00
File Access Date/Time           : 2019:11:16 09:46:10-08:00
File Inode Change Date/Time     : 2019:11:16 09:45:25-08:00
File Permissions                : rw-r--r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.02
Resolution Unit                 : None
X Resolution                    : 1
Y Resolution                    : 1
Image Width                     : 550
Image Height                    : 413
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 550x413
Megapixels                      : 0.227
srimbp-623:stego_the_doge sri$ binwalk the_doge.jpg 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02

srimbp-623:stego_the_doge sri$ jpeg
jpeg2ktopam  jpegtopnm    jpegtran     
srimbp-623:stego_the_doge sri$ gimp the_doge.jpg 
```

* Stegsolve and Steghide next....
  - Stegsolve was not much helpful, so maybe a passphrase or password was used to add data
  - Steghide extract it is, password provided by the hint in the question `treat`
```
root@kali:~# 
root@kali:~# steghide extract -sf the_doge.jpg 
Enter passphrase: 
steghide: could not extract any data with that passphrase!
root@kali:~# steghide extract -sf the_doge.jpg -p treat
the file "doge_ctf.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "doge_ctf.txt".
root@kali:~# 
root@kali:~# cat doge_ctf.txt 
RITSEC{hAppY_l1L_doG3}
root@kali:~# 

```

* Some LSB or MSB Stagano next but previous one solved it..