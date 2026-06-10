import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()

def build_html(summaries):
    today = date.today().strftime("%B %d, %Y")
    items = ""
    for s in summaries:
        items += f"""
        <div style="margin-bottom:24px; padding-bottom:24px; border-bottom:1px solid #eee;">
            <h3 style="margin:0 0 6px; font-size:16px;">
                <a href="{s['url']}" style="color:#1a1a1a; text-decoration:none;">{s['title']}</a>
            </h3>
            <p style="margin:0 0 8px; color:#666; font-size:13px;">{s['source']}</p>
            <p style="margin:0; font-size:14px; line-height:1.6; color:#333;">{s['summary']}</p>
        </div>
        """
    return f"""
    <html><body style="font-family:sans-serif; max-width:600px; margin:auto; padding:20px;">
        <h2 style="color:#1a1a1a;">Your AI News Briefing — {today}</h2>
        <p style="color:#666;">Here are today's top stories, summarised by AI.</p>
        {items}
        <p style="color:#aaa; font-size:12px;">Powered by Claude + NewsAPI</p>
    </body></html>
    """

def send_digest(summaries):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"Your Morning Briefing — {date.today().strftime('%b %d')}"
    msg["From"] = os.getenv("GMAIL_USER")
    msg["To"] = os.getenv("TO_EMAIL")
    msg.attach(MIMEText(build_html(summaries), "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("GMAIL_USER"), os.getenv("GMAIL_APP_PASSWORD"))
        server.send_message(msg)
    print("Email sent successfully!")