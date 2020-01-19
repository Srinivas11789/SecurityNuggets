* Given a web server to ping any domain name
* COMMAND INJECTION: it has a file called `print-flag`, tried various commands to read it
```
* Reading a file in Linux with minimal permissions
    * Cat 
    * Head
    * Less
    * More
    * Tail
    * File
    * echo "$(<print-flag)"
    * Python
    * Perl
    * Ruby
    * Ps
    * ;
    * &&
    * ||
    * Grep
    * Tac
    * Curl
    * Wget
    * Ls -ltr /usr/bin
    * Set
    * Ll
    * Nl
    * Strings
    * ‘
    * Whom
    * Uname -a
    * User add
    * Pwd
    * Nc
    * vi
    * Nano
```
* CODE INJECTION: leads to a 403

* After some time thinking about defeating PING or network stack to read files, I was just trying to look for the `robots.txt` file contents. As usual accessed using the browser. Oh GOD, that was it!

* Commiting this mistake `TWICE`, just browse the web server files from browser as usual or CURL or WGET to obtain the files from web root dir.

```
root@kali:~/Desktop/insomnia# wget http://lowdeep.insomnihack.ch/print-flag
--2020-01-19 01:06:09--  http://lowdeep.insomnihack.ch/print-flag
Resolving lowdeep.insomnihack.ch (lowdeep.insomnihack.ch)... 34.65.144.142
Connecting to lowdeep.insomnihack.ch (lowdeep.insomnihack.ch)|34.65.144.142|:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6128 (6.0K)
Saving to: ‘print-flag.1’

print-flag.1                                        100%[===================================================================================================================>]   5.98K  --.-KB/s    in 0s      

2020-01-19 01:06:10 (862 MB/s) - ‘print-flag.1’ saved [6128/6128]

root@kali:~/Desktop/insomnia# 
root@kali:~/Desktop/insomnia# mv ~/Downloads/print-flag .
root@kali:~/Desktop/insomnia# file print-flag 
print-flag: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=72c589834f878a6a3267944f305c29166a1ace8b, stripped
root@kali:~/Desktop/insomnia# strings  print-flag 
/lib64/ld-linux-x86-64.so.2
O0\)
libc.so.6
puts
__cxa_finalize
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
AWAVI
AUATL
[]A\A]A^A_
INS{Wh1le_ld_k1nd_0f_forg0t_ab0ut_th3_x_fl4g}
;*3$"
GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
root@kali:~/Desktop/insomnia# 
```