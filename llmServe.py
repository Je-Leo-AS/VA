from chatboot import llm
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI(title='Meu chat', description='chatboot para uso pessoal')

add_routes(app, llm, path='/chat')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, "localhost", 9090)