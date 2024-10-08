from ChatModel import *
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title='Meu chat', description='chatboot para uso pessoal')

add_routes(app, chain, path='/chat')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9090)
        
    