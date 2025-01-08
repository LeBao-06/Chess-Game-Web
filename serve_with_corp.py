from http.server import HTTPServer, SimpleHTTPRequestHandler

class CORPHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

# Start the server on localhost:8080
httpd = HTTPServer(('localhost', 8080), CORPHandler)
print("Serving on http://localhost:8080")
httpd.serve_forever()
