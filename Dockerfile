# Use a imagem base do Node.js
FROM node:14

# Instale o Python e pip
RUN apt-get update && apt-get install -y python3 python3-pip curl

# Instale o Ollama
RUN curl -fsSL https://ollama.ai/install.sh | sh

# Inicie o Ollama em segundo plano
RUN ollama serve &

# Baixe o modelo DeepSeek-V3 (ou um modelo similar)
RUN ollama pull deepseek-chat

# Defina o diretório de trabalho no contêiner
WORKDIR /usr/src/app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . .

# Instale as dependências do Python
RUN pip3 install -r requirements.txt

# Instale o servidor HTTP simples
RUN npm install -g http-server

# Exponha a porta que o servidor HTTP usará
EXPOSE 8080

# Comando para iniciar o servidor HTTP e o appChat.py
CMD ["sh", "-c", "python3 appChat.py & http-server -p 8080"]