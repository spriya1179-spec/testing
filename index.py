import http.server
import socketserver
import os
import json

PORT = int(os.environ.get('PORT', 8000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>SmartCampus Test</title>
                    <style>
                        body { font-family: Arial; text-align: center; padding: 50px; }
                        .success { color: green; }
                    </style>
                </head>
                <body>
                    <h1 class="success">✅ SmartCampus Test Page</h1>
                    <p>If you can see this, the server is running!</p>
                    <p>Next step: Deploy the full application.</p>
                </body>
                </html>
            ''')
        else:
            super().do_GET()

print(f"Starting server on port {PORT}")
with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    httpd.serve_forever()
