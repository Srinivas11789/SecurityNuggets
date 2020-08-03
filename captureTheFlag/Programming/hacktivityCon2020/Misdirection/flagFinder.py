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

"""
# Brute Force Logic --> Fail!

import requests
session = requests.Session()
session.max_redirects = 30
try:
  response = session.get("http://jh2i.com:50011/site/flag.php")
except requests.exceptions.TooManyRedirects as exc:
  print("Too many Redirects!") 
  #print(exc.text)
  pass

if response.history:
  for resp in response.history:
    print(resp.status_code, resp.url, resp.text)
  print("Last redirect is :")
  print(response.status_code, response.url, resp.text)
else:
    print("Failed to follow redirects!")
    print("Too Many Redirects!")
    print(e.response)
"""
