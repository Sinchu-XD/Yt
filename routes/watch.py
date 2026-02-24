from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import StreamingResponse
from services.Yt_Service import get_stream_urls
from YouTubeMusic.Video_Stream import start_ffmpeg_merge
import asyncio

router = APIRouter()

@router.get("/")
async def watch(request: Request, url: str):

    video_url, audio_url = get_stream_urls(url)

    if not video_url:
        raise HTTPException(400, "Invalid YouTube URL")

    process = start_ffmpeg_merge(video_url, audio_url)

    async def stream_generator():
        try:
            while True:
                # Client disconnected?
                if await request.is_disconnected():
                    break

                chunk = await asyncio.to_thread(
                    process.stdout.read, 1024 * 512
                )

                if not chunk:
                    break

                yield chunk

        finally:
            process.kill()
            process.wait()

    return StreamingResponse(
        stream_generator(),
        media_type="video/mp4"
    )
