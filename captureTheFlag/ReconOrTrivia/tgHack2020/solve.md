### Number Trouble

* Challenge
```
My friend only speaks in numbers. What does he say?

84 71 50 48 123 110 117 109 98 101 114 115 95 97 110 100 95 116 101 120 116 95 103 111 101 115 95 104 97 110 100 95 105 110 95 104 97 110 100 125
Need help?
```

* Solve
```
>>> code = "84 71 50 48 123 110 117 109 98 101 114 115 95 97 110 100 95 116 101 120 116 95 103 111 101 115 95 104 97 110 100 95 105 110 95 104 97 110 100 125"
>>> new = code.split(" ")
>>> flag = ""
>>> for n in new:
...   flag += chr(int(n))
... 
>>> flag
'TG20{numbers_and_text_goes_hand_in_hand}'
>>> 
```

### Secret Bases

* Challenge
```
We managed to extract this secret information from one of Mother's 64 secret bases before we had to leave Earth. Are you able to decode it?

VEcyMHt5b3VfY2FuX25ldmVyX2hhdmVfZW5vdWdoX3NlY3JldF9iYXNlc30=
```

* Solve
```
>>> import base64
>>> base64.b64decode("VEcyMHt5b3VfY2FuX25ldmVyX2hhdmVfZW5vdWdoX3NlY3JldF9iYXNlc30=")
'TG20{you_can_never_have_enough_secret_bases}'
>>> 
```

### Shifty Science

* Challenge
```
This flag was tampered with by a shifty scientist. Can you get it back to normal?

BO20{xtmiam_lwvb_bzg_apqnba_tqsm_bpqa_ib_pwum}
```

* Solve
* It is ROT-8 of the cipher
```
TG20{please_dont_try_shifts_like_this_at_home}
```

### Is This The One? Or Zero?

* Challenge
```
Help me decrypt this, it's important for gaia!

00110011 00100110 01011011 01010001 00011100 00001110 
00000111 00000100 00111000 00001110 00011011 00111110 
00011101 00000100 00011011 00001110 00111000 00000011 
00011100 00010101 00111000 00001111 00000110 00010101 
00111000 00000011 00000110 00010101 00001111 00011100
```

* Solve
```

```