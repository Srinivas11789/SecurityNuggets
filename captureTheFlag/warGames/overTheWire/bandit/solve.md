# Bandit Solves

* Stage 0

```
bandit0@bandit:~$ cat readme 
boJ9jbbUNNfktd78OOpsqOltutMc3MY1
```

* Stage 1

```
bandit1@bandit:~$ cat ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
bandit1@bandit:~$ strings ./-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9
bandit1@bandit:~$ file ./-
./-: ASCII text
bandit1@bandit:~$ 
```

* Stage 2

```
bandit2@bandit:~$ cat spaces\ in\ this\ filename 
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK
```

* Stage 3

```
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -ltr
total 0
bandit3@bandit:~/inhere$ ls -la
total 12
drwxr-xr-x 2 root    root    4096 Oct 16  2018 .
drwxr-xr-x 3 root    root    4096 Oct 16  2018 ..
-rw-r----- 1 bandit4 bandit3   33 Oct 16  2018 .hidden
bandit3@bandit:~/inhere$ cat .hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB
bandit3@bandit:~/inhere$ 
```

* Stage 4

```
bandit4@bandit:~$ ls
inhere
bandit4@bandit:~$ cd inhere/
bandit4@bandit:~/inhere$ ls
-file00  -file01  -file02  -file03  -file04  -file05  -file06  -file07  -file08  -file09
bandit4@bandit:~/inhere$ cat -file0
cat: invalid option -- 'f'
Try 'cat --help' for more information.
bandit4@bandit:~/inhere$ cat ./-file0
cat: ./-file0: No such file or directory
bandit4@bandit:~/inhere$ cat ./-file00
??????????~%	C[?걱>??| ?bandit4@bandit:~/inhere$ 
bandit4@bandit:~/inhere$ cat ./-file01
???U"7?w???H??ê?Q??(???#???bandit4@bandit:~/inhere$ cat ./-file02
?T?v??(?ִ?????A*?
2J?Ş؇_?y7bandit4@bandit:~/inhere$ cat ./-file03
?.A??u??#???w$N?c?-??Db3??=??bandit4@bandit:~/inhere$ cat ./-file04
?=<?W?????ht?Z??!??{?U
                      ?bandit4@bandit:~/inhere$ cat ./-file05
+??pm???;??:D??^??@?gl?Q?bandit4@bandit:~/inhere$ cat ./-file06
??@?%@???ZP*E??1?V???̫*????bandit4@bandit:~/inhere$ cat ./-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
bandit4@bandit:~/inhere$ cat ./-file09
N?{??Y?d4????]3?????9(?
Q???bandit4@bandit:~/inhere$ file ./-file09
./-file09: data
bandit4@bandit:~/inhere$ file ./-file07
./-file07: ASCII text
bandit4@bandit:~/inhere$ 
```

* Stage 5

```
bandit5@bandit:~$ ls
inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere03  maybehere06  maybehere09  maybehere12  maybehere15  maybehere18
maybehere01  maybehere04  maybehere07  maybehere10  maybehere13  maybehere16  maybehere19
maybehere02  maybehere05  maybehere08  maybehere11  maybehere14  maybehere17
bandit5@bandit:~/inhere$ strings *
bandit5@bandit:~/inhere$ cd maybehere
-bash: cd: maybehere: No such file or directory
bandit5@bandit:~/inhere$ cd maybehere00
bandit5@bandit:~/inhere/maybehere00$ ls
-file1  -file2  -file3  spaces file1  spaces file2  spaces file3
bandit5@bandit:~/inhere/maybehere00$ cat spaces\ file
cat: 'spaces file': No such file or directory
bandit5@bandit:~/inhere/maybehere00$ cat spaces\ file1
```

* Stage 6