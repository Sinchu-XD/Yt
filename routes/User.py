from fastapi import APIRouter
from database import history_col
from datetime import datetime

router = APIRouter()

@router.post("/history")
async def save_history(user_id: str, video_id: str):
    history_col.insert_one({
        "user_id": user_id,
        "url": url,
        "watched_at": datetime.utcnow()
    })
    return {"status": "saved"}

@router.get("/history/{user_id}")
async def get_history(user_id: str):
    data = list(history_col.find({"user_id": user_id}, {"_id": 0}))
    return data
