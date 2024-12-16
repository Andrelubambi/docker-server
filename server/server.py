from http.server import SimpleHTTPRequestHandler, HTTPServer
import time
import json
from urllib.parse import parse_qs

class MyHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {
                "server_time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Servidor está rodando no Docker!"
            }
            self.wfile.write(bytes(json.dumps(status), "utf-8"))
        
        elif self.path.startswith('/hello'):
            name = self.path.split('/')[-1]
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"<h1>Hello, {name}!</h1>".encode('utf-8'))
        
        elif self.path.startswith('/search'):
            query_params = parse_qs(self.path.split('?')[1])
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "search_results": query_params
            }
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "api_version": "1.0",
                "server_time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "API está rodando como esperado!"
            }
            self.wfile.write(bytes(json.dumps(info), "utf-8"))
        
        elif self.path == '/error':
            self.send_response(500)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {
                "error": "Alguma coisa falhou!"
            }
            self.wfile.write(bytes(json.dumps(error_message), "utf-8"))
        
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {
                "error": "Resource not found",
                "path": self.path
            }
            self.wfile.write(bytes(json.dumps(error_message), "utf-8"))

    def do_POST(self):
        if self.path == '/echo':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "received_data": data
            }
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            self.handle_404()

    def do_PUT(self):
        if self.path == '/update':
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            data = json.loads(put_data)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "message": "Data updated successfully",
                "updated_data": data
            }
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            self.handle_404()
    
    def do_DELETE(self):
        if self.path == '/delete':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {
                "message": "Data deleted successfully"
            }
            self.wfile.write(bytes(json.dumps(response), "utf-8"))
        else:
            self.handle_404()

    def handle_404(self):
        self.send_response(404)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        error_message = {
            "error": "Resource not found",
            "path": self.path
        }
        self.wfile.write(bytes(json.dumps(error_message), "utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8081), MyHandler)
    print("Servidor rodando na porta 8081...")
    server.serve_forever()