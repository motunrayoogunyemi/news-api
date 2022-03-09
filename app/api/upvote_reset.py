from api.models import Posts
    

def cleanvotes():
    print("Running task...")
    myposts = Posts.objects.update(post_upvotes=0)
    print(myposts, "objects updated")
    print("Done running")