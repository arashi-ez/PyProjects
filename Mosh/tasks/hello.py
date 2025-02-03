from http.server import HTTPServer, BaseHTTPRequestHandler

class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        html = '<h1 style="padding:50px">Greetings from Vultr</h1>'
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(html, 'utf-8'))

httpd = HTTPServer(('0.0.0.0', 5000), Serv)
print("Web server is listening on port 5000\nPress Ctrl+C to stop...")
httpd.serve_forever()
