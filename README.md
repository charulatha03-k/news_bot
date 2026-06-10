📰 AI News Briefing Bot
An automated news digest bot that fetches top headlines, summarises them using AI, and delivers a clean formatted email to your inbox every morning.
Built with Python, NewsAPI, Groq LLM, and Gmail SMTP.
---
✨ Features
Fetches top news articles by topic and country
Summarises each article into 3 concise sentences using AI
Sends a beautifully formatted HTML email digest daily
Fully automated — runs every morning without any manual trigger
Easily customisable topic, country, and delivery time
---
🛠️ Tech Stack
Tool	Purpose
Python	Core language
NewsAPI	Fetching live news headlines
Groq API	AI summarisation (LLM)
Gmail SMTP	Sending email digest
python-dotenv	Managing secret keys securely
schedule	Running the bot daily automatically
---
📁 Project Structure
```
news_bot/
├── .env                 # Secret API keys (never commit this)
├── .gitignore           # Excludes .env from git
├── fetcher.py           # Fetches news from NewsAPI
├── summariser.py        # Summarises articles using Groq AI
├── emailer.py           # Builds and sends HTML email
├── main.py              # Ties all modules together
├── scheduler.py         # Runs main.py daily at 7am
└── README.md            # You are here
```
---
⚙️ Setup & Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/news_bot.git
cd news_bot
```
2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```
3. Install dependencies
```bash
pip install requests groq python-dotenv schedule
```
4. Get your API keys
Key	Where to get it
`NEWS_API_KEY`	newsapi.org — free signup
`GPT_API_KEY`	console.groq.com — free signup
`GMAIL_APP_PASSWORD`	Google Account → Security → App Passwords
5. Create your `.env` file
Create a file named `.env` in the root folder:
```
NEWS_API_KEY=your_newsapi_key_here
GPT_API_KEY=your_groq_key_here
GMAIL_USER=yourname@gmail.com
GMAIL_APP_PASSWORD=your16charpassword
TO_EMAIL=yourname@gmail.com
```
> ⚠️ Never share this file or commit it to GitHub.
---
🚀 Running the Bot
Run once manually
```bash
python main.py
```
You should see:
```
Fetching news...
Got 5 articles. Summarising...
Summarising: Article title here...
Sending email...
Email sent successfully!
Done!
```
Run on a daily schedule
```bash
python scheduler.py
```
This keeps running in the background and triggers the bot every day at 7:00am.
---
🌍 Customising Topic & Country
In `main.py`, change the topic and country to anything you want:
```python
articles = fetch_top_news(topic="cricket", country="india", count=5)
```
Example combinations:
topic	country
`"cricket"`	`"india"`
`"sports"`	`"india"`
`"politics"`	`"india"`
`"technology"`	`"india"`
`"bollywood"`	`"india"`
---
☁️ Hosting (Run Without Your Laptop)
Option 1 — GitHub Actions (Recommended, Free)
Add `.github/workflows/daily_news.yml` to your repo:
```yaml
name: Daily News Briefing

on:
  schedule:
    - cron: '30 1 * * *'   # 7:00am IST daily
  workflow_dispatch:

jobs:
  send-briefing:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install requests groq python-dotenv
      - name: Run bot
        env:
          NEWS_API_KEY: ${{ secrets.NEWS_API_KEY }}
          GPT_API_KEY: ${{ secrets.GPT_API_KEY }}
          GMAIL_USER: ${{ secrets.GMAIL_USER }}
          GMAIL_APP_PASSWORD: ${{ secrets.GMAIL_APP_PASSWORD }}
          TO_EMAIL: ${{ secrets.TO_EMAIL }}
        run: python main.py
```
Add your keys in: GitHub repo → Settings → Secrets and variables → Actions
Option 2 — PythonAnywhere (Free, No Credit Card)
Sign up at pythonanywhere.com
Upload all `.py` files and your `.env`
Install packages in their Bash console
Set a daily task pointing to `main.py`
---
🧠 Concepts Learned
REST API integration (NewsAPI)
AI/LLM API integration (Groq)
Prompt engineering for structured output
JSON parsing and data pipelines
HTML email generation and SMTP
Environment variables and secret management
Task scheduling and automation
Cloud deployment with GitHub Actions
---
🔮 Possible Upgrades
[ ] Add multiple topics/categories in one email
[ ] Let AI pick the single most important story of the day
[ ] Send via WhatsApp using Twilio API
[ ] Add a web UI to configure topic and country
[ ] Store past digests in a database
---
📄 License
MIT License — free to use, modify, and share.
---
Built as a learning project to understand AI API integration, LLM summarisation, and automated pipelines.
