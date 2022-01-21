from api.models import Posts


def execute():
    print("Posts reset (minutely version)")
    myposts = Posts.objects.all()
    myposts.post_upvotes = 0
    return