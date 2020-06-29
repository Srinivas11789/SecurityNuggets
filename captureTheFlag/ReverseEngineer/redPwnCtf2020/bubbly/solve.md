### Challenge
```
rev/bubbly
dns

It never ends

nc 2020.redpwnc.tf 31039
```

### Recon
* Decompiling the binary in IDA, it was running a loop to check before it gives the flag
* Decompiling it in GHIDRA made it much easier with code generation, code browser clearly shows this important loop in main.c
```
  while( true ) {
    __isoc99_scanf(&DAT_00102058);
    if (8 < i) break;
    nums[i] = nums[i] ^ nums[i + 1];
    nums[i + 1] = nums[i + 1] ^ nums[i];
    nums[i] = nums[i] ^ nums[i + 1];
    pass = check();
  }
```
* The exor logic here is swapping 2 elements of array
```
>>> a = [1, 2]
>>> a[0] = a[0]^a[1]
>>> a
[3, 2]
>>> a[1] = a[1] ^ a[0]
>>> a
[3, 1]
>>> a[0] = a[0]^a[1]
>>> a
[2, 1]
```
* The check function that returns is as follows
```
_Bool check(void)

{
  uint32_t i;
  _Bool pass;
  
  i = 0;
  while( true ) {
    if (8 < i) {
      return true;
    }
    if (nums[i + 1] < nums[i]) break;
    i = i + 1;
  }
  return false;
}
```

* The nums array shows numbers with hex representation
```
[1, 10, 3, 2, 5, 9, 8, 7, 4, 6]
```
* Now the challenge name becomes evident, its performing bubble sorting ( swapping 2 elements at each step )
* We need to provide index i < 8 (corresponding to the size 8 of the array) --> this would swap at the resp index.
* So the input should be --> `1 2 3 4 5 6 7 8 1 4 5 4 6 5 4 3 7 6 5` to get it completely sorted and last give a value > 8 to exit with true

### Solve

```
kali@kali:~$ ./bubbly 
I hate my data structures class! Why can't I just sort by hand?
1
2
3
4
5
6
7
8
1
4
5
4
6
5
4
3
7
6
5
9
Well done!
cat: flag.txt: No such file or directory
```

* Solved this after the ctf, so ran only in local. Referring to some writeups confirmed I was going on the right path.

### Reference
* https://www.prepressure.com/library/technology/ascii-binary-hex
* https://ctftime.org/task/12097