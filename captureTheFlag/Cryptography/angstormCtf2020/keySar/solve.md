### Challenge

```
Hey! My friend sent me a message... He said encrypted it with the key ANGSTROMCTF.

He mumbled what cipher he used, but I think I have a clue.

Gotta go though, I have history homework!!

agqr{yue_stdcgciup_padas}
```

### Recon
* Thinking through some ciphers...
```
- Simple XOR ( Repeating Key )
- Substitution ciphers
- Block ciphers? ECB
```

* Rethinking...
  - The cipher text shared looks very similar to the flag - so there should have not been too much mixing so it should be caesar or poly alphabetic substitution
  - After a while of look out I did check out the HINT to find out that it is KEYED CAESAR so the name KEYSAR
  - KEYED CAESAR is including a key in the alphabet range and removing duplicates, otherwise the range(key, alphabet not containing any overlap with kay) with ROT is the answer.

### Solve

```
Srinivass-MacBook-Pro:keySar darkknight$ python exploit.py 
('angstromcf', ['b', 'd', 'e', 'h', 'i', 'j', 'k', 'l', 'p', 'q', 'u', 'v', 'w', 'x', 'y', 'z'], ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
Using cipher angstromcfbdehijklpquvwxyz
(0, 'a', 'a')
(2, 'c', 'g')
(19, 't', 'q')
(5, 'f', 'r')
(24, 'y', 'y')
(20, 'u', 'u')
(12, 'm', 'e')
(3, 'd', 's')
(4, 'e', 't')
(11, 'l', 'd')
(8, 'i', 'c')
(2, 'c', 'g')
(8, 'i', 'c')
(14, 'o', 'i')
(20, 'u', 'u')
(18, 's', 'p')
(18, 's', 'p')
(0, 'a', 'a')
(11, 'l', 'd')
(0, 'a', 'a')
(3, 'd', 's')
actf{yum_delicious_salad}
Srinivass-MacBook-Pro:keySar darkknight$ 
```

