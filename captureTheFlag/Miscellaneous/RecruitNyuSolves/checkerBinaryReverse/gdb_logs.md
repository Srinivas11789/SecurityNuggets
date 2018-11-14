6.1: icmp_seq=3 ttl=64 time=0.507 ms
64 bytes from 10.10.66.1: icmp_seq=4 ttl=64 time=0.498 ms
64 bytes from 10.10.66.1: icmp_seq=5 ttl=64 time=0.488 ms
64 bytes from 10.10.66.1: icmp_seq=6 ttl=64 time=0.224 ms
64 bytes from 10.10.66.1: icmp_seq=7 ttl=64 time=0.489 ms
64 bytes from 10.10.66.1: icmp_seq=8 ttl=64 time=0.358 ms
64 bytes from 10.10.66.1: icmp_seq=9 ttl=64 time=0.198 ms
^C
--- 10.10.66.1 ping statistics ---
9 packets transmitted, 9 received, 0% packet loss, time 7997ms
rtt min/avg/max/mdev = 0.198/0.365/0.507/0.125 ms
root@kali:~# ls
Desktop    google-chrome-stable_current_amd64.deb  output    Templates
Documents  live-build-config                       Pictures  Videos
Downloads  Music                                   Public
root@kali:~# cd ../
root@kali:/# ls
0     dev   initrd.img      lib    lost+found  opt   run   sys  var
bin   etc   initrd.img.old  lib32  media       proc  sbin  tmp  vmlinuz
boot  home  kali            lib64  mnt         root  srv   usr  vmlinuz.old
root@kali:/# cd kali/
root@kali:/kali# ls
checker  click_coordinates.txt  playmeout.txt
root@kali:/kali# gdb ./checker
GNU gdb (Debian 7.11.1-2) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./checker...(no debugging symbols found)...done.
(gdb) disas main
Dump of assembler code for function main:
   0x0804871a <+0>:	lea    0x4(%esp),%ecx
   0x0804871e <+4>:	and    $0xfffffff0,%esp
   0x08048721 <+7>:	pushl  -0x4(%ecx)
   0x08048724 <+10>:	push   %ebp
   0x08048725 <+11>:	mov    %esp,%ebp
   0x08048727 <+13>:	push   %ecx
   0x08048728 <+14>:	sub    $0x34,%esp
   0x0804872b <+17>:	mov    %gs:0x14,%eax
   0x08048731 <+23>:	mov    %eax,-0xc(%ebp)
   0x08048734 <+26>:	xor    %eax,%eax
   0x08048736 <+28>:	call   0x80485bb <init>
   0x0804873b <+33>:	sub    $0xc,%esp
   0x0804873e <+36>:	push   $0x8048940
   0x08048743 <+41>:	call   0x8048450 <puts@plt>
   0x08048748 <+46>:	add    $0x10,%esp
   0x0804874b <+49>:	mov    0x804a040,%eax
   0x08048750 <+54>:	sub    $0x4,%esp
   0x08048753 <+57>:	push   %eax
   0x08048754 <+58>:	push   $0x1f
   0x08048756 <+60>:	lea    -0x2c(%ebp),%eax
   0x08048759 <+63>:	push   %eax
   0x0804875a <+64>:	call   0x8048430 <fgets@plt>
---Type <return> to continue, or q <return> to quit--- 
   0x0804875f <+69>:	add    $0x10,%esp
   0x08048762 <+72>:	sub    $0x8,%esp
   0x08048765 <+75>:	push   $0xa
   0x08048767 <+77>:	lea    -0x2c(%ebp),%eax
   0x0804876a <+80>:	push   %eax
   0x0804876b <+81>:	call   0x8048460 <strchr@plt>
   0x08048770 <+86>:	add    $0x10,%esp
   0x08048773 <+89>:	mov    %eax,-0x30(%ebp)
   0x08048776 <+92>:	cmpl   $0x0,-0x30(%ebp)
   0x0804877a <+96>:	je     0x8048782 <main+104>
   0x0804877c <+98>:	mov    -0x30(%ebp),%eax
   0x0804877f <+101>:	movb   $0x0,(%eax)
   0x08048782 <+104>:	sub    $0xc,%esp
   0x08048785 <+107>:	lea    -0x2c(%ebp),%eax
   0x08048788 <+110>:	push   %eax
   0x08048789 <+111>:	call   0x8048661 <check>
   0x0804878e <+116>:	add    $0x10,%esp
   0x08048791 <+119>:	test   %al,%al
   0x08048793 <+121>:	je     0x804879c <main+130>
   0x08048795 <+123>:	call   0x80485d8 <give_flag>
   0x0804879a <+128>:	jmp    0x80487ac <main+146>
   0x0804879c <+130>:	sub    $0xc,%esp
   0x0804879f <+133>:	push   $0x8048960
