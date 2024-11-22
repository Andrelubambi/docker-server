from http.server import SimpleHTTPRequestHandler, HTTPServer
import time

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {
                "server_time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "status": "Server is running in Docker!"
            }
            self.wfile.write(bytes(str(status), "utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write("<h1>Nova versão do servidor no container Docker!</h1>".encode('utf-8'))


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8081), MyHandler)
    print("Servidor rodando na porta 8081...")
    server.serve_forever()
