FROM python:3.10-slim

# Instalar dependências necessárias
RUN apt-get update && apt-get install -y curl && apt-get clean

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o monitor.py para dentro do container
COPY monitor.py .

# Instalar a biblioteca requests
RUN pip install requests

# Comando para rodar o monitor
CMD ["python", "monitor.py"]
