
# Pillow Imager
from PIL import Image
import sys

# * Record the coordinates of all the options prior using a dictionary
# * Process answers and use them to create 
# CoOrdinates of the answer sheet in the png
alphabet_option = {"A": 0, "B": 1, "C":2, "D":3, "E":4}
options = {
    "1": [(300, 400),(365, 400),(435, 400),(510, 400), (580, 400)],
    "2": [(300, 500),(365, 500),(435, 500),(510, 500), (580, 500)],
    "3": [(300, 580),(365, 580),(435, 580),(510, 580), (580, 580)],
    "4": [(300, 680),(365, 680),(435, 680),(510, 680), (580, 680)],
    "5": [(300, 770),(365, 770),(435, 770),(510, 770), (580, 770)],
    "6": [(300, 860),(365, 860),(435, 860),(510, 860), (580, 860)],
    "7": [(300, 950),(365, 950),(435, 950),(510, 950), (580, 950)],
    "8": [(300, 1030),(365, 1030),(435, 1030),(510, 1030), (580, 1030)],
    "9": [(300, 1130),(365, 1130),(435, 1130),(510, 1130), (580, 1130)],
    "10": [(300, 1210),(365, 1210),(435, 1210),(510, 1210), (580, 1210)],
    "11": [(785, 400),(855, 400),(925, 400),(990, 400), (1060, 400)],
    "12": [(785, 500),(855, 500),(925, 500),(990, 500), (1060, 500)],
    "13": [(785, 580),(855, 580),(925, 580),(990, 580), (1060, 580)],
    "14": [(785, 680),(855, 680),(925, 680),(990, 680), (1060, 680)],
    "15": [(785, 770),(855, 770),(925, 770),(990, 770), (1060, 770)],
    "16": [(785, 860),(855, 860),(925, 860),(990, 860), (1060, 860)],
    "17": [(785, 950),(855, 950),(925, 950),(990, 950), (1060, 950)],
    "18": [(785, 1030),(855, 1030),(925, 1030),(990, 1030), (1060, 1030)],
    "19": [(785, 1130),(855, 1130),(925, 1130),(990, 1130), (1060, 1130)],
    "20": [(785, 1210),(855, 1210),(925, 1210),(990, 1210), (1060, 1210)]
}
test_version = [(600, 1290), (695, 1290), (800, 1290), (900, 1290)]

#final_answers = []

# Answer sheet open
#image = Image.open('scantron.png')

# Answer mark
#mark = Image.open('checkmark.png').convert("RGBA")

# Run first time to resize checkmark png
"""
mark_new = mark.resize((120,120), Image.ANTIALIAS)
mark_new.save("checkmark.png")
mark = Image.open('checkmark.png').convert("RGBA")
"""

# Check Orientation ==> Orient-test file as an example
"""
image_copy = image.copy()
for j in range(1, 21):
    for i in range(0, 5):
        position = options[str(j)][i]
        image_copy.paste(mark, position, mark)

for ord in test_version:
    image_copy.paste(mark, ord, mark)
"""

# Practice quesntionnarie solve
"""
# Fetch questions from the server
import urllib2
practice_url = "http://ee.sunshinectf.org/practice"
questions = urllib2.urlopen(practice_url)
cookie = questions.info().dict["set-cookie"]
questions = questions.read()
questions = questions.split("\n")

# Extract questions and options
import re
for i in range(len(questions)):
    if re.match("<li>[0-9]+\s+[+-\/*]+\s+[0-9]+<\/li>", questions[i]):
        expression = questions[i].strip("<li>").strip("</li>")
        ans = eval(expression)
        # type
        i += 2
        # options
        for j in range(0, 4):
            choice = questions[i].strip("<li>").strip("</li>")
            #rint expression, ans, choice
            if str(ans) == choice:
                final_answers.append(j)
            i += 1
        # type
        i += 1

# Find and Mark answers in the answer sheet
#print final_answers
image_copy = image.copy()
for choice in range(len(final_answers)):
    #print choice+1, final_answers[choice]
    position = options[str(choice+1)][final_answers[choice]]
    image_copy.paste(mark, position, mark)

# Save and Upload answer sheet to the server
image_copy.save('answer.png', format="png")

# Upload answer sheet to the server
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers

register_openers()

datagen, headers = multipart_encode({"file": open("answer.png", 'r')})
headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
headers["Cookie"] = cookie
request = urllib2.Request(practice_url, datagen, headers)
try:
    response = urllib2.urlopen(request)
    print(response.read())
except Exception as e:
    print str(e)

#import requests
#response = requests.post(practice_url, files={"file": open("answer.png", 'r')})
#print response

(pyenv) srimbp:entryExam sri$ python solve.py 
Correct, good job!, <a href="/practice">Try again<a>
"""

