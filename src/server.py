import http.server
import socketserver
import threading
import os

class LocalServer:
    def __init__(self, directory, port=8000):
        self.directory = directory
        self.port = port
        self.httpd = None
        self.thread = None

    def start(self):
        os.chdir(self.directory)
        handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", self.port), handler)
        self.thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
        self.thread.start()
        return f"Server started on http://localhost:{self.port}"

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()
            self.httpd.server_close()
            return "Server stopped"
        return "No active server"

