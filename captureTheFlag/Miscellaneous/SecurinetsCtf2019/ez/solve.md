root@kali:~/Downloads# file pic.png 
pic.png: PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
root@kali:~/Downloads# binwalk pic.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1920 x 1080, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, default compression

root@kali:~/Downloads# file pic.png 
pic.png: PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
root@kali:~/Downloads# exiftool pic.png 
ExifTool Version Number         : 11.16
File Name                       : pic.png
Directory                       : .
File Size                       : 1102 kB
File Modification Date/Time     : 2019:03:20 08:23:22-07:00
File Access Date/Time           : 2019:03:23 10:42:42-07:00
File Inode Change Date/Time     : 2019:03:23 10:41:09-07:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1920
Image Height                    : 1080
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1920x1080
Megapixels                      : 2.1

root@kali:~/Downloads# exif pic.png
Corrupt data
The data provided does not follow the specification.
ExifLoader: The data supplied does not seem to contain EXIF data.

root@kali:~/Downloads# exiftool pic.png 
ExifTool Version Number         : 11.16
File Name                       : pic.png
Directory                       : .
File Size                       : 1102 kB
File Modification Date/Time     : 2019:03:20 08:23:22-07:00
File Access Date/Time           : 2019:03:23 10:42:42-07:00
File Inode Change Date/Time     : 2019:03:23 10:41:09-07:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1920
Image Height                    : 1080
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1920x1080
Megapixels                      : 2.1
root@kali:~/Downloads# exiftool pic.png 
ExifTool Version Number         : 11.16
File Name                       : pic.png
Directory                       : .
File Size                       : 1102 kB
File Modification Date/Time     : 2019:03:20 08:23:22-07:00
File Access Date/Time           : 2019:03:23 10:42:42-07:00
File Inode Change Date/Time     : 2019:03:23 10:41:09-07:00
File Permissions                : rw-r--r--
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 1920
Image Height                    : 1080
Bit Depth                       : 8
Color Type                      : RGB
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Image Size                      : 1920x1080
Megapixels                      : 2.1

root@kali:~/Downloads# binwalk pic.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1920 x 1080, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, default compression


root@kali:~/Downloads# binwalk -e pic.png 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 1920 x 1080, 8-bit/color RGB, non-interlaced
41            0x29            Zlib compressed data, default compression

(ssss) root@kali:~/Downloads# cat stego.py 
#!/usr/bin/env python

from PIL import Image
import binascii

def ExtractMessage(carrier):
    c = Image.open(carrier)
    x, y = c.size[0], c.size[1]
    new_array = ""
    out = ""
    for i in range(x):
        for j in range(y):
            new_array = ""
            rgb = c.getpixel((i,j))
            for color in rgb:
                if color%2 == 0:
                    new_array += "0"
                else:
                    new_array += "1"
            #new_array = "".join(new_array)
            out += chr(int(new_array, 2))
    print(out)
    if "start" in out:
        print("YESS")
    #new_array = [new_array[i:i+8] for i in range(0, len(new_array), 8)]
    #print new_array
    #print ''.join([chr(int(x, 2)) for x in new_array])

def decode(img): 
    image = Image.open(img) 
    data = '' 
    imgdata = iter(image.getdata()) 
      
    while (True): 
        pixels = [value for value in imgdata.__next__()[:3] +
                                  imgdata.__next__()[:3] +
                                  imgdata.__next__()[:3]] 
        # string of binary data 
        binstr = '' 
          
        for i in pixels[:8]: 
            if (i % 2 == 0): 
                binstr += '0'
            else: 
                binstr += '1'
                  
        data += chr(int(binstr, 2)) 
        if (pixels[-1] % 2 != 0): 
            return data 

