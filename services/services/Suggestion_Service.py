async def get_suggestions(title: str, current_url: str):
    keywords = " ".join(title.split()[:3])
    data = await Search(keywords, limit=6)

    suggestions = []
    for result in data["main_results"]:
        if result["url"] != current_url:
            suggestions.append({
                "url": result["url"],
                "title": result["title"],
                "thumbnail": result["thumbnail"],
                "channel": result["channel"]
            })

    return suggestions
