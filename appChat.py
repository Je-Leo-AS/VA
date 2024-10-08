from chatboot import *
from fastapi import FastAPI
from langserve import add_routes
from txt2speech import *

app = FastAPI(title='Meu chat', description='chatboot para uso pessoal')

add_routes(app, llm_hf, path='/chat')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, "localhost", 9090)


while(1):    
    
    # Exception handling to handle
    # exceptions at the runtime
    audio2 = listen_()
    if  audio2:
    # use the microphone as source for input.
       
        print(f"Did you say : {recognizer(audio2)}")
        
    