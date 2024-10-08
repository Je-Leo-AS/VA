# %%
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

exemplo = "qual e a capital da mongolia"


# %%
messages = lambda duvida : [SystemMessage('assistente de menssagem, para me ajudar em projetos pessoais de desenvolvedor e no duvidas do  dia a dia, responda a seguinte duvida'), HumanMessage(duvida)]

llm_google = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

resposta = llm_google.invoke(messages(exemplo))

print(resposta.content)
# %%
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
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

# Usar em uma cadeia de conversação ou outro tipo de fluxo
chat_hf = ChatHuggingFace(llm=llm_hf, verbose=True)



# %%
exemplo = "qual e a capital da mongolia"

response = chat_hf.invoke(exemplo)
print(response)

# %%
