## Estrutura do Projeto

O projeto é composto por dois serviços:

- Servidor: Contém a aplicação que responde às requisições HTTP do cliente.
- Cliente: Realiza requisições HTTP para o servidor e exibe a resposta.

A estrutura do projeto é a seguinte:

servidor-docker
│
├── docker-compose.yml
│
├── README.md
│
├── server/
│   ├── server.py
│   ├── Dockerfile
│   ├── server_v2.py        
│   └── Dockerfile.v2       
│    
├── client/
│   ├── client.py
│   └── Dockerfile
│
└── monitor/                 
    ├── Dockerfile          
    └── monitor.py           


## Pré-requisitos




Aqui estão os passos para iniciar um contêiner Docker, verificar seu status e interagir com ele para executar o servidor:

1. Iniciar o contêiner
Certifique-se de que seu docker-compose.yml está configurado corretamente e inicie o contêiner:

bash
Copiar código
sudo docker-compose up --build
O parâmetro --build força a reconstrução das imagens Docker caso tenha feito alterações no código ou no Dockerfile.
Para rodar em segundo plano (modo "detached"):
bash
Copiar código
sudo docker-compose up -d
2. Verificar se o contêiner está em execução
Liste os contêineres ativos:

bash
Copiar código
sudo docker ps
Exemplo de saída:

bash
Copiar código
CONTAINER ID   IMAGE                         COMMAND               STATUS              PORTS                     NAMES
abc123456789   servidor-docker_servidor_v2   "python server.py"    Up 2 minutes        0.0.0.0:8081->8080/tcp    servidor_v2
STATUS indica se o contêiner está rodando.
PORTS mostra os mapeamentos de porta (ex.: 8081->8080).
NAMES mostra o nome do contêiner (ex.: servidor_v2).
3. Exibir logs do contêiner
Confira os logs para verificar se o servidor foi inicializado corretamente:

bash
Copiar código
sudo docker logs servidor_v2
Se o servidor não estiver rodando, os logs geralmente mostram mensagens de erro.

4. Verificar o estado detalhado do contêiner
Para obter informações detalhadas do contêiner:

bash
Copiar código
sudo docker inspect servidor_v2
Isso exibe informações sobre a configuração, estado, redes, e muito mais.

5. Acessar o terminal do contêiner
Para interagir diretamente com o contêiner:

bash
Copiar código
sudo docker exec -it servidor_v2 bash
Dentro do contêiner:

Verifique os processos ativos:
bash
Copiar código
ps aux
Teste o servidor:
bash
Copiar código
curl http://localhost:8080/status
6. Reiniciar ou parar o contêiner
Reiniciar:
bash
Copiar código
sudo docker restart servidor_v2
Parar:


Antes de executar o projeto, é necessário ter o Docker e o Docker Compose instalados no seu sistema.

