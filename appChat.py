from ChatModel import *
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from langserve import add_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Meu chat', description='chatboot para uso pessoal')


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)


add_routes(app, chain_html, path='/chat')

@app.get("/chat")
async def serve_index():
    return FileResponse("index.html", media_type="text/html")

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data["message"]
    response = chain_html.invoke({'quest' : message})
    return {"response": response}

@app.get("/chat/history")
async def chat(request: Request):
    return {"chat_history": []}

if __name__ == "__main__":
    import uvicorn
    import nest_asyncio
    nest_asyncio.apply()
    uvicorn.run(app, host="0.0.0.0", port=9090)