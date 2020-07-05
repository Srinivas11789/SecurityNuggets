# ipv6 network issue, so currently all it binds to is fe80 link local address. 
# Using ngrok helps, the url by default has hex to what we want, and also it can be accessed via a ipv6 address.

# Ref: https://stackoverflow.com/questions/25817848/python-3-does-http-server-support-ipv6
import socket
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
      return SimpleHTTPRequestHandler.do_GET(self)

class HTTPServerV6(HTTPServer):
    address_family = socket.AF_INET6

def main():
  server = HTTPServerV6(('::', 80), MyHandler)
  server.serve_forever()

if __name__ == '__main__':
  main()