---Type <return> to continue, or q <return> to quit---
   0x080487a4 <+138>:	call   0x8048450 <puts@plt>
   0x080487a9 <+143>:	add    $0x10,%esp
   0x080487ac <+146>:	mov    $0x0,%eax
   0x080487b1 <+151>:	mov    -0xc(%ebp),%edx
   0x080487b4 <+154>:	xor    %gs:0x14,%edx
   0x080487bb <+161>:	je     0x80487c2 <main+168>
   0x080487bd <+163>:	call   0x8048440 <__stack_chk_fail@plt>
   0x080487c2 <+168>:	mov    -0x4(%ebp),%ecx
   0x080487c5 <+171>:	leave  
   0x080487c6 <+172>:	lea    -0x4(%ecx),%esp
   0x080487c9 <+175>:	ret    
End of assembler dump.
(gdb) break 0x08048788
Function "0x08048788" not defined.
Make breakpoint pending on future shared library load? (y or [n]) yQuit
(gdb) break 0x08048788
Function "0x08048788" not defined.
Make breakpoint pending on future shared library load? (y or [n]) uy
Please answer y or [n].
Make breakpoint pending on future shared library load? (y or [n]) n
(gdb) 
Function "0x08048788" not defined.
Make breakpoint pending on future shared library load? (y or [n]) n
(gdb) disas main
Dump of assembler code for function main:
   0x0804871a <+0>:	lea    0x4(%esp),%ecx
   0x0804871e <+4>:	and    $0xfffffff0,%esp
   0x08048721 <+7>:	pushl  -0x4(%ecx)
   0x08048724 <+10>:	push   %ebp
   0x08048725 <+11>:	mov    %esp,%ebp
   0x08048727 <+13>:	push   %ecx
   0x08048728 <+14>:	sub    $0x34,%esp
   0x0804872b <+17>:	mov    %gs:0x14,%eax
   0x08048731 <+23>:	mov    %eax,-0xc(%ebp)
   0x08048734 <+26>:	xor    %eax,%eax
   0x08048736 <+28>:	call   0x80485bb <init>
   0x0804873b <+33>:	sub    $0xc,%esp
   0x0804873e <+36>:	push   $0x8048940
   0x08048743 <+41>:	call   0x8048450 <puts@plt>
   0x08048748 <+46>:	add    $0x10,%esp
   0x0804874b <+49>:	mov    0x804a040,%eax
   0x08048750 <+54>:	sub    $0x4,%esp
   0x08048753 <+57>:	push   %eax
   0x08048754 <+58>:	push   $0x1f
   0x08048756 <+60>:	lea    -0x2c(%ebp),%eax
   0x08048759 <+63>:	push   %eax
   0x0804875a <+64>:	call   0x8048430 <fgets@plt>
   0x0804875f <+69>:	add    $0x10,%esp
   0x08048762 <+72>:	sub    $0x8,%esp
   0x08048765 <+75>:	push   $0xa
   0x08048767 <+77>:	lea    -0x2c(%ebp),%eax
   0x0804876a <+80>:	push   %eax
   0x0804876b <+81>:	call   0x8048460 <strchr@plt>
   0x08048770 <+86>:	add    $0x10,%esp
   0x08048773 <+89>:	mov    %eax,-0x30(%ebp)
   0x08048776 <+92>:	cmpl   $0x0,-0x30(%ebp)
   0x0804877a <+96>:	je     0x8048782 <main+104>
   0x0804877c <+98>:	mov    -0x30(%ebp),%eax
