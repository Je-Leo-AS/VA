# %%
import os
import google.generativeai as genai
from langchain_google_vertexai import ChatVertexAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


model_genai = genai.GenerativeModel(model_name="gemini-1.5-flash")
# %%
caminho_imagem = "teste.png"  


def carregar_imagem(caminho_imagem):
    """Carrega uma imagem do disco e a converte para Base64."""
    with open(caminho_imagem, "rb") as imagem:
        return imagem.read()



def recognizer_image(image_array, message):
    chat_session = model_genai.start_chat(history=[{"role": "user", "parts": [ {"mime_type": "image/png", "data": image_array}]}])
    return chat_session.send_message(message)


# %%

if __name__ == "__main__":
    quest = "descreva essa imagem com detalhes, por exemplo que esta escrito? que formas voce? tem alguma coisa escrita?"

    response = recognizer_image(carregar_imagem(caminho_imagem),quest)

    print("Reconhecimento de Imagem:", response.text)

# %%
