### Scripting - CBMCTF - Are you Fast?

import requests, time

for i in range(10000):
    ts = int(time.time())
    question = requests.get("http://cbmctf2019.cf:3003/")
    cookie = question.cookies
    question = question.text
    question = question.split("<br>")
    A, B = question[0].strip("<h1>").split("and")
    A = A.split("=")[1]
    B = B.split("=")[1]
    ts = question[2].split("value=")[1].strip("></form>")

    #print A, B, ts
    
    data = {"answere": int(B)%int(A) ,"time": ts}
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
    headers["Referer"] = "http://cbmctf2019.cf:3003/"
    response = requests.post("http://cbmctf2019.cf:3003/check", data=data, cookies=cookie, headers=headers)
    answer = response.text
    if "cbm" in answer or "cbm".upper() in answer:
        print answer
        break
    