---Type <return> to continue, or q <return> to quit--- 
   0x0804877f <+101>:	movb   $0x0,(%eax)
   0x08048782 <+104>:	sub    $0xc,%esp
   0x08048785 <+107>:	lea    -0x2c(%ebp),%eax
   0x08048788 <+110>:	push   %eax
   0x08048789 <+111>:	call   0x8048661 <check>
   0x0804878e <+116>:	add    $0x10,%esp
   0x08048791 <+119>:	test   %al,%al
   0x08048793 <+121>:	je     0x804879c <main+130>
   0x08048795 <+123>:	call   0x80485d8 <give_flag>
   0x0804879a <+128>:	jmp    0x80487ac <main+146>
   0x0804879c <+130>:	sub    $0xc,%esp
   0x0804879f <+133>:	push   $0x8048960
   0x080487a4 <+138>:	call   0x8048450 <puts@plt>
   0x080487a9 <+143>:	add    $0x10,%esp
   0x080487ac <+146>:	mov    $0x0,%eax
   0x080487b1 <+151>:	mov    -0xc(%ebp),%edx
   0x080487b4 <+154>:	xor    %gs:0x14,%edx
   0x080487bb <+161>:	je     0x80487c2 <main+168>
   0x080487bd <+163>:	call   0x8048440 <__stack_chk_fail@plt>
   0x080487c2 <+168>:	mov    -0x4(%ebp),%ecx
   0x080487c5 <+171>:	leave  
   0x080487c6 <+172>:	lea    -0x4(%ecx),%esp
   0x080487c9 <+175>:	ret    
End of assembler dump.
(gdb) 
(gdb) 
(gdb) break 
No default breakpoint address now.
(gdb) break 0x080487c5
Function "0x080487c5" not defined.
Make breakpoint pending on future shared library load? (y or [n]) n
(gdb) i
[1]+  Stopped                 gdb ./checker
root@kali:/kali# ^C
root@kali:/kali# python -c "for i in range(100): print i"
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
root@kali:/kali# python -c "for i in range(100): print i" | ./chex^C
root@kali:/kali# ls
bombSpring10  checker  click_coordinates.txt  playmeout.txt
root@kali:/kali# chmod 777 checker 
root@kali:/kali# python -c "for i in range(100): print i" | ./checker 
Tell me something interesting:
That doesn't look right! Go reverse some more!
root@kali:/kali# python -c "for i in range(1000): print i" | ./checker 
Tell me something interesting:
That doesn't look right! Go reverse some more!
root@kali:/kali# python -c "for i in range(10000): print i" | ./checker 
Tell me something interesting:
That doesn't look right! Go reverse some more!
Traceback (most recent call last):
  File "<string>", line 1, in <module>
