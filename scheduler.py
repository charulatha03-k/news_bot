import schedule
import time
from main import run_briefing

schedule.every().day.at("07:00").do(run_briefing)

print("Scheduler running. Waiting for 7am...")
while True:
    schedule.run_pending()
    time.sleep(60)