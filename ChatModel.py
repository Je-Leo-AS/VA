from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

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

# Usar em uma cadeia de conversação ou outro tipo de fluxo
chat_hf = ChatHuggingFace(llm=llm_hf, verbose=True)

def parse_chat_response(response):
    # Divida a resposta em partes com base nos delimitadores
    response = response.content
    user_message = response.split("<|user|>")[-1].split("<|end|>")[0].strip()
    assistant_message = response.split("<|assistant|>")[-1].strip()

    return {'user' : user_message, 'assistent' : assistant_message}
# %%
if __name__ == "__main__":
    exemplo = "qual e a capital da mongolia"

    response = chat_hf.invoke(exemplo)

    parser = parse_chat_response(response)

    print(parser)
