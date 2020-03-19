### Challenge

```
RSA strikes again!

n = 126390312099294739294606157407778835887
e = 65537
c = 13612260682947644362892911986815626931
```

### Recon
* Its RSA, this time I used RsaCtfTool to save time and get ahead with other challenges in the ctf.
* https://github.com/Ganapati/RsaCtfTool

### Solve

```
(env) kali@kali:~/Downloads/RsaCtfTool$ ./RsaCtfTool.py -n 126390312099294739294606157407778835887 -e 65537 --uncipher 13612260682947644362892911986815626931                                 
[+] Clear text : b'\x00actf{10minutes}'                                                                   
(env) kali@kali:~/Downloads/RsaCtfTool$           
```
