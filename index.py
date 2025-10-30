import http.server
import socketserver
import os

PORT = int(os.environ.get('PORT', 8000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html_content = '''
                <!DOCTYPE html>
                <html>
                <head>
                    <title>SmartCampus Test</title>
                    <style>
                        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
                        .container { background: white; color: #333; padding: 40px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); max-width: 500px; margin: 0 auto; }
                        .success { color: #2ecc71; font-size: 24px; margin-bottom: 20px; }
                        .info { color: #3498db; margin: 20px 0; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <div class="success">✅ SmartCampus Test Page</div>
                        <p>If you can see this, the server is running correctly!</p>
                        <div class="info">
                            <p><strong>Next step:</strong> Deploy the full application.</p>
                            <p><strong>Status:</strong> <span style="color: #2ecc71;">Working</span></p>
                        </div>
                    </div>
                </body>
                </html>
            '''
            self.wfile.write(html_content.encode('utf-8'))
        else:
            # Serve other files normally
            super().do_GET()

if __name__ == "__main__":
    print(f"🚀 Starting SmartCampus test server on port {PORT}")
    print(f"📍 The app will be available at: http://localhost:{PORT}")
    print("🛑 Press Ctrl+C to stop the server")
    
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped!")
