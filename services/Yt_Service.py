from YouTubeMusic.Search import Search
from YouTubeMusic.Video_Stream import get_video_audio_urls
from Utils.Cache import get_cache, set_cache

async def search_youtube(query: str):
    cache_key = f"search:{query}"
    cached = get_cache(cache_key)
    if cached:
        return cached

    data = await Search(query, limit=10)

    results = []
    for result in data["main_results"]:
        results.append({
            "video_id": result["url"],
            "title": result["title"],
            "channel": result["channel"],
            "duration": result["duration"],
            "views": result["views"],
            "thumbnail": result["thumbnail"]
        })

    set_cache(cache_key, results)
    return results


def get_stream_urls(video_id: str):
    link = f"https://youtube.com/watch?v={video_id}"
    return get_video_audio_urls(link)
