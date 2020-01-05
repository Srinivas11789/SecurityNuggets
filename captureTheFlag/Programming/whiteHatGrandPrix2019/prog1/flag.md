```
srimbp-623:whiteHatGrandPrix2019 sri$ python pwn_algo.py "15.164.75.32" "1999" "Answer:"
[+] Opening connection to 15.164.75.32 on port 1999: Done

PROGRAMING - WHITEHAT GRANDPRIX 06:

--> COUNT THE NUMBER OF POSSIBLE TRIANGLES <--

HOW MANY TRIANGLES ARE CREATED BY N (1..N) NUMBER. N < 10^6

Example:  N = 5
OUTPUT : 3 

(2,3,4),(3,4,5),(2,4,5)
................/\...................|\...................
.............../  \..................| \..................
............../    \.................|  \.................
............./      \................|   \................
............/        \...............|    \...............
.........../          \..............|     \..............
........../____________\.............|______\.............
    
n = 7
Answer:
 Well done! Let's accelerate.n = 1000
Answer:
 Great ! the last challenge. n = 11111
Answer:
[*] Switching to interactive mode
  You are Victorious :WhiteHat{Y0u_h4v3_4_Sm4rt_Br41n}[*] Got EOF while reading in interactive
$  
[20]+  Stopped                 python pwn_algo.py "15.164.75.32" "1999" "Answer:"
srimbp-623:whiteHatGrandPrix2019 sri$ python
Python 2.7.15 (default, Jan 12 2019, 21:07:57) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import hashlib
>>> hashlib.sha256("Y0u_h4v3_4_Sm4rt_Br41n").hexdigest()
'571c7c63f05e31b6ab5a84a89522fcbc3b87c4f1116a80cfcdf04f931ef35ccb'
>>> hashlib.sha1("Y0u_h4v3_4_Sm4rt_Br41n").hexdigest()
'e6bee01defdbcb5fab218342855b49b1b3e6fe8b'
>>> 
[21]+  Stopped                 python
srimbp-623:whiteHatGrandPrix2019 sri$ 
```