from api.models import Posts

def update_something():
    print("this function runs every 10 seconds")

def cleanvotes():
    print("Running task...")
    myposts = Posts.objects.all()
    myposts.post_upvotes = 0
    print("Done running")