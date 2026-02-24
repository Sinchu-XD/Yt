from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from app.search_logic import SearchYt
from app.stream_logic import ytdl_audio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search")
async def search(q: str):
    data, url = await SearchYt(q)
    return {"result": data, "url": url}

@app.get("/stream")
async def stream(url: str):
    success, result = await ytdl_audio(url)
    return {"success": success, "stream": result}
