from apscheduler.schedulers.background import BackgroundScheduler
from .upvote_reset import update_something, cleanvotes


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_something, 'interval', seconds=20)
    scheduler.add_job(cleanvotes, 'interval', seconds=60)
    scheduler.start()