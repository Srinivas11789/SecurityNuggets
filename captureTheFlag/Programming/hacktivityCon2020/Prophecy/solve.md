### Challenge
```
C A N Y O U S E E T H E F U T U R E ?

Connect with:
nc jh2i.com 50012
```

### Solve
* Testing to check the prophecy
```
$ nc jh2i.com 50012


       ██████  ██████   ██████  ██████  ██   ██ ███████  ██████ ██    ██ 
       ██   ██ ██   ██ ██    ██ ██   ██ ██   ██ ██      ██       ██  ██  
       ██████  ██████  ██    ██ ██████  ███████ █████   ██        ████   
       ██      ██   ██ ██    ██ ██      ██   ██ ██      ██         ██    
       ██      ██   ██  ██████  ██      ██   ██ ███████  ██████    ██    

 
==============================================================================
 
                         I C A N S E E T H E F U T U R E
 
==============================================================================
 
 W H A T I S T H E N E X T N U M B E R T O C O M E F R O M T H E F U T U R E ?
 
> 99126
 
 W H A T I S T H E N E X T N U M B E R T O C O M E F R O M T H E F U T U R E ?
 
> 213
 
         F A I L U R E . T H E C O R R E C T N U M B E R W A S 76106
```
* We could trial and error to obtain all the numbers and reiterate through them starting over everytime we have a mistake

* The server was not stable so made extra retries with 10 second buffer

```
$ python3 prophecy.py 
[-] Opening connection to jh2i.com on port 50012: Failed
[ERROR] Could not connect to jh2i.com on port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[]
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378']
[*] Closed connection to jh2i.com port 50012
[-] Opening connection to jh2i.com on port 50012: Failed
[ERROR] Could not connect to jh2i.com on port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561']
[*] Closed connection to jh2i.com port 50012
[-] Opening connection to jh2i.com on port 50012: Failed
[ERROR] Could not connect to jh2i.com on port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030', b'53097']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030', b'53097', b'53885']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030', b'53097', b'53885', b'29931']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030', b'53097', b'53885', b'29931', b'10890']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030', b'53097', b'53885', b'29931', b'10890', b'20583']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030', b'53097', b'53885', b'29931', b'10890', b'20583', b'46190']
[*] Closed connection to jh2i.com port 50012
[+] Opening connection to jh2i.com on port 50012: Done
[b'99126', b'76106', b'32378', b'49560', b'87935', b'17366', b'36639', b'33561', b'51241', b'24009', b'82718', b'65774', b'87030', b'53097', b'53885', b'29931', b'10890', b'20583', b'46190', b'83643']
b' ==============================================================================\n \n                       Y O U T O O C A N S E E T H E F U T U R E\n \n==============================================================================\nflag{does_this_count_as_artificial_intelligence}\n'
```