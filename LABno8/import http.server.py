import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT),Handler) as httpd:
    print("Serving port ", PORT)
    httpd.serve_forever()