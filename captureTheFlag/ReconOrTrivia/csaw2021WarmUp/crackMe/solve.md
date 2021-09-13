* Chall
```
Crack Me
63
Can you crack this? Your hash: a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c. Your salt: the encryption method of the hash. (So if the hash is of the word example, you would submit flag{example} to score points.) UPDATE Friday 9PM: To streamline your efforts we would like to give you some more details about the format for the hash encryption method. An example: if you think the hash is RIPEMD-128, use ripemd128 for the salt.
```

* Identify
```
──(kali㉿kali)-[~]
└─$ hash-identifier
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c

Possible Hashs:
[+] SHA-256
[+] Haval-256

```

* hash:salt --> `a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256`

* Crack
```
──(kali㉿kali)-[~]
└─$ hashcat -m 1420 -a 0  csaw21.txt /usr/share/wordlists/rockyou.txt
hashcat (v2.01-7258-g286002a8d) starting...

OpenCL API (OpenCL 1.2 pocl 1.5, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz, 1785/1849 MB (512 MB allocatable), 3MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256
Minimim salt length supported by kernel: 0
Maximum salt length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Iterated
* Single-Hash
* Single-Salt
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545ebf24cdc0b76c:sha256:cathouse
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Name........: sha256($salt.$pass)
Hash.Target......: a60458d2180258d47d7f7bef5236b33e86711ac926518ca4545...sha256
Time.Started.....: Sat Sep 11 13:03:14 2021 (1 sec)
Time.Estimated...: Sat Sep 11 13:03:15 2021 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   796.2 kH/s (0.18ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 142080/14344385 (0.99%)
Rejected.........: 0/142080 (0.00%)
Restore.Point....: 141312/14344385 (0.99%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: charles. -> ashleen

Started: Sat Sep 11 13:02:58 2021
Stopped: Sat Sep 11 13:03:16 2021
                                                                                                            
┌──(kali㉿kali)-[~]
└─$ 

```

* flag{cathouse}