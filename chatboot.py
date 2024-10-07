from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

messages = lambda duvida : [SystemMessage(duvida), HumanMessage('assistente de menssagem, para me ajudar em projetos pessoais de desenvolvedor e no duvidas do  dia a dia')]

llm = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

exemplo = "qual e a capital da mongolia"
resposta = llm.invoke(messages(exemplo))

print(resposta.content)



