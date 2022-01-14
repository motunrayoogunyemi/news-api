from django.db import models

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200)
    post_link = models.CharField(max_length=150)
    post_date = models.DateTimeField(auto_now_add=True)
    post_upvotes = models.IntegerField()
    post_author_name = models.CharField(max_length=255)

    def __str__(self):
        return self.post_title

    def total_upvotes(self):
        return self.post_upvotes.count()


class Comments(models.Model):
    Comment_id = models.AutoField(primary_key=True)
    Comment_content = models.CharField(max_length=500)
    comment_author_name = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_author_name
    
