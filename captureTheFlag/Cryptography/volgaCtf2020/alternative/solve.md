### Challenge
```
Alternative
This task is alternative.

alternative.q.2020.volgactf.ru:7780/
```

### Recon
* I missed when Google Chrome complained of the certifcate being self signed when I connected to it. (Bummer@!)
* The page only has this text
```
<html>
    <head>
        <title>[VolgaCTF 2020 Quals] Alternative</title>
    </head>
    <body>
        <h1>Hello there!</h1>
        <p>Welcome to our first crypto challenge!</p>
        <p>Try to find some secret information here.</p>
    </body>
</html>
```
* Directly jumping into burp way would take a long time. ( Anyway... I tried a few stuff before ending to the point 1)
* `Directory Traversal` using dirb or dirbuster was not very successfull.
* Secret was somewhere so tried to play with cache and ETags. Modified most of the headers to check any different response ( while etag and times for last modified gave it was not very useful ). ( WayBackMachine or Google Cache? )
* Alternative? So tried different HTTP Methods - No Luck
* After sometime I tried to open the same without proxy and it complained of the certificate. (Bleh I realised it had a self signed cert)
* Now Alternative keyword made sense --> Its SAN ( Subj alternative name).
* One SAN DNS is `s0.many.fields.in.certificate.com`, so what are the next steps?
  - Tried connecting to the IP address with the hostname of SAN and it returned the same output (?????)
  - Tried alterning the etc/resolve to resolve the resp ip to the domain but same result
* All the fields of the certificate seemed normal.
  - Either there is a hidden fields or custom field in the cert itself
  - Converting between different certificate formats to view the fields?
  - As it is a crypto challenge there is something behind the hashes or strings
  - Crack the cert for the private key ( but we dont have any cipher text? )
  - no certificate policy so no EV

```
(env) kali@kali:~/Downloads$ python3
Python 3.7.6 (default, Dec 19 2019, 09:25:23) 
[GCC 9.2.1 20191130] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from OpenSSL import crypto
>>> cert_file = 'alternative2.pem'
>>> cert =  crypto.load_certificate(crypto.FILETYPE_PEM, open(cert_file).read())
>>> cert
<OpenSSL.crypto.X509 object at 0x7fc165a2ca10>
>>> cert.get_subject()
<X509Name object '/C=RU/ST=Samara/L=Samara/O=VolgaCTF/OU=CryptoGuys/CN=volgactf.ru'>
>>> subject = cert.get_subject()
>>> cert.get_issuer()
<X509Name object '/C=RU/ST=Samara/L=Samara/O=VolgaCTF/OU=CryptoGuys/CN=volgactf.ru'>
>>> cert.get_extension_count()
3
>>> cert.get_extension(0)
<OpenSSL.crypto.X509Extension object at 0x7fc164e95290>
>>> one = cert.get_extension(0)
>>> one.get_short_name()
b'keyUsage'
>>> one.get_data()
b'\x03\x02\x05\xe0'
>>> two = cert.get_extension(1)
>>> two.get_data()
b'0\n\x06\x08+\x06\x01\x05\x05\x07\x03\x01'
>>> two.get_short_name()
b'extendedKeyUsage'
>>> three = cert.get_extension(2)
>>> three.get_short_name()
b'subjectAltName'
>>> three.get_data()
b'04\x82\x0fwww.volgactf.ru\x82!s0.many.fields.in.certificate.com'
```

