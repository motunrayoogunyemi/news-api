# Create your tasks here

from .models import Posts

from celery import shared_task


@shared_task
def cleanvotes():
    print("Running task...")
    myposts = Posts.objects.all()
    myposts.post_upvotes = 0