IOError: [Errno 32] Broken pipe
root@kali:/kali# ./checker 
Tell me something interesting:
aqua
That doesn't look right! Go reverse some more!
root@kali:/kali# ./checker 
Tell me something interesting:
aquapqrstuwxyz12345
That doesn't look right! Go reverse some more!
root@kali:/kali# ./checker 
Tell me something interesting:
aquaaquaaaauqaauqa
That doesn't look right! Go reverse some more!
root@kali:/kali# ./checker 
Tell me something interesting:
aquaaquaaaauqaauqa
That doesn't look right! Go reverse some more!
root@kali:/kali# ./checker 
Tell me something interesting:
aquaaquaauqaauqa
That doesn't look right! Go reverse some more!
root@kali:/kali# 
root@kali:/kali# 
root@kali:/kali# 
root@kali:/kali# gdb ./checker 
GNU gdb (Debian 7.11.1-2) 7.11.1
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
and "show warranty" for details.
This GDB was configured as "x86_64-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
<http://www.gnu.org/software/gdb/documentation/>.
For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./checker...(no debugging symbols found)...done.
(gdb) 
(gdb) 
(gdb) disass main
Dump of assembler code for function main:
   0x0804871a <+0>:	lea    0x4(%esp),%ecx
   0x0804871e <+4>:	and    $0xfffffff0,%esp
   0x08048721 <+7>:	pushl  -0x4(%ecx)
   0x08048724 <+10>:	push   %ebp
   0x08048725 <+11>:	mov    %esp,%ebp
   0x08048727 <+13>:	push   %ecx
   0x08048728 <+14>:	sub    $0x34,%esp
   0x0804872b <+17>:	mov    %gs:0x14,%eax
   0x08048731 <+23>:	mov    %eax,-0xc(%ebp)
   0x08048734 <+26>:	xor    %eax,%eax
   0x08048736 <+28>:	call   0x80485bb <init>
   0x0804873b <+33>:	sub    $0xc,%esp
   0x0804873e <+36>:	push   $0x8048940
   0x08048743 <+41>:	call   0x8048450 <puts@plt>
   0x08048748 <+46>:	add    $0x10,%esp
   0x0804874b <+49>:	mov    0x804a040,%eax
   0x08048750 <+54>:	sub    $0x4,%esp
   0x08048753 <+57>:	push   %eax
   0x08048754 <+58>:	push   $0x1f
   0x08048756 <+60>:	lea    -0x2c(%ebp),%eax
   0x08048759 <+63>:	push   %eax
   0x0804875a <+64>:	call   0x8048430 <fgets@plt>
   0x0804875f <+69>:	add    $0x10,%esp
   0x08048762 <+72>:	sub    $0x8,%esp
   0x08048765 <+75>:	push   $0xa
   0x08048767 <+77>:	lea    -0x2c(%ebp),%eax
   0x0804876a <+80>:	push   %eax
   0x0804876b <+81>:	call   0x8048460 <strchr@plt>
   0x08048770 <+86>:	add    $0x10,%esp
   0x08048773 <+89>:	mov    %eax,-0x30(%ebp)
   0x08048776 <+92>:	cmpl   $0x0,-0x30(%ebp)
   0x0804877a <+96>:	je     0x8048782 <main+104>
   0x0804877c <+98>:	mov    -0x30(%ebp),%eax
   0x0804877f <+101>:	movb   $0x0,(%eax)
   0x08048782 <+104>:	sub    $0xc,%esp
   0x08048785 <+107>:	lea    -0x2c(%ebp),%eax
---Type <return> to continue, or q <return> to quit--- 
   0x08048788 <+110>:	push   %eax
   0x08048789 <+111>:	call   0x8048661 <check>
   0x0804878e <+116>:	add    $0x10,%esp
   0x08048791 <+119>:	test   %al,%al
   0x08048793 <+121>:	je     0x804879c <main+130>
   0x08048795 <+123>:	call   0x80485d8 <give_flag>
   0x0804879a <+128>:	jmp    0x80487ac <main+146>
   0x0804879c <+130>:	sub    $0xc,%esp
   0x0804879f <+133>:	push   $0x8048960
   0x080487a4 <+138>:	call   0x8048450 <puts@plt>
   0x080487a9 <+143>:	add    $0x10,%esp
   0x080487ac <+146>:	mov    $0x0,%eax
   0x080487b1 <+151>:	mov    -0xc(%ebp),%edx
   0x080487b4 <+154>:	xor    %gs:0x14,%edx
   0x080487bb <+161>:	je     0x80487c2 <main+168>
   0x080487bd <+163>:	call   0x8048440 <__stack_chk_fail@plt>
   0x080487c2 <+168>:	mov    -0x4(%ebp),%ecx
   0x080487c5 <+171>:	leave  
   0x080487c6 <+172>:	lea    -0x4(%ecx),%esp
   0x080487c9 <+175>:	ret    
