from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
import requests

sched = BlockingScheduler(timezone="Asia/Kolkata")

def send_request():
    requests.post("https://dogememe.herokuapp.com/schedule.json", data={
        "project": "dogememebot",
        "spider": "spider"
    })

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=15, minute=45)
def scheduled_job():
    subprocess.run("scrapyd-deploy", shell=True, universal_newlines=True)
    send_request()

sched.start()