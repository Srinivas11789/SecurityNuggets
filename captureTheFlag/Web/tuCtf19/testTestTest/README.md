srimbp-623:broken sri$ http http://chal.tuctf.com:30004/img/
HTTP/1.1 200 OK
Connection: Keep-Alive
Content-Encoding: gzip
Content-Length: 485
Content-Type: text/html;charset=UTF-8
Date: Sat, 30 Nov 2019 17:06:49 GMT
Keep-Alive: timeout=5, max=100
Server: Apache/2.4.38 (Debian)
Vary: Accept-Encoding

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<html>
 <head>
  <title>Index of /img</title>
 </head>
 <body>
<h1>Index of /img</h1>
  <table>
   <tr><th valign="top"><img src="/icons/blank.gif" alt="[ICO]"></th><th><a href="?C=N;O=D">Name</a></th><th><a href="?C=M;O=A">Last modified</a></th><th><a href="?C=S;O=A">Size</a></th><th><a href="?C=D;O=A">Description</a></th></tr>
   <tr><th colspan="5"><hr></th></tr>
<tr><td valign="top"><img src="/icons/back.gif" alt="[PARENTDIR]"></td><td><a href="/">Parent Directory</a></td><td>&nbsp;</td><td align="right">  - </td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/image2.gif" alt="[IMG]"></td><td><a href="TEST.jpg">TEST.jpg</a></td><td align="right">2019-11-21 08:06  </td><td align="right"> 53K</td><td>&nbsp;</td></tr>
<tr><td valign="top"><img src="/icons/text.gif" alt="[TXT]"></td><td><a href="TODO.txt">TODO.txt</a></td><td align="right">2019-11-21 08:06  </td><td align="right"> 86 </td><td>&nbsp;</td></tr>
   <tr><th colspan="5"><hr></th></tr>
</table>
<address>Apache/2.4.38 (Debian) Server at chal.tuctf.com Port 30004</address>
</body></html>

srimbp-623:broken sri$ http http://chal.tuctf.com:30004/img/TODO.txt
HTTP/1.1 200 OK
Accept-Ranges: bytes
Connection: Keep-Alive
Content-Encoding: gzip
Content-Length: 93
Content-Type: text/plain
Date: Sat, 30 Nov 2019 17:06:59 GMT
ETag: "56-597d6c7d565c0-gzip"
Keep-Alive: timeout=5, max=100
Last-Modified: Thu, 21 Nov 2019 08:06:55 GMT
Server: Apache/2.4.38 (Debian)
Vary: Accept-Encoding

1. Get rid of directory (bit.ly = love, bit.ly = life)
2. Move the flag from flag.php

srimbp-623:broken sri$ 
srimbp-623:broken sri$ 
srimbp-623:broken sri$ http http://chal.tuctf.com:30004/flag.php
HTTP/1.1 200 OK
Connection: Keep-Alive
Content-Encoding: gzip
Content-Length: 196
Content-Type: text/html; charset=UTF-8
Date: Sat, 30 Nov 2019 17:08:37 GMT
Keep-Alive: timeout=5, max=100
Server: Apache/2.4.38 (Debian)
Vary: Accept-Encoding
X-Powered-By: PHP/7.2.24

<link href="test.css" rel="stylesheet" type="text/css">TODO: put more stuff here before the test<br>Then print the flag TUCTF{d0nt_l34v3_y0ur_d1r3ct0ry_h4n61n6}<meta http-equiv='refresh' content='0;url=index.html'>

srimbp-623:broken sri$ 