**backtoBasics** 
* *Question:* —> Easy —> not pretty much many options. No need to open a link from a browser, there is always a different way

- *Thoughts:* Used `telnet, curl, httpie, ssl, openssl` ways to connect to the url with no luck. 

```bash
# HEAD request
$ curl -I http://35.197.254.240/backtobasics/
HTTP/1.1 200 OK
Server: nginx/1.10.3 (Ubuntu)
Date: Fri, 08 Feb 2019 22:55:57 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Allow: GET, POST, HEAD,OPTIONS

# POST request
$ curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://35.197.254.240/backtobasics/
<!--
var _0x7f88=["","join","reverse","split","log","ceab068d9522dc567177de8009f323b2"];function reverse(_0xa6e5x2){flag= _0xa6e5x2[_0x7f88[3]](_0x7f88[0])[_0x7f88[2]]()[_0x7f88[1]](_0x7f88[0])}console[_0x7f88[4]]= reverse;console[_0x7f88[4]](_0x7f88[5])
-->$

# GET request - obviously when executed from a browser this would redirect to google.com
$ curl -g http://35.197.254.240/backtobasics/

<script> document.location = "http://www.google.com"; </script>srimbp:dev sri$ 

# Also tried with /backtobasics in vain for a long time until changed to `/backtobasics/`
```

**Steps:**
* POST request works

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Web/saudiAndOmanNationalCtf/backToBasics/asset1.png" title="Burp">

* As already shown above, POST method worked and returned a javascript which when run in console had set the flag in the variable `flag`

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Web/saudiAndOmanNationalCtf/backToBasics/asset2.png" title="Consoe">

**Output:**

Flag:`2b323f9008ed771765cd2259d860baec`

**Other Tries:**

* Telnet
```bash
telnet 35.197.254.240 80
Trying 35.197.254.240...
Connected to 240.254.197.35.bc.googleusercontent.com.
Escape character is '^]'.
POST backtobasics/
HTTP/1.1 400 Bad Request
Server: nginx/1.10.3 (Ubuntu)
Date: Fri, 08 Feb 2019 23:17:05 GMT
Content-Type: text/html
Content-Length: 182
Connection: close
Allow: GET, POST, HEAD,OPTIONS

<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.10.3 (Ubuntu)</center>
</body>
</html>
Connection closed by foreign host.
srimbp:dev sri$ telnet 35.197.254.240 80
Trying 35.197.254.240...
Connected to 240.254.197.35.bc.googleusercontent.com.
Escape character is '^]'.
POST /backtobasics/
<html>
<head><title>400 Bad Request</title></head>
<body bgcolor="white">
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.10.3 (Ubuntu)</center>
</body>
</html>
Connection closed by foreign host.
srimbp:dev sri$ 

* Openssl
srimbp:dev sri$ openssl s_client -connect 35.197.254.240:80
CONNECTED(00000003)
4560729708:error:1400410B:SSL routines:CONNECT_CR_SRVR_HELLO:wrong version number:/BuildRoot/Library/Caches/com.apple.xbs/Sources/libressl/libressl-22.240.1/libressl-2.6/ssl/ssl_pkt.c:386:
---
no peer certificate available
---
No client certificate CA names sent
---
SSL handshake has read 5 bytes and written 0 bytes
---
New, (NONE), Cipher is (NONE)
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : 0000
    Session-ID: 
    Session-ID-ctx: 
    Master-Key: 
    Start Time: 1549666111
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
---
```



