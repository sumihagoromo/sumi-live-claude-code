#!/usr/bin/env python3
"""
Simple Python HTTP server for serving VTuber landing page
"""

import http.server
import socketserver
import os
import sys

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    PORT = 8000
    
    # Change to the directory containing static files
    web_dir = os.path.join(os.path.dirname(__file__), 'static')
    if os.path.exists(web_dir):
        os.chdir(web_dir)
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"🌸 VTuber Landing Page Server starting...")
        print(f"🚀 Server running at http://localhost:{PORT}")
        print(f"📁 Serving files from: {os.getcwd()}")
        print(f"💫 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n✨ Server stopped gracefully!")
            sys.exit(0)

if __name__ == "__main__":
    main()