import feedparser
import urllib.parse

def fetch_news(query: str):
    encoded = urllib.parse.quote(query)
    url = f"https://news.google.com/rss/search?q={encoded}&hl=id&gl=ID&ceid=ID:id"

    feed = feedparser.parse(url)
    results = []

    for entry in feed.entries:
        # Cek apakah ada kata 'sayuran' di title atau summary
        title_lower = entry.title.lower()
        summary_lower = getattr(entry, 'summary', '').lower()  # beberapa feed ada summary
        if 'sayuran' in title_lower or 'sayuran' in summary_lower:
            results.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published
            })
    
    return {
        "query": query,
        "results": results
    }
