### Challenge

```
The flag is right between your finger tips.

Download the file below.
```

### Solve

```
kali@kali:~$ foremost -a thumbcache_256.db -o thumbcache
Processing: thumbcache_256.db
|*|
kali@kali:~$ cd thumbcache/
kali@kali:~/thumbcache$ ls
audit.txt  jpg  png
kali@kali:~/thumbcache$ cat audit.txt 
Foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus
Audit File

Foremost started at Fri Jul 31 01:37:09 2020
Invocation: foremost -a thumbcache_256.db -o thumbcache 
Output directory: /home/kali/thumbcache
Configuration file: /etc/foremost.conf
------------------------------------------------------------------
File: thumbcache_256.db
Start: Fri Jul 31 01:37:09 2020
Length: 1024 KB (1048576 bytes)
 
Num      Name (bs=512)         Size      File Offset     Comment 

0:      00000156.jpg           5 KB           80032      
1:      00000002.png          24 KB            1306       (256 x 256)
2:      00000050.png          11 KB           26084       (256 x 256)
3:      00000073.png          17 KB           37474       (256 x 256)
4:      00000108.png          24 KB           55356       (256 x 256)
Finish: Fri Jul 31 01:37:09 2020

5 FILES EXTRACTED

jpg:= 1
png:= 4
------------------------------------------------------------------

Foremost finished at Fri Jul 31 01:37:09 2020

```

* JPEG has the flag