End of assembler dump.
(gdb) 
(gdb) 
(gdb) 
(gdb) ls
Undefined command: "ls".  Try "help".
(gdb) 
Undefined command: "ls".  Try "help".
(gdb) 
Undefined command: "ls".  Try "help".
(gdb) disass check
Dump of assembler code for function check:
   0x08048661 <+0>:	push   %ebp
   0x08048662 <+1>:	mov    %esp,%ebp
   0x08048664 <+3>:	sub    $0x18,%esp
   0x08048667 <+6>:	sub    $0xc,%esp
   0x0804866a <+9>:	pushl  0x8(%ebp)
   0x0804866d <+12>:	call   0x8048470 <strlen@plt>
   0x08048672 <+17>:	add    $0x10,%esp
   0x08048675 <+20>:	mov    %eax,-0x10(%ebp)
   0x08048678 <+23>:	cmpl   $0x13,-0x10(%ebp)
   0x0804867c <+27>:	ja     0x8048688 <check+39>
   0x0804867e <+29>:	mov    $0x0,%eax
   0x08048683 <+34>:	jmp    0x8048718 <check+183>
   0x08048688 <+39>:	mov    0x8(%ebp),%eax
   0x0804868b <+42>:	movzbl (%eax),%eax
   0x0804868e <+45>:	cmp    $0x61,%al
   0x08048690 <+47>:	je     0x8048699 <check+56>
   0x08048692 <+49>:	mov    $0x0,%eax
   0x08048697 <+54>:	jmp    0x8048718 <check+183>
   0x08048699 <+56>:	mov    0x8(%ebp),%eax
   0x0804869c <+59>:	add    $0x1,%eax
   0x0804869f <+62>:	movzbl (%eax),%eax
   0x080486a2 <+65>:	cmp    $0x71,%al
   0x080486a4 <+67>:	je     0x80486ad <check+76>
   0x080486a6 <+69>:	mov    $0x0,%eax
   0x080486ab <+74>:	jmp    0x8048718 <check+183>
   0x080486ad <+76>:	mov    0x8(%ebp),%eax
   0x080486b0 <+79>:	add    $0x2,%eax
   0x080486b3 <+82>:	movzbl (%eax),%eax
   0x080486b6 <+85>:	cmp    $0x75,%al
   0x080486b8 <+87>:	je     0x80486c1 <check+96>
   0x080486ba <+89>:	mov    $0x0,%eax
   0x080486bf <+94>:	jmp    0x8048718 <check+183>
   0x080486c1 <+96>:	mov    0x8(%ebp),%eax
   0x080486c4 <+99>:	add    $0x3,%eax
   0x080486c7 <+102>:	movzbl (%eax),%eax
   0x080486ca <+105>:	cmp    $0x61,%al
---Type <return> to continue, or q <return> to quit---break *0x0804868e
   0x080486cc <+107>:	je     0x80486d5 <check+116>
   0x080486ce <+109>:	mov    $0x0,%eax
   0x080486d3 <+114>:	jmp    0x8048718 <check+183>
   0x080486d5 <+116>:	subl   $0x1,-0x10(%ebp)
   0x080486d9 <+120>:	movl   $0x0,-0xc(%ebp)
   0x080486e0 <+127>:	jmp    0x804870b <check+170>
   0x080486e2 <+129>:	mov    0x8(%ebp),%edx
   0x080486e5 <+132>:	mov    -0xc(%ebp),%eax
   0x080486e8 <+135>:	add    %edx,%eax
   0x080486ea <+137>:	movzbl (%eax),%edx
   0x080486ed <+140>:	mov    0x8(%ebp),%ecx
   0x080486f0 <+143>:	mov    -0x10(%ebp),%eax
   0x080486f3 <+146>:	add    %ecx,%eax
   0x080486f5 <+148>:	movzbl (%eax),%eax
   0x080486f8 <+151>:	cmp    %al,%dl
   0x080486fa <+153>:	je     0x8048703 <check+162>
   0x080486fc <+155>:	mov    $0x0,%eax
   0x08048701 <+160>:	jmp    0x8048718 <check+183>
   0x08048703 <+162>:	addl   $0x1,-0xc(%ebp)
   0x08048707 <+166>:	subl   $0x1,-0x10(%ebp)
   0x0804870b <+170>:	mov    -0xc(%ebp),%eax
   0x0804870e <+173>:	cmp    -0x10(%ebp),%eax
   0x08048711 <+176>:	jbe    0x80486e2 <check+129>
   0x08048713 <+178>:	mov    $0x1,%eax
   0x08048718 <+183>:	leave  
   0x08048719 <+184>:	ret    
