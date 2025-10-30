def main():
    init_data()
    
    # Get PORT from environment variable (Render provides this)
    PORT = int(os.environ.get('PORT', 8000))
    
    # Ensure we're binding to all interfaces
    with socketserver.TCPServer(("0.0.0.0", PORT), SmartCampusHandler) as httpd:
        print(f"🚀 Server running on port {PORT}")
        print(f"📍 Access URL: https://your-app.onrender.com")
        try:
            httpd.serve_forever()
        except Exception as e:
            print(f"❌ Server error: {e}")
