srimbp-623:potato sri$ curl http://ctfchallenges.ritsec.club:8003/
<article>
<link rel="stylesheet" type="text/css" href="style.css">
<a href="https://twitter.com/RITSECclub" target="_blank">
  <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 width="30px" height="30px" viewBox="0 0 30 30" enable-background="new 0 0 30 30" xml:space="preserve">
   <path id="facebook" fill="#ffffff" d="M17.252,11.106V8.65c0-0.922,0.611-1.138,1.041-1.138h2.643V3.459l-3.639-0.015
	c-4.041,0-4.961,3.023-4.961,4.961v2.701H10v4.178h2.336v11.823h4.916V15.284h3.316l0.428-4.178H17.252z"/>
  </svg>
</a>

<a href="https://instagram.com/_ritsec_" target="_blank">
  <svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px"
	 width="30px" height="30px" viewBox="0 0 30 30" enable-background="new 0 0 30 30" xml:space="preserve">
   <path id="instagram" fill="#ffffff" d="M22.107,3.415H7.893c-2.469,0-4.479,2.007-4.479,4.477v4.73v9.486c0,2.469,2.01,4.479,4.479,4.479h14.215
	c2.469,0,4.479-2.01,4.479-4.479v-9.486v-4.73C26.586,5.421,24.576,3.415,22.107,3.415 M23.393,6.086l0.512-0.004v0.511v3.416
	l-3.916,0.014l-0.012-3.928L23.393,6.086z M11.693,12.622c0.742-1.028,1.945-1.7,3.307-1.7s2.564,0.672,3.307,1.7
	c0.484,0.67,0.771,1.49,0.771,2.379c0,2.248-1.828,4.078-4.078,4.078c-2.248,0-4.078-1.83-4.078-4.078
	C10.922,14.112,11.211,13.292,11.693,12.622 M24.328,22.107c0,1.225-0.994,2.219-2.221,2.219H7.893
	c-1.225,0-2.219-0.994-2.219-2.219v-9.486h3.459C8.832,13.356,8.664,14.159,8.664,15c0,3.494,2.842,6.335,6.336,6.335
	s6.336-2.842,6.336-6.335c0-0.842-0.17-1.645-0.467-2.379h3.459V22.107z"/>
  </svg>
</a>
 
  
</a>
<!-- upload and photos not yet linked -->
</article>



srimbp-623:potato sri$ curl http://ctfchallenges.ritsec.club:8003/upload.php
<form action="/upload.php" method="post" enctype="multipart/form-data">
 <input type="file" name="myFile">
 <br>
<input type="submit" name="submit" value="go!">
</form>



srimbp-623:potato sri$ curl http://ctfchallenges.ritsec.club:8003/photos.php
<html>
<head>
<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-0lax{text-align:left;vertical-align:top}
@media screen and (max-width: 767px) {.tg {width: auto !important;}.tg col {width: auto !important;}.tg-wrap {overflow-x: auto;-webkit-overflow-scrolling: touch;margin: auto 0px;}}</style>
</head>
<body>
Welcome to our awesome gallery!</br>
See recent uploaded pictures from our community, and feel free to rate or comment</br>
<div class="tg-wrap"><table class="tg">
<tr>
<td class="tg-0lax">uploaded by 10_0_0_37.php.gif<br><img src='uploads/10_0_0_37.php.gif' width=100px></td>
</tr>
</table></div>
</body>
</html>
srimbp-623:potato sri$ 



### Solve
* 

### References
* https://medium.com/@igordata/php-running-jpg-as-php-or-how-to-prevent-execution-of-user-uploaded-files-6ff021897389
* https://www.owasp.org/index.php/Code_Injection
* http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet 

