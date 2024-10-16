# %%
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser,SimpleJsonOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

exemplo = "qual e a capital da mongolia"


llm_groq = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.0,
    max_retries=2,
    # other params...
)
parser = StrOutputParser()

    
def parse_chat_response(response):
    # Divida a resposta em partes com base nos delimitadores

    user_message = response.split("<|user|>")[-1].split("<|end|>")[0].strip()
    assistant_message = response.split("<|assistant|>")[-1].strip()

    return {'user' : user_message, 'assistent' : assistant_message}

msg_tmpl = ChatPromptTemplate([
    ('system', 
     """Você é um assistente virtual especializado em responder perguntas de forma estruturada, com foco em clareza e objetividade. 
     Siga as diretrizes abaixo para respostas de qualidade:
     
     1. **Organização:**  
        - Use títulos, subtítulos, listas numeradas e bullets para estruturar respostas quando necessário.
        - Forneça exemplos práticos e relevantes.
        - Destaque trechos importantes ou termos técnicos relevantes.
        
     2. **Markdown:**  
        - Sempre que a resposta incluir código, utilize blocos de markdown e destaque a linguagem do código utilizando a notação (```nome da linguagem código ```) como por exemplo:
          ```python
          # Exemplo de código Python
          print("Olá, mundo!")
          ```
        - Adicione um botão de **"Copiar"** o codigo para facilitar a usabilidade.
        - Caso eu peça para reescrever um texto Adicione um botão de **"Copiar"** para facilitar a usabilidade.
        
     4. **Comportamento Padrão:**  
        - Responda perguntas complexas com exemplos claros e bem explicados.
        - Organize a informação para que seja de fácil leitura e prática de aplicar.
        """),

    ('human', '{quest}')
])


chain = msg_tmpl | llm_groq |  parser


# %%
if __name__ == "__main__":
    exemplo = "qual e a capital da mongolia"

    response = chain.invoke({'quest' : exemplo})

    print(parser)
