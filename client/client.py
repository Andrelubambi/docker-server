import requests

def main():
    servidor_url = "http://servidor_v2:8081"

    
    print("Enviando requisição ao servidor ...")
    
    # Requisição GET para a página inicial
    response = requests.get(servidor_url)
    print("StatusCode da requisição: {0}".format(response.status_code))
    print("Conteúdo da resposta: {0}".format(response.text))
    
    # Requisição GET para o endpoint /status
    response_status = requests.get(f"{servidor_url}/status")
    print("StatusCode da requisição ao /status: {0}".format(response_status.status_code))
    print("Conteúdo da resposta do /status: {0}".format(response_status.text))

if __name__ == "__main__":
    main()
