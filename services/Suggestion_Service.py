from YouTubeMusic.Search import Search

async def get_suggestions(title: str, current_url: str):
    keywords = " ".join(title.split()[:4])
    data = await Search(keywords, limit=8)

    suggestions = []
    for r in data["main_results"]:
        if r["url"] != current_url:
            suggestions.append({
                "url": r["url"],
                "title": r["title"],
                "thumbnail": r["thumbnail"],
                "channel": r["channel"],
                "duration": r["duration"]
            })
    return suggestions
