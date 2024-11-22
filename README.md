from fpdf import FPDF

# Criação do objeto FPDF
pdf = FPDF()

# Adicionando uma página
pdf.add_page()

# Definindo título
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Projeto Docker: Servidor e Cliente", ln=True, align="C")

# Quebra de linha
pdf.ln(10)

# Definindo o conteúdo
content = """
Este projeto utiliza Docker para criar e gerenciar contêineres que simulam a comunicação entre dois serviços: servidor e cliente. O servidor responde a uma requisição do cliente, retornando uma mensagem simples. A seguir, apresento um passo a passo para construir, rodar e entender a estrutura do projeto.

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
│   └── Dockerfile
│
└── client/
    ├── client.py
    └── Dockerfile

## Pré-requisitos

Antes de executar o projeto, é necessário ter o Docker e o Docker Compose instalados no seu sistema.

- [Instalar Docker](https://docs.docker.com/get-docker/)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/)

## Passo a Passo para Executar o Projeto

1. Clone o repositório:
   
   Primeiro, clone o repositório para sua máquina local:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <diretorio_do_repositorio>


2. Construa e inicie os contêineres:

Execute o seguinte comando para baixar as dependências necessárias e construir as imagens dos serviços servidor e cliente:

docker-compose up --build


3. Verifique os contêineres em execução:

Após a execução do comando acima, o Docker irá iniciar os contêineres. Você pode verificar se eles estão rodando com:

docker ps


4. Para parar os contêineres:

Para parar os contêineres, basta rodar o comando:

docker-compose down
