import base64, requests, re
url = "http://45.32.148.106/"
page = requests.get(url)
result = page.text
base64encodedstring = re.search("flag:\s(.*)", result)
print(base64.b64decode(base64encodedstring.group(1)))
