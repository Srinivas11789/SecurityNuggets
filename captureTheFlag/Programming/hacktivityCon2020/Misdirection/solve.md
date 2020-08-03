### Challenge

```

```

### Recon

* There are numerous redirects with body of the redirect containing the flag char by char
* Follow redirects until you get the flag

### Solve

```
kali@kali:~$ 
kali@kali:~$ cat flagFinder.py 
# The redirect body contains each letter of the flag 

import requests
host = "http://jh2i.com:50011"
r = requests.get(host + '/site/flag.php', allow_redirects=False)
flag = "->"
while r.status_code == 302 and flag[-1] != "}":
    body = r.text
    b = body.strip().split(" ")
    flag += b[-1]
    next_url = r.headers["Location"]
    r = requests.get(host + next_url, allow_redirects=False)
print(flag)

kali@kali:~$ python flagFinder.py 
->flag{http_302_point_you_in_the_right_redirection}
```