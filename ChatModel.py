# %%
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser,SimpleJsonOutputParser
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

exemplo = "qual e a capital da mongolia"
# Nome do modelo GPT-Neo local (ou GPT-J, se preferir)
model_name = "EleutherAI/gpt-neo-2.7B"

# Integrar ao LangChain usando o HuggingFacePipeline
llm_hf = HuggingFacePipeline.from_model_id(
    model_id="microsoft/Phi-3-mini-4k-instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 100,
        "top_k": 50,
        "temperature": 0.1,
    },
)



llm_groq = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0.0,
    max_retries=2,
    # other params...
)
parser = StrOutputParser()

# Usar em uma cadeia de conversação ou outro tipo de fluxo
chat_hf = ChatHuggingFace(llm=llm_hf, verbose=True)

def parse_chat_response(response):
    # Divida a resposta em partes com base nos delimitadores
    user_message = response.split("<|user|>")[-1].split("<|end|>")[0].strip()
    assistant_message = response.split("<|assistant|>")[-1].strip()

    return {'user' : user_message, 'assistent' : assistant_message}

msg_tmpl = ChatPromptTemplate([
            ('system', "Assistente virtual que tira responde perguntas"),
            ('human', '{quest}')])


# chain = msg_tmpl | chat_hf |  parser | (lambda response: parse_chat_response(response))
chain = msg_tmpl | llm_groq |  parser | (lambda response: parse_chat_response(response))


# %%
if __name__ == "__main__":
    exemplo = "qual e a capital da mongolia"

    response = chain.invoke({'quest' : exemplo})

    parser = parse_chat_response(response)

    print(parser)
