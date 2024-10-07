from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

messages = lambda duvida : [SystemMessage('assistente de menssagem, para me ajudar em projetos pessoais de desenvolvedor e no duvidas do  dia a dia, responda a seguinte duvida'), HumanMessage(duvida)]

llm_google = ChatGoogleGenerativeAI(model = "gemini-1.5-pro")

exemplo = "qual e a capital da mongolia"
resposta = llm_google.invoke(messages(exemplo))

print(resposta.content)

# %%
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace, HuggingFacePipeline
from langchain.llms import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch

# Nome do modelo GPT-Neo local (ou GPT-J, se preferir)
model_name = "EleutherAI/gpt-neo-2.7B"

# Baixar e carregar o tokenizer e o modelo localmente
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Configurar o pipeline de inferência com geração de texto
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

hf_pipeline = pipeline(
    "text-generation",  # Tarefa de geração de texto
    model=model, 
    tokenizer=tokenizer, 
    max_new_tokens=512,  # Definir o número máximo de tokens
    do_sample=False,  # Desabilitar amostragem aleatória
    repetition_penalty=1.03,  # Penalidade para evitar repetições
    device=0 if torch.cuda.is_available() else -1  # Usar GPU se disponível
)

# Integrar ao LangChain usando o HuggingFacePipeline
llm_hf = HuggingFacePipeline(pipeline=hf_pipeline)

# Usar em uma cadeia de conversação ou outro tipo de fluxo
chat = ChatHuggingFace(llm=llm_hf, verbose=True)

# Rodar a cadeia com input local
response = chat.invoke(exemplo)
print(response)

# %%
