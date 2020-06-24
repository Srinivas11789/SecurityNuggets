### Challenge
```
This bash script evaluates to echo dont just run it, dummy # flag{...} where the flag is in the comments.

The comment won't be visible if you just execute the script. How can you mess with bash to get the value right before it executes?

Enjoy the intro misc chal.
```

### Recon
* Assuming this was obfuscated with `bashfuscator` --> https://github.com/Bashfuscator/Bashfuscator

### Solve

```
kali@kali:~$ bash -x ctfBash.sh 2> output.txt
bash -x ctfBash.sh 2> output.txt
echo "# $BASH_COMMAND"
# bash -x ctfBash.sh 2> output.txt
dont just run it, dummy


kali@kali:~$ python revBash.py
python revBash.py
echo "# $BASH_COMMAND"
# python revBash.py
echodontjustrunitdummy#flag{us3_zsh,_dummy}


kali@kali:~$ cat revBash.py
cat revBash.py
echo "# $BASH_COMMAND"
# cat revBash.py
f = open('output.txt', 'r')
content = f.readlines()
flag= ""
for c in content:
    c = c.strip()
    if "printf" in c:
        c = c.split(" ")
        #print(c, c[-1].strip("'"),)
        flag += c[-1].strip("'")
print(flag)
kali@kali:~$ 

```