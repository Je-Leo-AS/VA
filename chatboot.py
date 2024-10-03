
import os
import getpass
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


messages = [SystemMessage("qual e a capital da mongolia"), HumanMessage('assistente de menssagem')]

llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")
resposta = llm.invoke("messages")

print(resposta)

