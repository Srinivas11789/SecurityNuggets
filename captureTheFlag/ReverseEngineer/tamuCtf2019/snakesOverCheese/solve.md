root@kali:~/Desktop/pyReverse# git clone https://github.com/Mysterie/uncompyle2
Cloning into 'uncompyle2'...
remote: Enumerating objects: 329, done.
remote: Total 329 (delta 0), reused 0 (delta 0), pack-reused 329
Receiving objects: 100% (329/329), 478.81 KiB | 2.66 MiB/s, done.
Resolving deltas: 100% (176/176), done.
root@kali:~/Desktop/pyReverse# ls
uncompyle2
root@kali:~/Desktop/pyReverse# cd uncompyle2/
root@kali:~/Desktop/pyReverse/uncompyle2# ls
compile_tests  PKG-INFO    scripts    setup.py  test_pythonlib.py
MANIFEST       README.rst  setup.cfg  test      uncompyle2
root@kali:~/Desktop/pyReverse/uncompyle2# python setup.py install
running install
running build
running install_scripts
copying build/scripts-2.7/uncompyle2 -> /usr/local/bin
changing mode of /usr/local/bin/uncompyle2 to 755
running install_egg_info
Writing /usr/local/lib/python2.7/dist-packages/uncompyle2-1.1.egg-info
root@kali:~/Desktop/pyReverse/uncompyle2# ls
build          MANIFEST  README.rst  setup.cfg  test               uncompyle2
compile_tests  PKG-INFO  scripts     setup.py   test_pythonlib.py
root@kali:~/Desktop/pyReverse/uncompyle2# ./scripts/uncompyle2 -h

Usage: uncompyle2 [OPTIONS]... [ FILE | DIR]...

Examples:
  uncompyle2      foo.pyc bar.pyc       # decompile foo.pyc, bar.pyc to stdout
  uncompyle2 -o . foo.pyc bar.pyc       # decompile to ./foo.pyc_dis and ./bar.pyc_dis
  uncompyle2 -o /tmp /usr/lib/python1.5 # decompile whole library

Options:
  -o <path>     output decompiled files to this path:
                if multiple input files are decompiled, the common prefix
                is stripped from these names and the remainder appended to
                <path>
                  uncompyle -o /tmp bla/fasel.pyc bla/foo.pyc
                    -> /tmp/fasel.pyc_dis, /tmp/foo.pyc_dis
                  uncompyle -o /tmp bla/fasel.pyc bar/foo.pyc
                    -> /tmp/bla/fasel.pyc_dis, /tmp/bar/foo.pyc_dis
                  uncompyle -o /tmp /usr/lib/python1.5
                    -> /tmp/smtplib.pyc_dis ... /tmp/lib-tk/FixTk.pyc_dis
  -c <file>     attempts a disassembly after compiling <file>
  -d            do not print timestamps
  -p <integer>  use <integer> number of processes
  -r            recurse directories looking for .pyc and .pyo files
  --verify      compare generated source with input byte-code
                (requires -o)
  --help        show this message

Debugging Options:
  --showasm   -a  include byte-code                  (disables --verify)
  --showast   -t  include AST (abstract syntax tree) (disables --verify)

Extensions of generated files:
  '.pyc_dis' '.pyo_dis'   successfully decompiled (and verified if --verify)
    + '_unverified'       successfully decompile but --verify failed
    + '_failed'           decompile failed (contact author for enhancement)

root@kali:~/Desktop/pyReverse/uncompyle2# ./scripts/uncompyle2 ~/Downloads/reversing2
reversing2(1).pyc  reversing2.pyc     
root@kali:~/Desktop/pyReverse/uncompyle2# ./scripts/uncompyle2 ~/Downloads/reversing2.pyc 
# 2019.02.23 11:56:29 PST
# Embedded file name: reversing2.py
from datetime import datetime
Fqaa = [102,
 108,
 97,
 103,
 123,
 100,
 101,
 99,
 111,
 109,
 112,
 105,
 108,
 101,
 125]
XidT = [83,
 117,
 112,
 101,
 114,
 83,
 101,
 99,
 114,
 101,
 116,
 75,
 101,
 121]

def main():
    print 'Clock.exe'
    input = raw_input('>: ').strip()
    kUIl = ''
    for i in XidT:
        kUIl += chr(i)

    if input == kUIl:
        alYe = ''
        for i in Fqaa:
            alYe += chr(i)

        print alYe
    else:
        print datetime.now()


if __name__ == '__main__':
    main()
# okay decompyling /root/Downloads/reversing2.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2019.02.23 11:56:29 PST
root@kali:~/Desktop/pyReverse/uncompyle2# ./scripts/uncompyle2 ~/Downloads/reversing2.pyc > ~/Downloads/reversing2.py
root@kali:~/Desktop/pyReverse/uncompyle2# python ~/Downloads/reversing2.py
Clock.exe
>: s
2019-02-23 11:57:54.551543
root@kali:~/Desktop/pyReverse/uncompyle2# python ~/Downloads/reversing2.py
Clock.exe
>: 12312
2019-02-23 11:57:56.911248
root@kali:~/Desktop/pyReverse/uncompyle2# cd ~/Downloads/
root@kali:~/Downloads# cdvi reversing2
bash: cdvi: command not found
root@kali:~/Downloads# vi reversing2
root@kali:~/Downloads# vi reversing2.py
root@kali:~/Downloads# python reversing2.py
Clock.exe
>: 123
SuperSecretKey
2019-02-23 11:58:44.911365
root@kali:~/Downloads# python reversing2.py
Clock.exe
>: SuperSecretKey
SuperSecretKey
flag{decompile}
root@kali:~/Downloads# cat reversing2.py
# 2019.02.23 11:57:43 PST
# Embedded file name: reversing2.py
from datetime import datetime
Fqaa = [102,
 108,
 97,
 103,
 123,
 100,
 101,
 99,
 111,
 109,
 112,
 105,
 108,
 101,
 125]
XidT = [83,
 117,
 112,
 101,
 114,
 83,
 101,
 99,
 114,
 101,
 116,
 75,
 101,
 121]

def main():
    print 'Clock.exe'
    input = raw_input('>: ').strip()
    kUIl = ''
    for i in XidT:
        kUIl += chr(i)
    print kUIl
    if input == kUIl:
        alYe = ''
        for i in Fqaa:
            alYe += chr(i)

        print alYe
    else:
        print datetime.now()


if __name__ == '__main__':
    main()
# okay decompyling /root/Downloads/reversing2.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2019.02.23 11:57:43 PST
root@kali:~/Downloads# 

