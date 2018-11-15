import os, re, sys
import requests
import pytesseract
from selenium import webdriver

### STEP1 - Obtain Data

# Use selenium to grab a screen shot of the webpage
driver = webdriver.Firefox()
driver.get('https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad')
element = driver.find_elements_by_tag_name('p')

# Html source, token and expression
htmls = driver.page_source
text = element[0].text
t = "".join(list(text))
tok = driver.find_element_by_name("token")
token = tok.get_attribute("value")
var = list(set(t))
vars = []
for ch in var:
    if ch.strip():
       vars.append(ch)
print vars
print htmls

### STEP2 - OCR - Recogize and Map

html = htmls.replace(text, " ".join(vars))
#print html
new_html = open("new.html","w")
new_html.write(str(html))
new_html.close()
alt_html = "file://"+os.path.abspath("new.html")
driver.get(alt_html)
screenshot = driver.save_screenshot('expression.png')
driver.quit()
expression = pytesseract.image_to_string(Image.open("expression.png"))
expression =  expression.split()[1]
expression = list(expression)
print vars, expression


### STEP3 - Construct expression

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


### STEP4 - Submit the answer

url = "https://hidden-island-93990.squarectf.com/ea6c95c6d0ff24545cad"
data = dict(token=token, answer=str(ans))
r = requests.post(url, data=data, allow_redirects=True)
print r.content

