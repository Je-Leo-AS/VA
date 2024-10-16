# %%
import os
import base64
from langchain.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain.memory import ConversationBufferMemory
from langchain_google_vertexai import GemmaVertexAIModelGarden, GemmaChatVertexAIModelGarden
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

llm_google = GoogleGenerativeAI(model = "gemini-1.5-flash")

# %%

def carregar_imagem_base64(caminho_imagem):
    """Carrega uma imagem do disco e a converte para Base64."""
    with open(caminho_imagem, "rb") as imagem:
        # Lê a imagem e a codifica em Base64
        imagem_base64 = base64.b64encode(imagem.read()).decode("utf-8")
    return imagem_base64

def reconhecer_imagem(image_base64):

    message = HumanMessage(
                content=[
                    {"type": "text", "text": "descreva essa imagem com detalhes, por exemplo que esta escrito? que formas voce"},
                    {
                        "type": "image",
                        "image": {"data":image_base64},
                    },
                ],
            )
    # Chama o modelo para obter a resposta
    resultado = llm_google.invoke([message])
    return resultado
# %%
    

# Teste com uma imagem local
caminho_imagem = "teste.png"  # Atualize para o caminho da sua imagem
imagem_base64 = carregar_imagem_base64(caminho_imagem)
resultado_imagem = reconhecer_imagem(imagem_base64)
print("Reconhecimento de Imagem:", resultado_imagem)

# %%
