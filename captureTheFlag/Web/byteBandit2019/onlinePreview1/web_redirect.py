import SimpleHTTPServer
import SocketServer
class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
   def do_GET(self):
       print self.path
       self.send_response(301)
       new_path = '%s%s'%('http://127.0.0.1:1337', self.path)
       self.send_header('Location', new_path)
       self.end_headers()

PORT = 8000
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port 8000"
handler.serve_forever()
