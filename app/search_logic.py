from YouTubeMusic.Search import Search

async def SearchYt(query: str):
    results = await Search(query, limit=1)

    if not results or not results.get("main_results"):
        return [], None

    item = results["main_results"][0]

    search_data = [{
        "title": item.get("title"),
        "duration": item.get("duration") or "Unknown",
        "thumbnail": item.get("thumbnail"),
        "url": item.get("url"),
    }]

    return search_data, item.get("url")