def newer(img):
    image = Image.open(img)

    extracted = ''

    pixels = image.load()
    # Iterate over pixels of the first row
    for y in range(0, image.height):
        for x in range(0, image.width):
            r,g,b = pixels[x,y]
            extracted += bin(r)[-1]
            extracted += bin(g)[-1]
            extracted += bin(b)[-1]

    chars = []
    for i in range(int(len(extracted)/8)):
        byte = extracted[i*8:(i+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    chars = ("".join(chars)).split(" ")
    for c in range(len(chars)):
        if "END" in chars[c]:
            print(" ".join(chars[:c+1]))

#print(decode("pic.png"))
#ExtractMessage("pic.png")
newer("pic.png")
(ssss) root@kali:~/Downloads# 

root@kali:~/Downloads# zsteg pic.png 
b1,rgb,lsb,xy       .. text: "--START--\n\"The fact is that upon his entrance I had instantly recognized the extreme\npersonal danger in which I lay. The only conceivable escape for him lay in silencing\nmy tongue. In an instant I had slipped the revolver from the drawer into my\npocket and"
b2,b,msb,xy         .. text: "_uW}W}W}"
b3,b,lsb,xy         .. file: very old 16-bit-int big-endian archive
b4,r,lsb,xy         .. text: "\nvvwgffwfwvwgg"
b4,g,lsb,xy         .. text: "gwvwvffwvgvfggfvwgvfvgfgvgffvwfvwgfvfgvvwwvfwgfwfgvgvgffwgffffffwgfffgfgvwvfwgvfwwfwvwfgvwvfwgvffgvfvwffwgvwvwvfggffvgfgwgfffgvfwgvfvgffwgfwwgfgwgfffgvfwwvfvgfffgvgwgffvwvgvwvfvgfgwgvfvwfgvwfffgvgvgffwwvfwgfvfgfgfgffwgvgvwfgvvffwwfvwwvgvwvgfffgfgfgfgfgvwvf"
b4,b,lsb,xy         .. text: "wfgggfgfgffwffwfvfffwfggwfgwvfgfvfgfvggfwfvfvfggvfgvwgwgwfwgvfffvfgfvfgvvgggwggvvfgfwfwwwfwwvfgfvggvwfggvggfwfggfgggvgwwwfgvvfggwfwgvfgwwfggvfggvfgwvfggvfvfgfggvfwvwgffvfwvvfgwwfgfwfffwgwgvgggvfwwvfgvvfffwfgwvfgvvgwwwfgvvfgvwfwwvfgfwfwgwffvvfgvvfgvvfgvvggg"
b4,rgb,lsb,xy       .. text: "ogWef&vfFmw"
b4,rgb,msb,xy       .. text: "`vnovng>"
b4,bgr,lsb,xy       .. text: "ogVev&ffG}g"
root@kali:~/Downloads# 


(ssss) root@kali:~/Downloads# python3 stego.py 
--START--
"The fact is that upon his entrance I had instantly recognized the extreme
personal danger in which I lay. The only conceivable escape for him lay in silencing
my tongue. In an instant I had slipped the revolver from the drawer into my
pocket and was covering him through the cloth. At his remark I drew the weapon
out and laid it cocked upon the table. He still smiled and blinked, but there was
something about his eyes which made me feel very glad that I had it there,
"You evidently don't know me,' said he.
"'On the contrary,' I answered, 'I think it is fairly evident that I do. Pray take
a chair. I can spare you five minutes if you have anything to say.'
"'All that I have to say has already crossed your mind,' said he.
"'Then possibly my answer has crossed yours,' I replied.
"'You stand fast?'
"'Absolutely.'
"He clapped his hand into his pocket, and I raised the pistol from the table.
But he merely drew out a <DETELED_WORD> in which he had scribbled some
dates.
"You crossed my path on the fourth of January,' said he. 'On the twenty-third
you incommoded me; by the middle of February I was seriously inconvenienced
by you; at the end of March I was absolutely hampered in my plans; and now, at
the close of April, I find myself placed in such a position through your continual
persecution that I am in positive danger of losing my liberty. The situation is
becoming an impossible one.'
"'Have you any suggestion to make?' I asked.
"'You must drop it, Mr. Holmes,' said he, swaying his face about. 'You really
must, you know.'"
--END--;o¶Ûÿ¶ß}þßý¶û·ûo¿ûï·Ûo¿ûm¿ßo¿ûï·Ûÿ¶Ûí¿ßí·Ûo¿Û}¿ûo¶Ûm¶Ûm¶Ûm¿Ûm¶ûÿ·ûm¶ûm÷Û}¶Ûm¶Ûm¶Ûm¶Ûm·Ûm¶Ûm¶Ûm¶Ûm¶Ûm¶ßÿ¶Û}¶Ûm¶Ûm¶Ûÿ¶ßÿ¶Ûm¶Ûm¶ßo¾ßm÷ßm¶

