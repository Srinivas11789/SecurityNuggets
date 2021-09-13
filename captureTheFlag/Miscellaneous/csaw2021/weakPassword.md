* Challenge

```
Can you crack Aaron’s password hash? He seems to like simple passwords. I’m sure he’ll use his name and birthday in it. Hint: Aaron writes important dates as YYYYMMDD rather than YYYY-MM-DD or any other special character separator. Once you crack the password, prepend it with flag{ and append it with } to submit the flag with our standard format. Hash: 7f4986da7d7b52fa81f98278e6ec9dcb.
```

* match md5 hashes with possible [aaronAARON]YYYYMMDD == 7f4986da7d7b52fa81f98278e6ec9dcb

* Solving using hashcat with mask attack

```
┌──(kali㉿kali)-[/usr/share/hashcat/rules]
└─$ hashcat -a 3 -m 0 weakPassword.txt Aaron?d?d?d?d?d?d?d?d                                                                                               1 ⨯

hashcat (v2.01-7258-g286002a8d) starting...

OpenCL API (OpenCL 1.2 pocl 1.5, None+Asserts, LLVM 9.0.1, RELOC, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
=============================================================================================================================
* Device #1: pthread-Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz, 1785/1849 MB (512 MB allocatable), 3MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 256

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates

Optimizers applied:
* Zero-Byte
* Early-Skip
* Not-Salted
* Not-Iterated
* Single-Hash
* Single-Salt
* Brute-Force
* Raw-Hash

ATTENTION! Pure (unoptimized) backend kernels selected.
Using pure kernels enables cracking longer passwords but for the price of drastically reduced performance.
If you want to switch to optimized backend kernels, append -O to your commandline.
See the above message to find out about the exact limits.

Watchdog: Hardware monitoring interface not found on your system.
Watchdog: Temperature abort trigger disabled.

Host memory required for this attack: 0 MB

[s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit => s

Session..........: hashcat
Status...........: Running
Hash.Name........: MD5
Hash.Target......: 7f4986da7d7b52fa81f98278e6ec9dcb
Time.Started.....: Sun Sep 12 18:18:36 2021 (3 secs)
Time.Estimated...: Sun Sep 12 18:19:05 2021 (26 secs)
Guess.Mask.......: Aaron?d?d?d?d?d?d?d?d [13]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  3492.5 kH/s (0.05ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 0/1 (0.00%) Digests
Progress.........: 8550144/100000000 (8.55%)
Rejected.........: 0/8550144 (0.00%)
Restore.Point....: 8550144/100000000 (8.55%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: Aaron72005378 -> Aaron20993589

7f4986da7d7b52fa81f98278e6ec9dcb:Aaron19800321            
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Name........: MD5
Hash.Target......: 7f4986da7d7b52fa81f98278e6ec9dcb
Time.Started.....: Sun Sep 12 18:18:36 2021 (7 secs)
Time.Estimated...: Sun Sep 12 18:18:43 2021 (0 secs)
Guess.Mask.......: Aaron?d?d?d?d?d?d?d?d [13]
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:  3300.0 kH/s (0.06ms) @ Accel:256 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests
Progress.........: 23803392/100000000 (23.80%)
Rejected.........: 0/23803392 (0.00%)
Restore.Point....: 23802624/100000000 (23.80%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: Aaron78077430 -> Aaron29199430

Started: Sun Sep 12 18:18:34 2021
Stopped: Sun Sep 12 18:18:45 2021
                                                                                                                                                               
┌──(kali㉿kali)-[/usr/share/hashcat/rules]
```

* flag --> flag{Aaron19800321}