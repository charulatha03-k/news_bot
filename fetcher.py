import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_top_news(topic="sports", country="india", count=5):
    url = "https://newsapi.org/v2/everything"   # ← changed from top-headlines
    params = {
        "q": f"{topic} {country}",              # ← search by keyword instead
        "language": "en",
        "sortBy": "publishedAt",                # ← latest news first
        "pageSize": count,
        "apiKey": os.getenv("NEWS_API_KEY")
    }
    response = requests.get(url, params=params)
    data = response.json()

    print(f"Status: {data.get('status')}, Results: {data.get('totalResults')}")

    articles = []
    for article in data.get("articles", []):
        if article.get("title") and article.get("description"):
            articles.append({
                "title": article["title"],
                "description": article.get("description", ""),
                "url": article["url"],
                "source": article["source"]["name"]
            })
    return articles