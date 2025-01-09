import requests
import json

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
    
    # Requisição GET para o endpoint /hello/{name}
    name = "Joao"
    response_hello = requests.get(f"{servidor_url}/hello/{name}")
    print("StatusCode da requisição ao /hello: {0}".format(response_hello.status_code))
    print(f"Conteúdo da resposta do /hello/{name}: {response_hello.text}")
    
    # Requisição GET para o endpoint /search com parâmetros
    params = {"name": "Joao", "age": "30"}
    response_search = requests.get(f"{servidor_url}/search", params=params)
    print("StatusCode da requisição ao /search: {0}".format(response_search.status_code))
    print("Conteúdo da resposta do /search: {0}".format(response_search.text))
    
    # Requisição POST para o endpoint /echo com dados JSON
    data = {"name": "Joao", "age": 30}
    response_post = requests.post(f"{servidor_url}/echo", json=data)
    print("StatusCode da requisição ao /echo: {0}".format(response_post.status_code))
    print("Conteúdo da resposta do /echo: {0}".format(response_post.text))
    
    # Requisição PUT para o endpoint /update com dados JSON
    update_data = {"id": 1, "name": "Joao", "age": 31}
    response_put = requests.put(f"{servidor_url}/update", json=update_data)
    print("StatusCode da requisição ao /update: {0}".format(response_put.status_code))
    print("Conteúdo da resposta do /update: {0}".format(response_put.text))
    
    # Requisição DELETE para o endpoint /delete
    response_delete = requests.delete(f"{servidor_url}/delete")
    print("StatusCode da requisição ao /delete: {0}".format(response_delete.status_code))
    print("Conteúdo da resposta do /delete: {0}".format(response_delete.text))

if __name__ == "__main__":
    main()