* Cert details
```
kali@kali:~/Downloads$ openssl x509 -text -noout -in alternative.cert 
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            2f:56:ad:4c:98:83:f7:73:92:5e:1a:d5:e7:62:bb:05:f4:a8:8e:e7
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C = RU, ST = Samara, L = Samara, O = VolgaCTF, OU = CryptoGuys, CN = volgactf.ru
        Validity
            Not Before: Mar  7 05:46:24 2020 GMT
            Not After : Mar  7 05:46:24 2022 GMT
        Subject: C = RU, ST = Samara, L = Samara, O = VolgaCTF, OU = CryptoGuys, CN = volgactf.ru
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                RSA Public-Key: (2048 bit)
                Modulus:
                    00:ab:20:5a:46:08:db:71:4c:23:5a:3c:88:12:05:
                    84:94:e6:e3:43:c8:91:6d:d7:40:1d:a2:86:2c:a8:
                    46:c2:92:b7:2e:aa:5c:21:19:ce:b9:30:f8:d3:b3:
                    b2:48:52:fa:92:57:86:0b:e0:9e:b3:9d:39:bc:35:
                    05:7d:94:f4:c0:10:42:0e:c2:3a:62:17:ec:5f:8c:
                    a5:a2:ad:63:39:82:9c:74:f1:ae:6d:44:e4:dd:4a:
                    c6:70:d9:15:86:e2:f8:df:09:62:4a:06:64:e8:21:
                    35:ac:60:31:54:97:3d:e1:ef:b1:1d:87:bc:56:c6:
                    d6:26:87:7f:3a:b5:1a:2c:56:61:e7:da:a6:d6:4f:
                    de:78:fe:73:07:e8:2e:2e:bd:74:d1:bf:45:65:c1:
                    fa:d1:0c:b2:f6:90:63:43:6d:ec:cb:b5:6e:70:69:
                    00:7d:ca:f0:e5:77:20:b3:8d:c8:43:19:9f:23:bb:
                    98:0d:b2:ae:ea:40:09:14:2e:0b:5e:2f:83:b3:16:
                    d3:1c:f0:a2:39:a4:67:c7:76:c3:8d:23:6f:a3:49:
                    41:64:ae:a5:6e:a4:4d:d1:09:a7:04:8b:00:78:ed:
                    84:da:7a:5c:0e:ab:3c:3a:ff:9c:34:2c:5a:8d:c9:
                    ae:3f:e2:c1:3e:3f:db:da:80:ed:c6:06:ad:98:e6:
                    a9:a5
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Key Usage: 
                Digital Signature, Non Repudiation, Key Encipherment
            X509v3 Extended Key Usage: 
                TLS Web Server Authentication
            X509v3 Subject Alternative Name: 
                DNS:www.volgactf.ru, DNS:s0.many.fields.in.certificate.com
    Signature Algorithm: sha256WithRSAEncryption
         51:dd:0b:0c:90:e0:81:a9:c9:42:90:cf:72:59:cb:d3:98:e5:
         1e:ec:96:ee:d4:e1:eb:98:56:69:32:46:16:80:99:4c:3f:41:
         ca:e2:e9:d9:7a:d8:a2:4d:eb:18:04:03:7b:a3:8e:c9:b5:e3:
         b7:b5:c6:33:b9:8d:ac:76:e5:be:15:4e:6d:b5:14:64:72:2e:
         02:96:c2:e7:d8:df:91:69:f2:ec:5b:8d:c2:be:99:c9:58:6a:
         08:36:02:07:83:31:c0:75:88:bb:4b:e9:e2:e5:49:ae:35:63:
         d4:7a:86:e7:78:73:cb:c3:db:3e:95:09:b9:b7:7a:9e:7a:77:
         da:2a:09:66:b9:6e:c8:cd:62:b6:da:82:fd:63:43:1f:e7:9d:
         8a:71:bc:a2:8d:68:bf:35:10:03:a8:cf:54:a8:ea:72:b2:a3:
         cd:0c:7f:ce:6b:39:42:ad:45:c7:e6:28:6a:9b:3a:ab:45:8b:
         47:df:f0:14:46:35:3c:b4:4f:ff:3b:62:4c:59:76:9a:2a:db:
         98:97:57:f5:68:3e:32:f6:3a:45:7b:3f:c6:a2:45:79:f0:cf:
         f7:64:39:90:61:7c:0a:92:37:d7:6e:fe:65:40:71:56:7f:5b:
         b7:71:73:37:ab:82:22:3c:ee:8f:5c:48:1c:09:da:7a:5b:93:
         6a:6a:a9:9e
```

### Solve
* After all this research, I tried the SAN I obtained on the challenge and it passed as the flag. Bleh! that was the flag but it was not in the flag format....
