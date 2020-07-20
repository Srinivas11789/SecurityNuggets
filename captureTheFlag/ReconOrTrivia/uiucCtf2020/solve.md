### Challenge 0
* Isabelle bot in discord --> Find useful info about it to track
* Check in misc/uiucCtf/starterOSINT
* Interacting with the bot
```
!socials

> I'm a hacker, but I'm also Isabelle. Maybe you could call me... IsabelleHacker? No, that sounds strange... Whatever, it will be something like that.
```
* Searching twitter we find https://twitter.com/search?q=hacker%20isabelle&src=typed_query
* Leading to account https://twitter.com/hackerisabelle
* With Flag in the tweet in plaintext

### Challenge 1

* Chal
```
Isabelle has some really bad opsec! She left some code up on a repo that definitely shouldnt be public. Find the naughty code and claim your prize.

Finishing the warmup OSINT chal will really help with this chal

The first two characters of the internal of this flag are 'c0', it may not be plaintext Additionally, the flag format may not be standard capitalization. Please be aware
```

* Find the secret exposed in code
* Use hints from twitter about mimidogz
* Tweets about github account --> Search github --> https://github.com/IsabelleOnSecurity
* This commit looks interesting https://github.com/IsabelleOnSecurity/mimidogz/commit/41d581eb3fc3aacb0a6a1f1aa0c5d65d40515d7b with the private keys
```
-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgQCXkMsJyPcWxSs8c2Q+cpV64WYzqVKtLTWC+8zMazjQ53LiL6PW
+USD3oVZbtLb/+oiLVXxE1fKs255OdKJzKfeghjs8fANC46RnZegNJ5sHvp18AaA
LjjDg0gdVtzSvb9zy3iJ+froBb2yHboGPyjhDWW9bNnDYUwNwKTtonswRQIDAQAB
AoGAWaMJYW0YLMBJFMRNydzsaLL7RZxjSAYPurp+YXscK/hl6j0wkYf0LGUiykSP
sgrFBpd3V08QQdIiiNFYoaSGtlZLKiUt79s++rhAkqMvGHppH2OnGJUs5K+BN7+l
eVvmPMKQgF0AQbTPp3Khr2vsFhp6j66DCKbEydWwS8E6RIECQQDo0cruDtbVHuFZ
FOHwgkhr4etrt/QGk3/b+YKY2lL4tV/dusuu8fsvzYghDsRJwzeQGPN+wqttf3hu
irbryg/lAkEApqf29Ja8Bu2ePcPhs/qq/3v/zvWBSblKkqdzv2iVrPym/Qy2UwJv
N2DLxBVxzqSIu2AMNAt2Et9UphilOvLY4QJAYD2Q6FVkAxdPyfYy66u/ajEqkw2o
pytD2FfM34iocbzwEwVLe1b2Ia2RjzC+fUtgZYWa6hRorsvZqcBXmyKc7QJBAIdt
JnlLpC/dGCII83hV0m8aTJ3ZUt6d+8OA38ZDLp4MEYbAtchuygGuXudQpdLOUW4y
drg0OBbN9POkQ2DLxwECQCTwJVBTbVv7nmYFNXHDKLsax2lBUPLGM1oDIwJAwaN9
Lk52tiAidez1Dpo7WsqFZLVfwnZMa2K/MPs6MgMX88s=
-----END RSA PRIVATE KEY-----

-----BEGIN RSA PRIVATE KEY-----
MIICXAIBAAKBgH0Y2Z0xu7m+AdeBMwV0F93JuqXyCAJOJbv0le2xtf3D7Fa+iX5s
XZrcRgtKozKy4Gg4LFaZqXQlKum106FpONJX/gNIvm67S1gs6ONS7Lfz+14E09mb
9ZA7fadqPUoRKHrhgLSsDlgqSLzUNpxoCQJdDfYbOtKH6mnzwd/3FyKbAgMBAAEC
gYBhJf5BjFDcI0ns4UINNyYdsD7KBpbfq260c3JHoF3UD+YnS1sdmexriiq/NBxf
D/kkFpOgQT8Ompqj2vfZ/wwHf4K5Ss241sTPQrYrDITztKYKeiU2tmkq9c4oRbXc
Oz0gY+egbXMFL9PaswyaVUiQdE0NqZOLdrrQRPextY57mQJBAL+Y/EA0acnRjUqm
9vU9OaGUY/8weaM31M+mM7gDenx+kNDViPwahhb4MEtfVJ7vPT6wVi4MzfM5Sehq
yIKfmlcCQQCnJXrbDZhLKCA5frtTTHPL0mLHt0JRHkKhwI4eh8P54UA1RtDw/NN5
e6nE6EEuiRG+6iHETNnzVErLiQknS9ddAkA7cM7xbFFVl3lqK5p6QuBaTJspVHSo
Om3/beSltg6OCQYMg/LXo7Lt9VmmSJEMLdSmWjaiWr6aMq/HNzm1rKZJAkEAoQxh
5bKhrLjK49sST154rEjYWKpgwZwwg33u8cfKsnew0CSdqbVRZdobZ9iJBXeYm6Uo
R+XskqIDNz2gjjZrGQJBAKHXJ/Howt6d8YRl7n+Y1ZZSAaUq4IJM9fOANwWk0XvU
BjPxWG9wJt6EqIOjtsH8Xp4IYIgxKbh6eFARmYeXjLc=
-----END RSA PRIVATE KEY-----

-----BEGIN RSA PRIVATE KEY-----
MIICWgIBAAKBgHBJRaQaXZ4wT2eoUDlGS5K4rGg0zzGTO0vdiT8E19xeuqMcDzjN
l9K6WZnKxHnyAQcY0RGujPN6mX+PmJt6UsAcJ8CHz/h1zqYuSe5zIJIj/qM24gaH
N0yP3ZtMdd/giChGOJ8bJXyvD5onFCG6hPRJjLvLGkXpvfiuG1SMBAqTAgMBAAEC
gYAOGqYMvuMTg631r0akaxgDDf9Z94gvCfdgyCr9J3aVz7BR3KxsziZL6exnTPjw
+Fz4rz1To0FBNB0j0L2yieLq46v86+c/gcIYB0ZgMCvy9AKuvh1E+3g0f4hkONR4
yuKkDBGxvazfp1jOl0tILhEjX/tqBucwaL7cQScIMHExAQJBAMDdTmdcQ+ftaz6w
xBcueL6z2cTXdJ7RXgfg33gl98NxgTPDu0Ja1M1iyjhNzIRnNMyDRvvmrhXrfvO9
KEEzHCMCQQCVCzxkfU1G7R3JFhKFXTp8QP+n5yVqGk1TlxzRTh1fp/n1K5EFXgUL
dOZR+1co47x32aCGBVclMpmSdcQRTcbRAkBdID9Ef3O2oJiBS99Thjf9dWB4wMRq
D5SE31toa4ToVX1anm9kSfGpPsOATmiroh4HhngXGDsFEJJbZQH0AZbbAkBhhaKU
ljB0Uj6FDv47aU8VcmpV8LbYgDFMmrnuclBiAMVbGJChlG10m58A0ZasWKc/PJT+
XIwy+LLn1Ergj6WhAkBV/Nssh+e5zzfoDSZThlfwEyY0GHbrN0FpCKawQ9d2+O5F
ieVegA9PBWTKbnBrd2q0bpbKHa/I2WN3jK4iSCNe
-----END RSA PRIVATE KEY-----
```
* And this one with the driver code change. (https://github.com/IsabelleOnSecurity/mimidogz/commit/89f4f78390a1a31d08643ba16cba50dc9fcd5ecb)
```
# Driver Code 
  DRIVER_CODE = "dWl1Y3Rme2MwbU0xdF90b195b3VyX2RyM0BtNSF9=="
  DRIVER_CODE = "c3BhZ2hldHRp=="
# Dimensions of a Matrix 
```

# Flag: 
```
>>> import base64
>>> base64.b64decode("dWl1Y3Rme2MwbU0xdF90b195b3VyX2RyM0BtNSF9==")
'uiuctf{c0mM1t_to_your_dr3@m5!}'
>>> base64.b64decode("c3BhZ2hldHRp==")
'spaghetti'
```

* uiuctf{c0mM1t_to_your_dr3@m5!}


### Challenge 2

* Chal
```
Wow holy heck Isabelle's OPSEC is really bad. She was trying to make a custom youtube api but it didnt work. Can you find her channel??

Finishing Isabelle's Opsec 1 will may you with this challenge

The first two characters of the internal of this flag are 'l3', it may not be plaintext Additionally, the flag format may not be standard capitalization. Please be aware
```

* This commit looks like it leads to the channel ---> https://github.com/IsabelleOnSecurity/api-stuff/commit/07aada163593bd8c57de496354ba04aa42c16723

* https://www.youtube.com/channel/UCnL8vVmpKY8ZmfSwoikavHQ/featured --> EliteHackerIsabelle1337

* Only one video is present in the channel and it says it used windows movie maker. Clearly this has got to something with the next challenge of using the video but for this challenge we need to find a flag starting with 13

* channel name, source, metadata about the channel until email did not help.

### Challenge 4

```
Isabelle hid one more secret somewhere on her youtube channel! Can you find it!?

Finishing previous OSINT Chals will assist you with this challenge

The first two characters of the internal of this flag are 'th', it may not be plaintext

Additionally, the flag format may not be standard capitalization. Please be aware

Made By: Thomas [Authors Note] I love this chal because I used it IRL to find out who someone cyberbullying a friend was. It's real OSINT -Thomas
```

* With frustration from challenge 2, I tried to learn more about youtube channel metadata security and found  

* Wanted to use the youtube data api --> Found https://mattw.io/youtube-metadata/ and tried to fetch all the metadata --> I doubted different thumbnail images for different device setttings under BRANDING SETTINGS for BANNER
  * TV Image had the flag.

* uiuctf{this_flag_is_not_cake_on_the_inside}