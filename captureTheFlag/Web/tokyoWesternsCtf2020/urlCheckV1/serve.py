from http.server import HTTPServer, BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("respond: ")
        print(self.headers)
        print(self.path)
        print("GET request for {}".format(self.path).encode('utf-8'))
        self.send_response(301)
        self.send_header("Location", 'http://0177.0.0.01/admin-status')
        #self.send_header("Location", 'http://127.0.0.1/admin-status')
        self.end_headers()
httpd = HTTPServer(('0.0.0.0', 80), SimpleHTTPRequestHandler)
httpd.serve_forever()

### Reference octal ip localhost --> https://www.hacksparrow.com/networking/many-faces-of-ip-address.html