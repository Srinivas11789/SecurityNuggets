### Challenge

```
A geopolitical activity that is pursued through economic and political actions, propaganda, acts of espionage or proxy wars and without direct military action is known as a Cold War. This type of war does not refer to conflict of seasons, but this challenge might.
```

### Recon
* There looks like some white space below the paragraph from looking it with text editor
* White space stegano --> stegsnow

### Solve
```
kali@kali:~$ sudo apt install stegsnow^C

kali@kali:~$ stegsnow --help
Usage: stegsnow [-C] [-Q] [-S] [-V | --version] [-h | --help]
        [-p passwd] [-l line-len] [-f file | -m message]
        [infile [outfile]]

kali@kali:~$ stegsnow -C cold_war.txt 
flag{do_not_use_merriam_webster}

kali@kali:~$ 
```