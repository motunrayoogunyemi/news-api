from apscheduler.schedulers.background import BackgroundScheduler
from .upvote_reset import cleanvotes


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(cleanvotes, trigger='cron', hour=0, minute=0, id='clean_votes', replace_existing=True)
    scheduler.start()