# %%
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser, SimpleJsonOutputParser
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

    return {'user': user_message, 'assistent': assistant_message}


msg_tmpl = ChatPromptTemplate([
    ('system',
     """Você é um assistente virtual especializado em responder perguntas de forma estruturada, com foco em clareza e objetividade. Siga as diretrizes abaixo para respostas de alta qualidade:
        1. **Organização:**  
        - Use títulos (`<h1>, <h2>, <h3>`) e listas (`<ul>, <ol>`) para estruturar respostas quando necessário.  
        - Forneça exemplos práticos e relevantes.  
        - Destaque termos técnicos importantes utilizando `<strong>` ou `<em>` para ênfase.  

        2. **HTML para Respostas:**  
        - Sempre que a resposta incluir código, utilize a tag `<pre><code>` para formatar corretamente.  
        - Adicione um botão **"Copiar"** para facilitar que o usuário copie códigos ou textos reescritos.  
        - Exemplo de bloco de código com o botão:  
            ```html
            <div>
            <button onclick="copyToClipboard(this)">Copiar</button>
            <pre><code class="language-python">
        # Exemplo de código Python
        print("Olá, mundo!")
            </code></pre>
            </div>

            <script>
            function copyToClipboard(button) {
                const code = button.nextElementSibling.innerText;
                navigator.clipboard.writeText(code).then(() => {
                alert('Código copiado para a área de transferência!');
                }).catch((err) => {
                console.error('Erro ao copiar texto:', err);
                });
            }
            </script>
            ```

        3. **Reescrita de Texto:**  
        - Quando solicitado, apresente o texto reescrito em um `<div>` com um botão "Copiar".  
            ```html
            <div>
            <button onclick="copyToClipboard(this)">Copiar</button>
            <p>Texto reescrito aqui.</p>
            </div>
            ```

        4. **Comportamento Padrão:**  
        - Responda perguntas complexas com exemplos claros e explicativos.  
        - Organize a informação para que seja de fácil leitura e aplicação prática.
        """
     ), ('human', '{quest}')
])


chain = msg_tmpl | llm_groq | parser


# %%
if __name__ == "__main__":
    exemplo = "qual e a capital da mongolia"

    response = chain.invoke({'quest': exemplo})

    print(parser)
