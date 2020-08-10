### Challenge

```
Great day to you, AppSec Agent! Your mission if you choose to accept, find a way to read the flag. All we have for you was an interception of a file and the network traffic. Good luck.
```

### Recon
* The App.sec has garbage data
* PCAP
  * has a HTTP python file exchange
* Investigate python file,
  * secret.pdf has been encrypted to App.sec and sent
  * A random key is used but it is also sent over the network
  * ( For a while I mistook the key to be `A P P 5 3 C` and the random key is just used as delay ) Yikes! 
  * That was not the case, the last message says SENT KEY IN SECURE WAY which means the delay is the key and that is what was meant to be sent with the same keywork `A P P 5 3 C`
  * Taking all the packet delays from Wireshark for packates where `A P P 5 3 C` was sent...

### Solve
* Decryption in this case is only XOR so we can reverse the XOR logic and key is only rotated. So we check our hypotheses of decryption with secret.pdf and AppTest.sec and it works fine.....
* Now with the deduced key try running decrypt
* flag.pdf contains webpage of super-fans in appsec village
* Viewed source, did a little pdf forensics and also checked the destination webpage src --> NOTHING!
* Finally remembered it might be printed in white colors so copied all text from pdf ---> 
```
C T F { A S - M 1 5 C - A S -1 T - 1 5 }
Congrats! Join App Sec Village as a Super Fans today  https://www.appsecvillage.com/super-fans
```