# Fetch questions from the server
import urllib2
practice_url = "http://ee.sunshinectf.org/exam"
#questions = urllib2.urlopen(practice_url)
#cookie = [questions.info().dict["set-cookie"]]
#questions = questions.read()
#questions = questions.split("\n")

import requests
questions = requests.get(practice_url)
cookie = questions.cookies
questions = questions.text
questions = questions.split("\n")
print cookie
section = 1
flag = ""
print questions

while "sun" not in flag:
    # Answer sheet open
    filename = "answer.png"
    
    image = Image.open('scantron.png')
    # Answer mark
    mark = Image.open('checkmark.png').convert("RGBA")
    
    # Extract questions and options
    final_answers = []
    types = ""
    import re
    for i in range(len(questions)):
        if re.match("<li>[0-9]+\s+[+-\/*]+\s+[0-9]+<\/li>", questions[i]):
            expression = questions[i].strip("<li>").strip("</li>")
            ans = eval(expression)
            # type
            i += 1
            #types = questions[i].split('"')[1]
            i += 1
            # options
            for j in range(0, 4):
                choice = questions[i].strip("<li>").strip("</li>")
                print expression, ans, choice
                if str(ans) == choice:
                    final_answers.append(j)
                    i += 4 - (j+1)
                    break
                else:
                    i += 1
            # type
            i += 1
    # Find and Mark answers in the answer sheet
    #print final_answers
    image_copy = image.copy()
    for choice in range(len(final_answers)):
        #print choice+1, final_answers[choice]
        position = options[str(choice+1)][final_answers[choice]]
        image_copy.paste(mark, position, mark)
    #image_copy.paste(mark, test_version[alphabet_option[types]], mark)
    # Save and Upload answer sheet to the server
    image_copy.save(filename, format="png")

    """
    # Upload answer sheet to the server
    from poster.encode import multipart_encode
    from poster.streaminghttp import register_openers
    register_openers()
    fd = open(filename)
    datagen, headers = multipart_encode({"file": fd})
    headers["User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    headers["Cookie"] = "; ".join(cookie)
    request = urllib2.Request(practice_url, datagen, headers)

    
    class NoRedirection(urllib2.HTTPErrorProcessor):

        def http_response(self, request, response):
            return response

        https_response = http_response

    
    import cookielib
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(NoRedirection, urllib2.HTTPCookieProcessor(cj))
    data = {}
    response = opener.open(request)
    if response.code == 302:
        redirection_target = response.headers['Location']
        print redirection_target

    

    #try:
    response = urllib2.urlopen(request)
    #print cookieprocessor.cookiejar
    cookie[-1] = cookie[-1].strip("HttpOnly; Path=/")
    current_cookie = response.info().dict["set-cookie"]#.strip("session=")
    cookie.append(current_cookie)
    print cookie
    print response.info().dict
    questions = response.read()
    flag = questions
    questions = questions.split("\n")
    print questions
    #print flag
    #print response.info().dict
    if "Wrong" in flag or "slow" in flag:
        print "Exited as wrong or slow...."
        sys.exit()
    if "sun" in flag:
        print flag
        sys.exit()

    fd.close()
    #except Exception as e:
    #    print e
    """

    # Upload answer sheet to the server
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
    files = {'file': open(filename, 'rb')}
    r = requests.post(practice_url, files=files, cookies=cookie, headers=headers)
    cookie = r.cookies
    questions = r.text
    flag = questions
    if "Wrong" in flag or "slow" in flag:
        print "Exited as wrong or slow...."
        sys.exit()
    if "sun" in flag:
        print flag
        sys.exit()
    questions = questions.split("\n")
    print questions