End of assembler dump.
(gdb) break *0x0804868e
Breakpoint 1 at 0x804868e
(gdb) break 0x080486a2
Function "0x080486a2" not defined.
Make breakpoint pending on future shared library load? (y or [n]) n
(gdb) break *0x080486a2
Breakpoint 2 at 0x80486a2
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aqua
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3208) exited normally]
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aquaaaaaaaaaaaaaaa
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3212) exited normally]
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aaaaaaaaaaaaa
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3213) exited normally]
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x0804868e in check ()
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /kali/checker 
Tell me something interesting:
aaaaaaaaaaaaaaaaaaa
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3215) exited normally]
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aaaaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x0804868e in check ()
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /kali/checker 
Tell me something interesting:
aaaaaaaaaaaaaaaaaaa
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3217) exited normally]
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aaaaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x0804868e in check ()
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) ay
Please answer y or n.
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /kali/checker 
Tell me something interesting:
aquaaquaaquaauqaauqa

Breakpoint 1, 0x0804868e in check ()
(gdb) c
Continuing.

Breakpoint 2, 0x080486a2 in check ()
(gdb) c
Continuing.
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3219) exited normally]
(gdb) disass check
Dump of assembler code for function check:
   0x08048661 <+0>:	push   %ebp
   0x08048662 <+1>:	mov    %esp,%ebp
   0x08048664 <+3>:	sub    $0x18,%esp
   0x08048667 <+6>:	sub    $0xc,%esp
   0x0804866a <+9>:	pushl  0x8(%ebp)
   0x0804866d <+12>:	call   0x8048470 <strlen@plt>
   0x08048672 <+17>:	add    $0x10,%esp
   0x08048675 <+20>:	mov    %eax,-0x10(%ebp)
   0x08048678 <+23>:	cmpl   $0x13,-0x10(%ebp)
   0x0804867c <+27>:	ja     0x8048688 <check+39>
   0x0804867e <+29>:	mov    $0x0,%eax
   0x08048683 <+34>:	jmp    0x8048718 <check+183>
   0x08048688 <+39>:	mov    0x8(%ebp),%eax
   0x0804868b <+42>:	movzbl (%eax),%eax
   0x0804868e <+45>:	cmp    $0x61,%al
   0x08048690 <+47>:	je     0x8048699 <check+56>
   0x08048692 <+49>:	mov    $0x0,%eax
   0x08048697 <+54>:	jmp    0x8048718 <check+183>
   0x08048699 <+56>:	mov    0x8(%ebp),%eax
   0x0804869c <+59>:	add    $0x1,%eax
   0x0804869f <+62>:	movzbl (%eax),%eax
   0x080486a2 <+65>:	cmp    $0x71,%al
   0x080486a4 <+67>:	je     0x80486ad <check+76>
   0x080486a6 <+69>:	mov    $0x0,%eax
   0x080486ab <+74>:	jmp    0x8048718 <check+183>
   0x080486ad <+76>:	mov    0x8(%ebp),%eax
   0x080486b0 <+79>:	add    $0x2,%eax
   0x080486b3 <+82>:	movzbl (%eax),%eax
   0x080486b6 <+85>:	cmp    $0x75,%al
   0x080486b8 <+87>:	je     0x80486c1 <check+96>
   0x080486ba <+89>:	mov    $0x0,%eax
   0x080486bf <+94>:	jmp    0x8048718 <check+183>
   0x080486c1 <+96>:	mov    0x8(%ebp),%eax
   0x080486c4 <+99>:	add    $0x3,%eax
   0x080486c7 <+102>:	movzbl (%eax),%eax
   0x080486ca <+105>:	cmp    $0x61,%al
---Type <return> to continue, or q <return> to quit--- 
   0x080486cc <+107>:	je     0x80486d5 <check+116>
   0x080486ce <+109>:	mov    $0x0,%eax
   0x080486d3 <+114>:	jmp    0x8048718 <check+183>
   0x080486d5 <+116>:	subl   $0x1,-0x10(%ebp)
   0x080486d9 <+120>:	movl   $0x0,-0xc(%ebp)
   0x080486e0 <+127>:	jmp    0x804870b <check+170>
   0x080486e2 <+129>:	mov    0x8(%ebp),%edx
   0x080486e5 <+132>:	mov    -0xc(%ebp),%eax
   0x080486e8 <+135>:	add    %edx,%eax
   0x080486ea <+137>:	movzbl (%eax),%edx
   0x080486ed <+140>:	mov    0x8(%ebp),%ecx
   0x080486f0 <+143>:	mov    -0x10(%ebp),%eax
   0x080486f3 <+146>:	add    %ecx,%eax
   0x080486f5 <+148>:	movzbl (%eax),%eax
   0x080486f8 <+151>:	cmp    %al,%dl
   0x080486fa <+153>:	je     0x8048703 <check+162>
   0x080486fc <+155>:	mov    $0x0,%eax
   0x08048701 <+160>:	jmp    0x8048718 <check+183>
   0x08048703 <+162>:	addl   $0x1,-0xc(%ebp)
   0x08048707 <+166>:	subl   $0x1,-0x10(%ebp)
   0x0804870b <+170>:	mov    -0xc(%ebp),%eax
   0x0804870e <+173>:	cmp    -0x10(%ebp),%eax
   0x08048711 <+176>:	jbe    0x80486e2 <check+129>
   0x08048713 <+178>:	mov    $0x1,%eax
   0x08048718 <+183>:	leave  
   0x08048719 <+184>:	ret    
