from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app.search_logic import SearchYt
from app.stream_logic import get_video_audio_urls, stream_merged

# 🔥 FIRST create app
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# -----------------------
# HOME PAGE
# -----------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# -----------------------
# SEARCH API
# -----------------------
@app.get("/search")
async def search(q: str):
    data, url = await SearchYt(q)
    return {"result": data, "url": url}


# -----------------------
# WATCH (Highest Quality Merged Stream)
# -----------------------
@app.get("/watch")
async def watch(url: str):
    video_url, audio_url = get_video_audio_urls(url)

    if not video_url:
        return {"error": "Failed to get streams"}

    return stream_merged(video_url, audio_url)
