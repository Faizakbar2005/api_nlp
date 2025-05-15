def format_news(results):
    return [
        {
            "title": item.get("title"),
            "description": item.get("description"),
            "link": item.get("link"),
            "pubDate": item.get("pubDate"),
            "source": item.get("source_id")
        }
        for item in results
    ]
