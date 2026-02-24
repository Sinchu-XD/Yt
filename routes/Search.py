from fastapi import APIRouter
from services.Yt_Service import search_youtube

router = APIRouter()

@router.get("/")
async def search(q: str):
    return await search_youtube(q)
