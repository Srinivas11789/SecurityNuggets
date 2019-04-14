import requests, time
import urllib

# Obviously a direct redirection does not work
cookie = ""
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
headers["Referer"] = "http://op1.ctf.euristica.in/"
# Extra
# headers["Location"] = "http://127.0.0.1:1337" (only in php?)
# Redirect 302?
# Make a website to return 302 to the localhost?
#
data = {"url":"http://google.com"}
question = requests.post("http://op1.ctf.euristica.in/view", headers=headers, cookies=cookie, data=data)
cookie = question.cookies
question = question.text
print question

"""
                          
                                <div class="notification is-warning">
                                        Can&#39;t do that mate.
                                </div>
                          

"""
