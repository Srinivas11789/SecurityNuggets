# Solve

### Challenge
* Encoded text and we have to decode correctly continuously until we are returned the flag

### Recon

```
srimbp-623:sonic sri$ nc chal.tuctf.com 30100 > test.txt
srimbp-623:sonic sri$ cat test.txt 

    ___------__
 |\__-- /\       _-
 |/    __      -
 //\  /  \    /__
 |  o|  0|__     --_
 \____-- __ \   ___-
 (@@    __/  / /_
    -_____---   --_
    //  \ \\   ___-
    //|\__/  \  \
    \_-\_____/  \-\
        // \\--\| 
    ____//  ||_
  /_____\ /___\

  Gotta go fast!

  
Hey, decode this: PHRIH
Too slow!
```

### Solution

```
srimbp-623:sonic sri$ python solve.py chal.tuctf.com 30100 "\n"
[+] Opening connection to chal.tuctf.com on port 30100: Done

    ___------__
 |\__-- /\       _-
 |/    __      -
 //\  /  \    /__
 |  o|  0|__     --_
 \____-- __ \   ___-
 (@@    __/  / /_
    -_____---   --_
    //  \ \\   ___-
    //|\__/  \  \
    \_-\_____/  \-\
        // \\--\| 
    ____//  ||_
  /_____\ /___\

  Gotta go fast!

  
Hey, decode this: AMLEPCQQGMLYJ

['\n', '', '', '', '___------__\n', '|\\__--', '/\\', '', '', '', '', '', '', '_-\n', '|/', '', '', '', '__', '', '', '', '', '', '-\n', '//\\', '', '/', '', '\\', '', '', '', '/__\n', '|', '', 'o|', '', '0|__', '', '', '', '', '--_\n', '\\____--', '__', '\\', '', '', '___-\n', '(@@', '', '', '', '__/', '', '/', '/_\n', '', '', '', '-_____---', '', '', '--_\n', '', '', '', '//', '', '\\', '\\\\', '', '', '___-\n', '', '', '', '//|\\__/', '', '\\', '', '\\\n', '', '', '', '\\_-\\_____/', '', '\\-\\\n', '', '', '', '', '', '', '', '//', '\\\\--\\|', '\n', '', '', '', '____//', '', '||_\n', '', '/_____\\', '/___\\\n\n', '', 'Gotta', 'go', 'fast!\n\n', '', '\nHey,', 'decode', 'this:', 'AMLEPCQQGMLYJ\n']
('BNMFQDRRHNMZK', 1)
('CONGRESSIONAL', 2)
Sending... CONGRESSIONAL

You got it!

Here's your prize:
TUCTF{W04H_DUD3_S0_F4ST_S0N1C_4PPR0V3S}

['\nYou', 'got', "it!\n\nHere's", 'your', 'prize:\nTUCTF{W04H_DUD3_S0_F4ST_S0N1C_4PPR0V3S}\n']
('WYPGL;\x0bUVDUGHX15IFEVE4FT1FG5TUFT1O2DF5QQS1W4TJ', 1)
('XZQHM<\x0cVWEVHIY26JGFWF5GU2GH6UVGU2P3EG6RRT2X5UK', 2)
('YARIN=\rWXFWIJZ37KHGXG6HV3HI7VWHV3Q4FH7SSU3Y6VL', 3)
('ZBSJO>\x0eXYGXJKA48LIHYH7IW4IJ8WXIW4R5GI8TTV4Z7WM', 4)
('ACTKP?\x0fYZHYKLB59MJIZI8JX5JK9XYJX5S6HJ9UUW5A8XN', 5)
('BDULQ@\x10ZAIZLMC6:NKJAJ9KY6KL:YZKY6T7IK:VVX6B9YO', 6)
('CEVMRA\x11ABJAMND7;OLKBK:LZ7LM;ZALZ7U8JL;WWY7C:ZP', 7)
('DFWNSB\x12BCKBNOE8<PMLCL;MA8MN<ABMA8V9KM<XXZ8D;AQ', 8)
('EGXOTC\x13CDLCOPF9=QNMDM<NB9NO=BCNB9W:LN=YYA9E<BR', 9)
('FHYPUD\x14DEMDPQG:>RONEN=OC:OP>CDOC:X;MO>ZZB:F=CS', 10)
('GIZQVE\x15EFNEQRH;?SPOFO>PD;PQ?DEPD;Y<NP?AAC;G>DT', 11)
('HJARWF\x16FGOFRSI<@TQPGP?QE<QR@EFQE<Z=OQ@BBD<H?EU', 12)
('IKBSXG\x17GHPGSTJ=AURQHQ@RF=RSAFGRF=A>PRACCE=I@FV', 13)
('JLCTYH\x18HIQHTUK>BVSRIRASG>STBGHSG>B?QSBDDF>JAGW', 14)
('KMDUZI\x19IJRIUVL?CWTSJSBTH?TUCHITH?C@RTCEEG?KBHX', 15)
('LNEVAJ\x1aJKSJVWM@DXUTKTCUI@UVDIJUI@DASUDFFH@LCIY', 16)
('MOFWBK\x1bKLTKWXNAEYVULUDVJAVWEJKVJAEBTVEGGIAMDJZ', 17)
('NPGXCL\x1cLMULXYOBFZWVMVEWKBWXFKLWKBFCUWFHHJBNEKA', 18)
('OQHYDM\x1dMNVMYZPCGAXWNWFXLCXYGLMXLCGDVXGIIKCOFLB', 19)
('PRIZEN\x1eNOWNZAQDHBYXOXGYMDYZHMNYMDHEWYHJJLDPGMC', 20)
('QSJAFO\x1fOPXOABREICZYPYHZNEZAINOZNEIFXZIKKMEQHND', 21)
('RTKBGP PQYPBCSFJDAZQZIAOFABJOPAOFJGYAJLLNFRIOE', 22)
('SULCHQ!QRZQCDTGKEBARAJBPGBCKPQBPGKHZBKMMOGSJPF', 23)
('TVMDIR"RSARDEUHLFCBSBKCQHCDLQRCQHLIACLNNPHTKQG', 24)
('UWNEJS#STBSEFVIMGDCTCLDRIDEMRSDRIMJBDMOOQIULRH', 25)
('VXOFKT$TUCTFGWJNHEDUDMESJEFNSTESJNKCENPPRJVMSI', 26)
Sending... no match!
[*] Switching to interactive mode
[*] Got EOF while reading in interactive
```
