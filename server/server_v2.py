from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Codificando explicitamente para bytes com UTF-8
        self.wfile.write("<h1>Nova versão do servidor no container Docker!</h1>".encode('utf-8'))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), MyHandler)
    print("Servidor rodando na porta 8080...")
    server.serve_forever()
