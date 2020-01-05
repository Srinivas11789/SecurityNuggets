```bash
root@kali:~/Downloads/forensics# fcrackzip -v -D -p /usr/share/wordlists/rockyou.txt -u output.zip 
found file 'flag.gif', (size cp/uc 174326/180688, flags 9, chk 61ad)
checking pw arizon1                                 

PASSWORD FOUND!!!!: pw == Malhotra
root@kali:~/Downloads/forensics# unzip output.zip 
Archive:  output.zip
[output.zip] flag.gif password: 
  inflating: flag.gif                
root@kali:~/Downloads/forensics# open flag.gif 
bash: open: command not found
root@kali:~/Downloads/forensics# strings flag.gif | grep -i "inferno"
root@kali:~/Downloads/forensics# vi flag.gif
root@kali:~/Downloads/forensics# file flag.gif 
flag.gif: data
root@kali:~/Downloads/forensics# foremost flag.gif 
Processing: flag.gif
|*|
root@kali:~/Downloads/forensics# cat output/audit.txt 
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Fri Dec 27 16:30:00 2019
Invocation: foremost flag.gif 
Output directory: /root/Downloads/forensics/output
Configuration file: /etc/foremost.conf
------------------------------------------------------------------
File: flag.gif
Start: Fri Dec 27 16:30:00 2019
Length: 176 KB (180688 bytes)
 
Num	 Name (bs=512)	       Size	 File Offset	 Comment 

Finish: Fri Dec 27 16:30:00 2019

0 FILES EXTRACTED
	
------------------------------------------------------------------

Foremost finished at Fri Dec 27 16:30:00 2019
root@kali:~/Downloads/forensics# binwalk flag.gif 

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------

root@kali:~/Downloads/forensics# xxd flag.gif 
00000000: 4141 4141 4161 5304 6900 e7fb 0032 0000  AAAAAaS.i....2..
00000010: 3800 023b 0000 4100 0343 0000 4900 034d  8..;..A..C..I..M
00000020: 0000 5600 0050 0200 6000 005c 0400 6a00  ..V..P..`..\..j.
00000030: 0164 0200 7400 016f 0300 7801 007f 0002  .d..t..o..x.....
00000040: 8302 008a 0002 8c00 007c 0802 660f 0290  .........|..f...
00000050: 0600 760e 0688 0a03 7911 016b 1509 8110  ..v.....y..k....
00000060: 0794 0d03 8513 0271 1905 8e12 0880 1908  .......q........
00000070: 9813 0677 200c 941a 057d 2108 861e 0d8e  ...w ....}!.....
00000080: 1d09 7525 0c9d 1a0a ff00 008b 2309 a11e  ..u%........#...
00000090: 059b 220b 8429 0c8f 2705 a523 0898 270a  .."..)..'..#..'.
000000a0: 7f2e 0f94 2b0f a926 0b85 320a a229 1092  ....+..&..2..)..
000000b0: 310f ac2a 0ea7 2c0c 8338 0ea1 2f11 a92e  1..*..,..8../...
000000c0: 0488 3a05 a030 24b1 2e12 a533 0c9f 3511  ..:..0$....3..5.
000000d0: 9c38 11b5 320d 8242 0bb0 3513 b237 0cad  .8..2..B..5..7..
000000e0: 3912 bb37 12a0 4104 aa3e 13a3 4018 814e  9..7..A..>..@..N
000000f0: 0ab9 3d13 c03b 16a7 4313 b33f 18b1 4419  ..=..;..C..?..D.
00000100: b943 15c0 4210 bb44 0cbf 4218 b049 17b7  .C..B..D..B..I..
00000110: 4815 8459 0881 5821 c345 1bad 4d1a c547  H..Y..X!.E..M..G
00000120: 14c1 4a1b ad53 1ec0 4f11 cb4b 19bf 4f1c  ..J..S..O..K..O.
00000130: ba52 0ec6 4e17 b356 18b8 551d bd54 1db7  .R..N..V..U..T..
00000140: 5907 d050 1db2 5b18 ae60 13cf 551f a864  Y..P..[..`..U..d
...
...
...
```