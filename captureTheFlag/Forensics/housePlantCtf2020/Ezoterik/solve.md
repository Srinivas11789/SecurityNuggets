### Challenge
```
Inventing languages is hard. Luckily, there's plenty of them, including stupid ones.

Dev: Tom
 Hint! You will find what you seek beyond the whitespace
 ezoterik.jpg 2ccd8135a03c5936b6f0b4e989db8a30
```

### Solve
* Esoteric programming languages --> Looks like BrainFuck per the image
* https://en.wikipedia.org/wiki/Esoteric_programming_language
* Encoded bf in image --> 
```
+[--->++<]>+++.[->++++<]>+.----.+++++++.----[->+++<]>.------------.+[----->+<]>+.+.[->+++++<]>+.------------.---[->++++<]>-.----.+++..+++++++.-----[++>---<]>.
```
* Decoded to --> `Yeah, no, sorry.`
* Hint about whitespace, they gave us an image
* Embedded contents --> Binwalk, Comments or trailer data --> exif data, unusual strings --> strings or vi
* unusual data at the end with vi editor or strings, 
```
2TLEdubBbS21p7u3AUWQpj1TB98gUrgHFAiFZmbeJ8qZFb9qCUc8Qp6o86eJYkrm2NLexkSDyRYd3X9sRCRKJzoZnDtrWZKcHPxjoRaFPHfmeUyoxyyWQtiqEgdJR1WU4ywAYqRq7o55XLUgmdit6svgviN8qy72wvLvT2eWjECbqHdrKa2WjiAEvgaGxVedY8SRXXcU9JbP5Ps3RY2ieejz6DrF9NBD7mri2wrsyDs9gpVgosxnYPbwjGdmsq7GwudbqtJ7SeKgaStmygyfPast5F3ZKL9KeC2LzCeenffoZ4d4Cna7TZdkUsfdK1HNmoB46fo9jK5ENQwnWdPmZBnZ4h8uDxHpQF74rs3wPcpmch6Byu31och1cyz8JxgXkacHpTrGeAN2bEhRp8kDQpmPtj9QqaAgxTbam9hoB4mvtrRmRx5GnzzZoWW5qDxwMvgKCYWiLwtLcvjDZPNdHGbvFspFeCq7kBcTeyrjYeHxuwwwM1GpdwMdxzNiFK1jYkA4DUZRohuKxeyhBFiY9HuwD6zKf9nZMThoYwTGhAJR2d3GqVqXGsivAKLs1oBzrmH9V6vaMwAjM7Hu69TLfKHtZUThoiEDftxPJdraNxoQps3mFamNbT1U3kRdpAz5s5kq6i2jLBUjBjAdV9N8jWNqx4RgiaHTW5qqb8E6JvHgQyrVkLmMdsjoLAWaWZLRw2pQpBJehRsx1LU6wmAC1nfeLbdQxPmytaMUURBDhHVqPNxwThCzZsnA9RuKrYWGsmyTxCzVUEjvUXaU4hkoV62qn7G1TnVRiADNhRfMnxm8R2ZoSPxEhVaFyHvLweq
```

* Base64 encoding was a dead end. Apparently it did successfully decode though. [ Lesson --> try all types of base decoding that works! ]

* Base58 it is! --> Wiki about satoshi invention for use with Bitcoin --> https://en.wikipedia.org/wiki/Base58

* Decode base58

```
elevator lolwat
  action main
    show 114
    show 116
    show 99
    show 112
    show 123
    show 78
    show 111
    show 116
    show 32
    show 113
    show 117
    show 105
    show 116
    show 101
    show 32
    show 110
    show 111
    show 114
    show 109
    show 97
    show 108
    show 32
    show 115
    show 116
    show 101
    show 103
    show 111
    show 95
    show 52
    show 120
    show 98
    show 98
    show 52
    show 53
    show 103
    show 121
    show 116
    show 106
    show 125
  end action
  action show num
    floor num
    outFloor
  end action
end elevator
```

* Convert the integer to character representation

```
>>> flag = ""

>>> elevator
'\n    show 114\n    show 116\n    show 99\n    show 112\n    show 123\n    show 78\n    show 111\n    show 116\n    show 32\n    show 113\n    show 117\n    show 105\n    show 116\n    show 101\n    show 32\n    show 110\n    show 111\n    show 114\n    show 109\n    show 97\n    show 108\n    show 32\n    show 115\n    show 116\n    show 101\n    show 103\n    show 111\n    show 95\n    show 52\n    show 120\n    show 98\n    show 98\n    show 52\n    show 53\n    show 103\n    show 121\n    show 116\n    show 106\n    show 125\n'

>>> elevator = elevator.split("\n")

>>> elevator
['', '    show 114', '    show 116', '    show 99', '    show 112', '    show 123', '    show 78', '    show 111', '    show 116', '    show 32', '    show 113', '    show 117', '    show 105', '    show 116', '    show 101', '    show 32', '    show 110', '    show 111', '    show 114', '    show 109', '    show 97', '    show 108', '    show 32', '    show 115', '    show 116', '    show 101', '    show 103', '    show 111', '    show 95', '    show 52', '    show 120', '    show 98', '    show 98', '    show 52', '    show 53', '    show 103', '    show 121', '    show 116', '    show 106', '    show 125', '']

>>> for e in elevator:
...   e = e.strip()
...   e = e.strip("show")
...   e = e.strip()
...   if e:
...     flag += chr(int(e))
... 

>>> flag
'rtcp{Not quite normal stego_4xbb45gytj}'

>>> 
```