from YouTubeMusic.Stream import get_stream

async def ytdl_audio(url: str):
    try:
        stream_url = get_stream(url)
        if not stream_url:
            return False, "Failed to get audio stream URL"
        return True, stream_url
    except Exception as e:
        return False, str(e)
