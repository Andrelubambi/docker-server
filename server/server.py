import datetime
from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Registrando a requisição
        with open("/app/requests.log", "a") as log_file:
            log_file.write(f"[{datetime.datetime.now()}] Requisição recebida de {self.client_address}\n")
        
        # Respondendo ao cliente
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Mensagem do servidor no container Docker!")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), MyHandler)
    print("Servidor rodando na porta 8080...")
    server.serve_forever()
