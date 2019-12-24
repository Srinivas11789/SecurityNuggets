# Smelly Onion

### Challenge
```
I cry when I cut onions.
Given a "rar" file.
```

### Recon + Explore + Hits

* Initially starting with a `rar` file --> we get a zip file. From here on manually continuing unzipping the files returns a new file which is again an empty file. 
* One interesting fact is that every file obtained from unzipping is a `NUMBER`
* Automating this process in Python --> we ultimaltely end at a empty zip file. So we record all the file name which appear to be numbers.
* Converting this number from ord() to chr() does not help. We get garbage! --> `P>5$^-L@1LaP%[RN+^bU>NPaC4`
* Looking for more hints --> Question says `CRY` --> searching around google --> Cryptography, Scream cipher --> Maybe it just implied Cryptography?
* Looking further into the zipfiles with `binwalk, zipinfo, unzip -v`, one another thing is we find another set of hex digits as COMMENTS in each of those files. So repeat the same logic to fetch all the comments will give the flag

```
srimbp-623:ans sri$ binwalk 80

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             Zip archive data, at least v2.0 to extract, compressed size: 3244, uncompressed size: 3239, name: 62
3252          0xCB4           End of Zip archive, comment: "46"
3324          0xCFC           End of Zip archive, comment: "41"

srimbp-623:ans sri$ unzip -v 80
Archive:  80
41
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
    3239  Defl:N     3244  -0% 11-29-2019 22:29 e18137e7  62
--------          -------  ---                            -------
    3239             3244  -0%                            1 file

```

* Solve

```
srimbp-623:smellyOnion sri$ python exhack.py 
['onion', '80', '62', '53', '29', '36', '94', '45', '76', '23', '64', '49', '76', '7', '97', '19', '7', '80', '2', '37', '91', '82', '18', '78', '29', '43', '94', '98', '85', '16', '62', '23', '78', '80', '97', '5', '2', '67', '52', '66', '41']
onion 80 62 53 29 36 94 45 76 23 64 49 76 7 97 19 7 80 2 37 91 82 18 78 29 43 94 98 85 16 62 23 78 80 97 5 2 67 52 66 41 onionP>5$^-L@1LaP%[RN+^bU>NPaC4B)
A F { 2 1 P _ P H 1 L 3 2 _ R _ A W 3 S 0 M 3 _ D 0 N T _ Y 0 U _ T H 1 N K }  Done
srimbp-623:smellyOnion sri$ python
Python 2.7.15 (default, Jan 12 2019, 21:07:57) 
[GCC 4.2.1 Compatible Apple LLVM 10.0.0 (clang-1000.11.45.5)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> s = "K A F { 2 1 P _ P H 1 L 3 2 _ R _ A W 3 S 0 M 3 _ D 0 N T _ Y 0 U _ T H 1 N K }"
>>> list(s)
['K', ' ', 'A', ' ', 'F', ' ', '{', ' ', '2', ' ', '1', ' ', 'P', ' ', '_', ' ', 'P', ' ', 'H', ' ', '1', ' ', 'L', ' ', '3', ' ', '2', ' ', '_', ' ', 'R', ' ', '_', ' ', 'A', ' ', 'W', ' ', '3', ' ', 'S', ' ', '0', ' ', 'M', ' ', '3', ' ', '_', ' ', 'D', ' ', '0', ' ', 'N', ' ', 'T', ' ', '_', ' ', 'Y', ' ', '0', ' ', 'U', ' ', '_', ' ', 'T', ' ', 'H', ' ', '1', ' ', 'N', ' ', 'K', ' ', '}']
>>> "".join(list(s))
'K A F { 2 1 P _ P H 1 L 3 2 _ R _ A W 3 S 0 M 3 _ D 0 N T _ Y 0 U _ T H 1 N K }'
>>> c = []
>>> for i in s:
...     if i:
...       c.append(i)
... 
>>> c
['K', ' ', 'A', ' ', 'F', ' ', '{', ' ', '2', ' ', '1', ' ', 'P', ' ', '_', ' ', 'P', ' ', 'H', ' ', '1', ' ', 'L', ' ', '3', ' ', '2', ' ', '_', ' ', 'R', ' ', '_', ' ', 'A', ' ', 'W', ' ', '3', ' ', 'S', ' ', '0', ' ', 'M', ' ', '3', ' ', '_', ' ', 'D', ' ', '0', ' ', 'N', ' ', 'T', ' ', '_', ' ', 'Y', ' ', '0', ' ', 'U', ' ', '_', ' ', 'T', ' ', 'H', ' ', '1', ' ', 'N', ' ', 'K', ' ', '}']
>>> for i in s:
...     if i != " ":
...       c.append(i)
... 
>>> c
['K', ' ', 'A', ' ', 'F', ' ', '{', ' ', '2', ' ', '1', ' ', 'P', ' ', '_', ' ', 'P', ' ', 'H', ' ', '1', ' ', 'L', ' ', '3', ' ', '2', ' ', '_', ' ', 'R', ' ', '_', ' ', 'A', ' ', 'W', ' ', '3', ' ', 'S', ' ', '0', ' ', 'M', ' ', '3', ' ', '_', ' ', 'D', ' ', '0', ' ', 'N', ' ', 'T', ' ', '_', ' ', 'Y', ' ', '0', ' ', 'U', ' ', '_', ' ', 'T', ' ', 'H', ' ', '1', ' ', 'N', ' ', 'K', ' ', '}', 'K', 'A', 'F', '{', '2', '1', 'P', '_', 'P', 'H', '1', 'L', '3', '2', '_', 'R', '_', 'A', 'W', '3', 'S', '0', 'M', '3', '_', 'D', '0', 'N', 'T', '_', 'Y', '0', 'U', '_', 'T', 'H', '1', 'N', 'K', '}']
>>> c = []
>>> for i in s:
...     if i != " ":
...       c.append(i)
... 
>>> c
['K', 'A', 'F', '{', '2', '1', 'P', '_', 'P', 'H', '1', 'L', '3', '2', '_', 'R', '_', 'A', 'W', '3', 'S', '0', 'M', '3', '_', 'D', '0', 'N', 'T', '_', 'Y', '0', 'U', '_', 'T', 'H', '1', 'N', 'K', '}']
>>> "".join(list(c))
'KAF{21P_PH1L32_R_AW3S0M3_D0NT_Y0U_TH1NK}'
```
### 