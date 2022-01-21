from api.models import Posts
from django_extensions.management.jobs import MinutelyJob

class Job(MinutelyJob):
    help = "Upvotes(minutely) cleanup Job"

    def execute(self):
        myposts = Posts.objects.all()
        myposts.post_upvotes = 0
        print("Posts reset (minutely version)")
        return