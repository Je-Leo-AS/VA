import speech_recognition as sr
import pyttsx3
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize the recognizer
r = sr.Recognizer()

# Função para capturar áudio e reconhecer fala
def recognize_speech():
    with sr.Microphone() as source:
        print("Fale algo...")
        audio = r.listen(source)

        try:
            # Reconhece a fala usando o Google Web Speech API
            text = r.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Web Speech não conseguiu entender o áudio.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do Google Web Speech; {e}")
        return ""

recognized_text = recognize_speech()

if recognized_text:
    # Processando o texto com Langchain
    prompt = PromptTemplate(template="reescrevra esse texto de iutra maneira: {input}", input_variables=["input"])
    llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(input=recognized_text)

    print("Resposta da IA:", response)
