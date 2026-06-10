from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GPT_API_KEY"))

def summarise_article(title, description):
    prompt = f"""
Article title: {title}
Article description: {description}

Summarise this news story in exactly 3 short sentences:
1. What happened
2. Why it matters
3. What to watch next

Be concise and factual. No fluff.
"""
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def summarise_all(articles):
    summaries = []
    for article in articles:
        print(f"Summarising: {article['title'][:50]}...")
        summary = summarise_article(article["title"], article["description"])
        summaries.append({**article, "summary": summary})
    return summaries