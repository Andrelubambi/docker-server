import requests
import time


servidor_url = "http://servidor_v2:8080/status"

def verificar_servidor():
    try:
        # Faz uma requisição GET para o servidor
        response = requests.get(servidor_url)
        if response.status_code == 200:
            print("Servidor está online")
        else:
            print(f"Servidor retornou um erro: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar se conectar ao servidor: {e}")

def main():
    while True:
        verificar_servidor()
        # Espera 10 segundos antes de verificar novamente
        time.sleep(10)

if __name__ == "__main__":
    main()
