import http.server
import socketserver
import json

PORT = 8000

names_dict = {"Alex", "Mihai", "Daniel"}

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_DELETE(self):
        if self.path == '/names':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = 'Hello, world!'
            self.wfile.write(bytes(message, 'utf-8'))
            return
        
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = 'Not found'
        self.wfile.write(bytes(message, 'utf-8'))
        return
    
    def do_GET(self):
        if self.path == '/names':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = json.dumps(names_dict)
            self.wfile.write(bytes(message, 'utf-8'))
            return
        
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = 'Not found'
        self.wfile.write(bytes(message, 'utf-8'))
        return
    
    def do_POST(self):
        if self.path == '/names':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            message = 'Hello, world!'
            self.wfile.write(bytes(message, 'utf-8'))
            return
        
        self.send_response(404)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = 'Not found'
        self.wfile.write(bytes(message, 'utf-8'))
        return
    

with socketserver.TCPServer(("", PORT), MyHttpRequestHandler) as httpd:
    print("server started at port:", PORT)
    httpd.serve_forever()




# def do_DELETE(self):
#     if self.path == '/names':
#         self.send_response(200)
#         self.send_header('Content-type', 'text/html')
#         self.end_headers()
#         message = 'test'
#         self.wfile.write(bytes(message, 'utf-8'))
#         return
    