### I CANT SEE YOU

* Challenge
```
I can't see you!
Misc
Can you know me? (all capital letters)
```

* Recon
  - It is a encrypted RAR file
  - GOOGLE or any search for possible HINTs and keywords based on the challenge string for the password..
  - Best approach here is `BRUTEFORCE`
  - For a zip file, we could use `fcrackzip`, in this case it is a rar file
  - Using `RARCRACK`, I did not find a way to use wordlists though ( rockyou ). It was performed brute force and was slow.
```
root@kali:~/Downloads# rarcrack --type zip --threads 4 what.rar 
RarCrack! 0.2 by David Zoltan Kedves (kedazo@gmail.com)

INFO: the specified archive type: zip
INFO: cracking what.rar, status file: what.rar.xml
INFO: Resuming cracking from password: 'pIIC'
Probing: 'pJSZ' [1494 pwds/sec]
Probing: 'pL1h' [1452 pwds/sec]
^C
root@kali:~/Downloads# 
``` 

  - I wanted to desparately use chosen wordlist --> Use `JOHN` --> Ref: https://bytesoverbombs.io/cracking-everything-with-john-the-ripper-d434f0f6dc1c
```
root@kali:~/Downloads# unrar l what.rar 

UNRAR 5.61 beta 1 freeware      Copyright (c) 1993-2018 Alexander Roshal

Archive: what.rar
Details: RAR 5

 Attributes      Size     Date    Time   Name
----------- ---------  ---------- -----  ----
*   ..A....     37033  2019-12-28 01:46  picture.png
----------- ---------  ---------- -----  ----
                37033                    1

root@kali:~/Downloads# unrar x what.rar 

UNRAR 5.61 beta 1 freeware      Copyright (c) 1993-2018 Alexander Roshal


Extracting from what.rar

Enter password (will not be echoed) for picture.png: 

root@kali:~/Downloads# rar2john what.rar > what.rar.hash
root@kali:~/Downloads# john --wordlist=/usr/share/wordlists/rockyou.txt what.rar.hash 
Using default input encoding: UTF-8
Loaded 1 password hash (RAR5 [PBKDF2-SHA256 256/256 AVX2 8x])
Cost 1 (iteration count) is 32768 for all loaded hashes
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
blind            (what.rar)
1g 0:00:00:29 DONE (2020-01-01 09:38) 0.03386g/s 654.5p/s 654.5c/s 654.5C/s mormor..231089
Use the "--show" option to display all of the cracked passwords reliably
Session completed
root@kali:~/Downloads# unrar x what.rar 

UNRAR 5.61 beta 1 freeware      Copyright (c) 1993-2018 Alexander Roshal


Extracting from what.rar

Enter password (will not be echoed) for picture.png: 

Extracting  picture.png                                               OK 
All OK
root@kali:~/Downloads# open picture.png 
bash: open: command not found
root@kali:~/Downloads# file picture.png 
picture.png: PNG image data, 1543 x 800, 8-bit colormap, interlaced
root@kali:~/Downloads# gimp picture.png
root@kali:~/Downloads# 
```

* The Image was a braille code and using `dcode` to convert braille

* Flag: `BAMBOOFOX{YA_YOU_KNOW_WHAT_BLIND_MEANS}`