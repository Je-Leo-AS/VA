# %%
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser, SimpleJsonOutputParser
from langchain_groq import ChatGroq
from langchain_ollama.chat_models import ChatOllama
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

exemplo = "qual e a capital da mongolia"


llm = ChatOllama(
    model="deepseek-chat",  # Substitua pelo nome do modelo que você baixou
    base_url="http://localhost:11434",  # URL do Ollama rodando localmente
)

parser = StrOutputParser()


def parse_chat_response(response):
    # Divida a resposta em partes com base nos delimitadores

    user_message = response.split("<|user|>")[-1].split("<|end|>")[0].strip()
    assistant_message = response.split("<|assistant|>")[-1].strip()

    return {'user': user_message, 'assistent': assistant_message}


msg_tmpl = ChatPromptTemplate([
    ('system',
     """Você é um assistente virtual que responde de forma clara e objetiva. Suas respostas devem ser formatadas em HTML, utilizando a seguinte estrutura:

1. **Títulos e subtítulos** para organizar a informação.
2. **Parágrafos claros** para explicar conceitos de forma concisa.
3. **Listas numeradas ou com marcadores**, conforme necessário.
4. **Blocos de código ou texto destacado** em `<pre><code>` para respostas com reescritas de texto ou exemplos de código. Adicione um botão funcional para copiar o conteúdo diretamente.

Aqui está um exemplo da estrutura esperada:

<h1>Título da Resposta</h1>
<p>Esta é uma explicação clara e objetiva da questão.</p>

<h2>Subtítulo relevante</h2>
<ul>
  <li>Ponto 1</li>
  <li>Ponto 2</li>
</ul>

<h3>Exemplo de Código</h3>
<pre><code>// Exemplo de código em Python
print('Hello, World!')
</code></pre>
<button onclick="navigator.clipboard.writeText('// Exemplo de código em Python\nprint(\'Hello, World!\');')">
  Copiar Código
</button>

Siga sempre este formato para garantir que a resposta esteja organizada e clara. Use esta estrutura também para **trechos reescritos de texto** ou **blocos de exemplo**.
"""
     ), ('human', '{quest}')
])


chain_html = msg_tmpl | llm | parser


# %%
if __name__ == "__main__":
    exemplo = "qual e a capital da mongolia"

    response = chain_html.invoke({'quest': exemplo})

    print(parser)
