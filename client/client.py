import requests
import time

def request_to_server():
    try:
        print("Enviando requisição ao servidor ...")
        response = requests.get("http://servidor:8080")
        print(f"StatusCode da requisição: {response.status_code}")
        print("Conteúdo da resposta:", response.text)
    except Exception as e:
        print("Erro ao fazer requisição:", e)

if __name__ == "__main__":
    request_to_server()
   ## time.sleep(60)  # Mantém o cliente em execução por 60 segundos após a requisição
