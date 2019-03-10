# Curl Command to send a request with a cookie and receive the new cookie
# * Identified the cookie to be a md5 hash
# * Initial 2 hashes were pc, tf so we have to crack all the hashes to obtain the flag...
"""
curl -i -s -k  -X $'OPTIONS' \
    -H $'Host: 159.89.166.12:13500' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Cookie: flag=440c5c247c708c6e46783e47e3986889' -H $'Connection: close' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'flag=440c5c247c708c6e46783e47e3986889' \
    $'http://159.89.166.12:13500/'
"""
# Ref for handling cookies: https://stackoverflow.com/questions/5606083/how-to-set-and-retrieve-cookie-in-http-header-in-python

from urllib import request
cookies = []
response = request.urlopen("http://159.89.166.12:13500")
cookie = response.getheader("Set-Cookie")
while cookie not in cookies:
      print(cookie.split("=")[-1])
      cookies.append(cookie)
      req = request.Request("http://159.89.166.12:13500", headers={"Cookie": cookie}) 
      response = request.urlopen(req)
      cookie = response.getheader("Set-Cookie")
