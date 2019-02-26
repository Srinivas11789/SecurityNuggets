root@kali:~/Downloads# file reversing1 
reversing1: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=a0d672b744b45bdc3f634cf144d1ae3f2a0f4509, not stripped
root@kali:~/Downloads# strings reversing1 
/lib64/ld-linux-x86-64.so.2
CyIk
libstdc++.so.6
__gmon_start__
_Jv_RegisterClasses
_ITM_deregisterTMCloneTable
_ITM_registerTMCloneTable
_ZNSaIcED1Ev
_ZNSt8ios_base4InitD1Ev
__gxx_personality_v0
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_
_ZNSaIcEC1Ev
_ZNSt8ios_base4InitC1Ev
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev
_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
_ZSt4cout
libgcc_s.so.1
_Unwind_Resume
libc.so.6
__stack_chk_fail
__cxa_atexit
__libc_start_main
GCC_3.0
GLIBC_2.4
GLIBC_2.2.5
CXXABI_1.3
GLIBCXX_3.4.21
GLIBCXX_3.4
AWAVA
AUATL
[]A\A]A^A_
QUFBQUFBQUFBQUFBQUFBQQ==
Hello! I bet you are looking for the flag..
I really like basic encoding.. can you tell what kind I used??
RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn
Q2FuIHlvdSByZWNvZ25pemUgYmFzZTY0Pz8=
Z2lnZW17M2E1eV9SM3YzcjUxTjYhfQ==
WW91IGp1c3QgbWlzc2VkIHRoZSBmbGFn
;*3$"
zPLR
GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.11) 5.4.0 20160609
crtstuff.c
__JCR_LIST__
deregister_tm_clones
__do_global_dtors_aux
completed.7594
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
reversing1.cpp
_ZStL8__ioinit
_Z41__static_initialization_and_destruction_0ii
_GLOBAL__sub_I_main
__FRAME_END__
__JCR_END__
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__init_array_end
__init_array_start
_DYNAMIC
__libc_csu_fini
__gmon_start__
_Jv_RegisterClasses
_ZNSt8ios_base4InitC1Ev@@GLIBCXX_3.4
__libc_start_main@@GLIBC_2.2.5
__cxa_atexit@@GLIBC_2.2.5
_ZNSt8ios_base4InitD1Ev@@GLIBCXX_3.4
_ITM_deregisterTMCloneTable
_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc@@GLIBCXX_3.4
_IO_stdin_used
_ITM_registerTMCloneTable
__data_start
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEED1Ev@@GLIBCXX_3.4.21
__TMC_END__
_ZSt4cout@@GLIBCXX_3.4
__dso_handle
__libc_csu_init
__bss_start
__stack_chk_fail@@GLIBC_2.4
_ZNSaIcED1Ev@@GLIBCXX_3.4
_ZNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEC1EPKcRKS3_@@GLIBCXX_3.4.21
_edata
_ZNSaIcEC1Ev@@GLIBCXX_3.4
__gxx_personality_v0@@CXXABI_1.3
_Unwind_Resume@@GCC_3.0
.symtab
.strtab
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
.gcc_except_table
.init_array
.fini_array
.jcr
.dynamic
.got.plt
.data
.bss
.comment
root@kali:~/Downloads# base64 -d QUFBQUFBQUFBQUFBQUFBQQ==
base64: 'QUFBQUFBQUFBQUFBQUFBQQ==': No such file or directory
root@kali:~/Downloads# base64 -d "QUFBQUFBQUFBQUFBQUFBQQ=="
base64: 'QUFBQUFBQUFBQUFBQUFBQQ==': No such file or directory
root@kali:~/Downloads# base64 -d "QUFBQUFBQUFBQUFBQUFBQQ==
> ^C
root@kali:~/Downloads# python
Python 2.7.15+ (default, Nov 28 2018, 16:27:22) 
[GCC 8.2.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import base64
>>> base64.b64decode("QUFBQUFBQUFBQUFBQUFBQQ==")
'AAAAAAAAAAAAAAAA'
>>> base32.b32decode("QUFBQUFBQUFBQUFBQUFBQQ==")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'base32' is not defined
>>> import base32
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named base32
>>> base32.b32decode("QUFBQUFBQUFBQUFBQUFBQQ==")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'base32' is not defined
>>> base64.b64decode("QUFBQUFBQUFBQUFBQUFBQQ==")
'AAAAAAAAAAAAAAAA'
>>> base64.b64decode("RkxBR2ZsYWdGTEFHZmxhZ0ZMQUdmbGFn")
'FLAGflagFLAGflagFLAGflag'
>>> base64.b64decode("Q2FuIHlvdSByZWNvZ25pemUgYmFzZTY0Pz8=")
'Can you recognize base64??'
>>> base64.b64decode("Z2lnZW17M2E1eV9SM3YzcjUxTjYhfQ==")
'gigem{3a5y_R3v3r51N6!}'
>>> 

