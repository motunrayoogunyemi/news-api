# -*- coding: utf-8 -*-
"""
Daily cleanup job.
Can be run as a cronjob to clean out old data from the database (only expired
sessions at the moment).
"""
from api.models import Posts
from django_extensions.management.jobs import DailyJob

class Job(DailyJob):
    help = "Upvotes cleanup Job"

    def execute(self):
        myposts = Posts.objects.all()
        myposts.post_upvotes = 0
        print("Posts reset")
        return