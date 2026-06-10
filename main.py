from fetcher import fetch_top_news
from summariser import summarise_all
from emailer import send_digest

def run_briefing():
    print("Fetching news...")

    articles = fetch_top_news()

    if not articles:
        print("No articles found.")
        return

    print(f"Got {len(articles)} articles. Summarising...")

    summaries = summarise_all(articles)

    print("Sending email...")
    send_digest(summaries)

    print("Done!")

if __name__ == "__main__":
    run_briefing()