- [Instalar Docker](https://docs.docker.com/get-docker/)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## Passo a Passo para Executar o Projeto

1. Clone o repositório:
   
   Primeiro, clone o repositório para sua máquina local:

   ```bash
   git clone https://github.com/Andrelubambi/docker-server.git


2. Construa e inicie os contêineres:

`sudo docker-compose up --build`



### 3. Verifique os contêineres em execução:

`sudo docker ps`
`sudo docker-compose up`


### 4. Para parar os contêineres:

`docker-compose down`


### Exibe estado do Container
`sudo docker-compose ps`

### 5. Rodar o server_v2.py
`python3 server_v2.py`


### Logs em tempo real 
`sudo docker-compose logs -f servidor`


# Detalhamento das Rotas e Métodos HTTP

## 1. **GET /status**
- **Método HTTP:** `GET`
- **Descrição:** Retorna o status do servidor e o tempo atual.
- **O que deve ser enviado:** Nenhum parâmetro de entrada.
- **Resposta:**
    - **Código de status:** `200 OK`
    - **Tipo de conteúdo:** `application/json`
    - **Corpo da resposta:**
    ```json
    {
        "server_time": "YYYY-MM-DD HH:MM:SS",
        "status": "Server is running in Docker!"
    }
    ```
    - **Exemplo de resposta:**
    ```json
    {
        "server_time": "2024-11-22 14:20:10",
        "status": "Server is running in Docker!"
    }
    ```

## 2. **GET /hello/{name}**
- **Método HTTP:** `GET`
- **Descrição:** Exibe uma mensagem de saudação personalizada com o nome fornecido na URL.
- **O que deve ser enviado:** O nome a ser saudado, passado como parte da URL.
- **Resposta:**
    - **Código de status:** `200 OK`
    - **Tipo de conteúdo:** `text/html`
    - **Corpo da resposta:** 
    ```html
    <h1>Hello, {name}!</h1>
    ```
    - **Exemplo de resposta:**
    ```html
    <h1>Hello, John!</h1>
    ```

## 3. **GET /search?query={query}**
- **Método HTTP:** `GET`
- **Descrição:** Realiza uma pesquisa usando os parâmetros de consulta passados na URL.
- **O que deve ser enviado:** Um ou mais parâmetros de consulta (query parameters) na URL, como `?query=value`.
- **Resposta:**
    - **Código de status:** `200 OK`
    - **Tipo de conteúdo:** `application/json`
    - **Corpo da resposta:**
    ```json
    {
        "search_results": {
            "query": "value"
        }
    }
    ```
    - **Exemplo de resposta:**
    ```json
    {
        "search_results": {
            "query": "example"
        }
    }
    ```

## 4. **GET /info**
- **Método HTTP:** `GET`
- **Descrição:** Retorna informações sobre a versão da API e o tempo do servidor.
- **O que deve ser enviado:** Nenhum parâmetro de entrada.
- **Resposta:**sudo sy
    - **Código de status:** `200 OK`
    - **Tipo de conteúdo:** `application/json`
    - **Corpo da resposta:**
    ```json
    {
        "api_version": "1.0",
        "server_time": "YYYY-MM-DD HH:MM:SS",
        "status": "API is running successfully!"
    }
    ```
    - **Exemplo de resposta:**
    ```json
    {
        "api_version": "1.0",
        "server_time": "2024-11-22 14:25:30",
        "status": "API is running successfully!"
    }
    ```

## 5. **GET /error**
- **Método HTTP:** `GET`
- **Descrição:** Simula um erro no servidor.
- **O que deve ser enviado:** Nenhum parâmetro de entrada.
- **Resposta:**
    - **Código de status:** `500 Internal Server Error`
    - **Tipo de conteúdo:** `application/json`
    - **Corpo da resposta:**
    ```json
    {
        "error": "Something went wrong!"
    }
    ```
    - **Exemplo de resposta:**
    ```json
    {
        "error": "Something went wrong!"
    }
    ```

## 6. **POST /echo**
- **Método HTTP:** `POST`
- **Descrição:** Recebe dados JSON no corpo da requisição e retorna os dados recebidos.
- **O que deve ser enviado:** Um corpo de requisição contendo dados em formato JSON. Exemplo:
    ```json
    {
        "name": "John",
        "age": 30
    }
    ```
- **Resposta:**
    - **Código de status:** `200 OK`
    - **Tipo de conteúdo:** `application/json`
    - **Corpo da resposta:**
    ```json
    {
        "received_data": {
            "name": "John",
            "age": 30
        }
    }
    ```
    - **Exemplo de resposta:**
    ```json
    {
        "received_data": {
            "name": "John",
            "age": 30
        }
    }
    ```

## 7. **PUT /update**
- **Método HTTP:** `PUT`
- **Descrição:** Recebe dados JSON no corpo da requisição e retorna uma mensagem confirmando que os dados foram atualizados.
- **O que deve ser enviado:** Um corpo de requisição contendo dados em formato JSON. Exemplo:
    ```json
    {
        "id": 1,
        "name": "Updated Name"
    }
    ```
- **Resposta:**
    - **Código de status:** `200 OK`
    - **Tipo de conteúdo:** `application/json`
    - **Corpo da resposta:**
    ```json
    {
        "message": "Data updated successfully",
        "updated_data": {
            "id": 1,
            "name": "Updated Name"
        }
    }
    ```
    - **Exemplo de resposta:**
    ```json
    {
        "message": "Data updated successfully",
        "updated_data": {
            "id": 1,
            "name": "Updated Name"
        }
    }
    ```

## 8. **DELETE /delete**
- **Método HTTP:** `DELETE`
- **Descrição:** Simula a exclusão de dados e retorna uma mensagem confirmando que os dados foram excluídos.
- **O que deve ser enviado:** Nenhum parâmetro de entrada.
- **Resposta:**
    - **Código de status:** `200 OK`
    - **Tipo de conteúdo:** `application/json`
    - **Corpo da resposta:**
    ```json
    {
        "message": "Data deleted successfully"
    }
    ```
    - **Exemplo de resposta:**
    ```json
    {
        "message": "Data deleted successfully"
    }
    ```

---
### Notas
- **Tratamento de Erros:** Se uma rota não corresponder a nenhuma das definidas, o servidor irá retornar uma resposta de erro 404 com a mensagem:
  ```json
  {
      "error": "Resource not found",
      "path": "/caminho/errado"
  }
