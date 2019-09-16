from http.server import HTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie

from io import BytesIO
from urllib.parse import urlparse

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse(self.path)
        message = '\n'.join([
            'CLIENT VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' % self.request_version,
            '',
            'SERVER VALUES:',
            'server_version=%s' % self.server_version,
            'sys_version=%s' % self.sys_version,
            'protocol_version=%s' % self.protocol_version,
            ])
        cookies = SimpleCookie(self.headers.get('Cookie'))
        print(cookies)
        print(message)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello Welcome to my world! \n')

httpd = HTTPServer(('localhost', 3000), SimpleHTTPRequestHandler)
httpd.serve_forever()

# References:
# * https://gist.github.com/trungly/5889154
