import os, re, sys
import urllib2, requests
import subprocess
import base64
import StringIO
from io import BytesIO
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import pytesseract
from PIL import Image
from PIL import ImageEnhance, ImageFilter

# Use selenium to grab a screen shot of the webpage
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad')
element = driver.find_elements_by_tag_name('p')

#for i,t in enumerate(element):
#    print t.text, i
#location = element[0].location
#size = element[0].size
#screenshot = driver.save_screenshot('expression.png')

htmls = driver.page_source
text = element[0].text
t = "".join(list(text))
#print t
tok = driver.find_element_by_name("token")
token = tok.get_attribute("value")
#sys.exit()
var = list(set(t))
#vars = filter(" ", vars)
vars = []
for ch in var:
    if ch.strip():
       vars.append(ch)
print vars
print htmls
#html = re.sub(r'<p>.*</p>', htmls, "</p>"+" ".join(vars))
html = htmls.replace(text, " ".join(vars))
print html
new_html = open("new.html","w")
new_html.write(str(html))
new_html.close()
alt_html = "file://"+os.path.abspath("new.html")
driver.get(alt_html)
screenshot = driver.save_screenshot('expression.png')

#size = (0, 50, 100, 110)
#image = Image.open(StringIO.StringIO(screenshot))
#region = image.crop(size)
#region.save('expression.png', 'PNG', optimize=True, quality=105)

driver.quit()

# OCR - Not very reliable

#image = Image.open('expression.png')

#image.save("expression.png", dpi=(600,600))

#im = Image.open(BytesIO(screenshot))
#left = location['x'] + 100
#top = location['y'] + 100
#right = location['x'] + size['width']
#bottom = location['y'] + size['height']
#im = im.crop((left, top, right, bottom)) # defines crop points
#im.save('expression.png') # saves new cropped image

#image.filter(ImageFilter.SHARPEN)
#new_size = tuple(2*x for x in image.size)
#image = image.resize(new_size, Image.ANTIALIAS)
#image.save('expression.png')
#im = Image.open("expression.png") # the second one 
#im = im.filter(ImageFilter.MedianFilter())
#enhancer = ImageEnhance.Contrast(im)
#im = enhancer.enhance(2)
#im = im.convert('1')
#im.save('expression.png')
#0123456789+xX-/*

expression = pytesseract.image_to_string(Image.open("expression.png"))

"""
api_key = "4129d1319788957"
image = open("expression.png", "r")
data = base64.b64encode(image.read())
expression = subprocess.check_output('curl -H "apikey:%s" --form "base64Image=data:image/png;base64,/9j/AAQSk %s" --form "language=eng" --form "isOverlayRequired=false" https://api.ocr.space/parse/image' % (api_key, data))
"""
expression =  expression.split()[1]
expression = list(expression)

print vars, expression

for k,v in zip(vars, expression):
    text = text.replace(k, v)

print text

# Replace x or X and solve
#expr = expression.split("\n")[1]
expr = text.replace("x","*")
expr = expr.replace("X","*")
print expr
ans =  eval(expr)
print ans



url = "https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad"
data = dict(token=token, answer=str(ans))
r = requests.post(url, data=data, allow_redirects=True)
print r.content

"""
# Old method
# Get the html page
headers = { 'User-Agent' : 'Mozilla/5.0' }
req = urllib2.Request('https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad', None, headers)
web_page = urllib2.urlopen(req)
content = web_page.read()
#print content

# Extract the expression
parsed_html = BeautifulSoup(content)
expression = parsed_html.body.find('p').text

# Replace para with ascii mapping characters to map
#map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#map = "1234567890"
#map_ascii = parsed_html.new_tag('p', id='map')
#map_ascii.append(map)
#parsed_html.body.append(map_ascii)
#new_html = open("new.html","w")
#new_html.write(str(parsed_html))
#new_html.close()

# Fetch the output and create a mapping
#alt_html = "file://"+os.path.abspath("new.html")
#web_page2 = urllib2.urlopen(alt_html)
#content2 = web_page2.read()
#print content2

# Construct the expression - the refresh seems to be every 5 seconds, variables should be cracked by then
symbols = list(set(expression))
print symbols

# Return the solution of the expression
"""
