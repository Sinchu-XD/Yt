from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from services.Yt_Service import get_stream_urls
from YouTubeMusic.Video_Stream import start_ffmpeg_merge

router = APIRouter()

@router.get("/{video_id}")
async def watch(video_id: str):

    video_url, audio_url = get_stream_urls(video_id)

    if not video_url:
        raise HTTPException(404, "Stream not found")

    process = start_ffmpeg_merge(video_url, audio_url)

    async def generator():
        try:
            while True:
                chunk = process.stdout.read(1024 * 1024)
                if not chunk:
                    break
                yield chunk
        finally:
            process.kill()
            process.wait()

    return StreamingResponse(generator(), media_type="video/mp4")
