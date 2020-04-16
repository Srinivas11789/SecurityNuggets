### Challenge

```
Game Of Keys

Download this file and get the flag. You will also need this wordlist
```

### Recon
* First step, `.pyc --> .py`
* Used `uncompyle6` based on previous encounter, does not work for `py3.7`
* Trying different decompilers
  * https://github.com/rocky/python-decompile3
  * https://github.com/figment/unpyc3
  * https://pypi.org/project/uncompyle6/

### Solve
```
kali@kali:~/gameOfKeys$ wget https://storage.googleapis.com/tghack-public/2020/32314e6d7337d592670c9d23a9a1c9e3/keygame.pyc
--2020-04-16 00:04:49--  https://storage.googleapis.com/tghack-public/2020/32314e6d7337d592670c9d23a9a1c9e3/keygame.pyc
Resolving storage.googleapis.com (storage.googleapis.com)... 108.177.98.128, 2607:f8b0:400e:c06::80
Connecting to storage.googleapis.com (storage.googleapis.com)|108.177.98.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1790 (1.7K) [application/x-python-code]
Saving to: ‘keygame.pyc’

keygame.pyc                        100%[==============================================================>]   1.75K  --.-KB/s    in 0.001s  

2020-04-16 00:04:50 (3.39 MB/s) - ‘keygame.pyc’ saved [1790/1790]

kali@kali:~/gameOfKeys$ wget https://storage.googleapis.com/tghack-public/2020/32314e6d7337d592670c9d23a9a1c9e3/wordlist.txt
--2020-04-16 00:04:56--  https://storage.googleapis.com/tghack-public/2020/32314e6d7337d592670c9d23a9a1c9e3/wordlist.txt
Resolving storage.googleapis.com (storage.googleapis.com)... 108.177.98.128, 2607:f8b0:400e:c06::80
Connecting to storage.googleapis.com (storage.googleapis.com)|108.177.98.128|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 878800 (858K) [text/plain]
Saving to: ‘wordlist.txt’

wordlist.txt                       100%[==============================================================>] 858.20K  --.-KB/s    in 0.07s   

2020-04-16 00:04:57 (11.6 MB/s) - ‘wordlist.txt’ saved [878800/878800]

kali@kali:~/gameOfKeys$ pip3 install decompyle3
Requirement already satisfied: decompyle3 in /home/kali/python-decompile3 (3.3.2)
Requirement already satisfied: spark-parser<1.9.0,>=1.8.9 in /home/kali/.local/lib/python3.7/site-packages (from decompyle3) (1.8.9)
Requirement already satisfied: xdis<4.3.0,>=4.2.4 in /home/kali/.local/lib/python3.7/site-packages (from decompyle3) (4.2.4)
Requirement already satisfied: click in /usr/lib/python3/dist-packages (from spark-parser<1.9.0,>=1.8.9->decompyle3) (7.0)
kali@kali:~/gameOfKeys$ decompyle3 keygame.pyc 
# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.6 (default, Dec 19 2019, 09:25:23) 
# [GCC 9.2.1 20191130]
# Embedded file name: keygame.py
# Size of source mod 2**32: 1496 bytes
import base64
from itertools import cycle

class myGame:

    def __init__(self, xdim=4, ydim=4):
        self.x = xdim
        self.y = ydim
        self.matrix = []
        for i in range(self.x):
            row = []
            for j in range(self.y):
                row.append(0)

            self.matrix.append(row)

    def make_keys(self, *args, **kwargs):
        words = []
        with open('wordlist.txt') as f:
            for line in f:
                words.append(line.strip())

            for i in range(self.x):
                for j in range(self.y):
                    self.matrix[j][i] = words[(i + j)]

        keyArray = []
        keyArray.append(self.matrix[args[0]][args[1]])
        keyArray.append(self.matrix[args[2]][args[3]])
        key = ''
        for k in keyArray:
            key = key.strip() + str(k).strip()

        print(key)
        return key

    def checkdata(self, key):
        f = base64.b64decode(b'NSYDUhoVWQ8SQVcOAAYRFQkORA4FQVMDQQ5fQhUEWUYMDl4MHA==')
        data = f.decode('ascii')
        c = ''.join((chr(ord(c) ^ ord(k)) for c, k in zip(data, cycle(key))))
        print('%s ^ %s = %s' % (data, key, c))


if __name__ == '__main__':
    mgame = myGame(25, 25)
    x = input('input a number: ')
    y = input('input a number: ')
    x1 = input('input a number: ')
    y1 = input('input a number: ')
    data = mgame.make_keys(int(x), int(y), int(x1), int(y1))
    mgame.checkdata(data)
# okay decompiling keygame.pyc
kali@kali:~/gameOfKeys$ 
kali@kali:~/gameOfKeys$ decompyle3 keygame.pyc > keygame.py
kali@kali:~/gameOfKeys$ cp keygame.py keygamebruteforce.py
kali@kali:~/gameOfKeys$ vi keygamebruteforce.py 
kali@kali:~/gameOfKeys$ python3 keygamebruteforce.py 
input a number: 1
input a number: 2
input a number: 3
input a number: 4
aa0aaa0a
aa0aaa0b
aa0aaa0c
aa0aaa0d
```

* Brute force script
```
    def checkdata(self, key):
        f = base64.b64decode(b'NSYDUhoVWQ8SQVcOAAYRFQkORA4FQVMDQQ5fQhUEWUYMDl4MHA==')
        data = f.decode('ascii')
        c = ''.join((chr(ord(c) ^ ord(k)) for c, k in zip(data, cycle(key))))
        if "TG20" in c:
          print('%s ^ %s = %s' % (data, key, c))


if __name__ == '__main__':
    mgame = myGame(25, 25)
    x = input('input a number: ')
    y = input('input a number: ')
    x1 = input('input a number: ')
    y1 = input('input a number: ')
    for x in range(25):
      for y in range(25):
        for x1 in range(25):
          for y1 in range(25):
            data = mgame.make_keys(int(x), int(y), int(x1), int(y1))
            mgame.checkdata(data)
# okay decompiling keygame.pyc
```

### Flag
> ✓ The planets are aligned, you won!
  TG20{this flag should be on teh moon}