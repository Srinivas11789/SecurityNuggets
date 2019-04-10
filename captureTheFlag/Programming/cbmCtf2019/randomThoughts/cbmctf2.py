# Web2

import requests, time

cookie = ""
for i in range(10000):
    ts = int(time.time())
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
    headers["Referer"] = "http://cbmctf2019.cf:3003/"
    question = requests.get("http://cbmctf2019.cf:5001/", headers=headers, cookies=cookie)
    cookie = question.cookies
    question = question.text
    print question
    if "cbm" in question.lower():
        print question
        break