import SimpleHTTPServer
import SocketServer

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
       global count
       print self.path
       self.send_response(302)
       self.send_response(302)
       self.send_response(302)
       if "flag" in self.path:
          self.send_response(301)
          new_path = '%s'%('http://0.0.0.0:1337')
       elif "index9" in self.path:
          new_path = '%s'%('/flag')
       else:
          count = self.path.strip("/")
          count = count.strip("index")
          if count != "":
             count = int(count)+1
          else:
             count = 1
          new_path = '%s'%('/index'+str(count))
       print new_path
       self.send_header('Location', new_path)
       self.end_headers()

PORT = 8000
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port 8000"
handler.serve_forever()