End of assembler dump.
(gdb) break *0x080486ca
Breakpoint 3 at 0x80486ca
(gdb) break *0x080486f8
Breakpoint 4 at 0x80486f8
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aquaaaaaaaaaaaaaaaaa

Breakpoint 1, 0x0804868e in check ()
(gdb) c
Continuing.

Breakpoint 2, 0x080486a2 in check ()
(gdb) c
Continuing.

Breakpoint 3, 0x080486ca in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) ir
Undefined command: "ir".  Try "help".
(gdb) info registers 
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x286	[ PF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x282	[ SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /kali/checker 
Tell me something interesting:
aqua
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3226) exited normally]
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aquaaquaaquaauqaauqa

Breakpoint 1, 0x0804868e in check ()
(gdb) c
Continuing.

Breakpoint 2, 0x080486a2 in check ()
(gdb) c
Continuing.

Breakpoint 3, 0x080486ca in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x282	[ SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x282	[ SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x286	[ PF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) run
The program being debugged has been started already.
Start it from the beginning? (y or n) y
Starting program: /kali/checker 
Tell me something interesting:
aquaaquaauqaauqaauqa

Breakpoint 1, 0x0804868e in check ()
(gdb) c
Continuing.

Breakpoint 2, 0x080486a2 in check ()
(gdb) c
Continuing.

Breakpoint 3, 0x080486ca in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x282	[ SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x286	[ PF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) 
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3230) exited normally]
(gdb) c
The program is not being run.
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aquaaquaaquaauqaauqa

Breakpoint 1, 0x0804868e in check ()
(gdb) c
Continuing.

Breakpoint 2, 0x080486a2 in check ()
(gdb) c
Continuing.

Breakpoint 3, 0x080486ca in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x282	[ SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x286	[ PF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.
That doesn't look right! Go reverse some more!
[Inferior 1 (process 3231) exited normally]
(gdb) run
Starting program: /kali/checker 
Tell me something interesting:
aquaaquaauuaauqaauqa

Breakpoint 1, 0x0804868e in check ()
(gdb) c
Continuing.

Breakpoint 2, 0x080486a2 in check ()
(gdb) c
Continuing.

Breakpoint 3, 0x080486ca in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x282	[ SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x71	113
ecx            0xffffd3bc	-11332
edx            0x71	113
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x61	97
ecx            0xffffd3bc	-11332
edx            0x61	97
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x292	[ AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.

Breakpoint 4, 0x080486f8 in check ()
(gdb) i r
eax            0x75	117
ecx            0xffffd3bc	-11332
edx            0x75	117
ebx            0x0	0
esp            0xffffd380	0xffffd380
ebp            0xffffd398	0xffffd398
esi            0x1	1
edi            0xf7fa9000	-134574080
eip            0x80486f8	0x80486f8 <check+151>
eflags         0x296	[ PF AF SF IF ]
cs             0x23	35
ss             0x2b	43
ds             0x2b	43
es             0x2b	43
fs             0x0	0
gs             0x63	99
(gdb) c
Continuing.
flag.txt not found. If you were running this against the remote server, you'd have the flag right now. If you are seeing this when connected to the server, something has gone horribly wrong, and you should contact the admins!
[Inferior 1 (process 3232) exited normally]
(gdb) 
The program is not being run.
(gdb) 
The program is not being run.
(gdb) 
The program is not being run.

