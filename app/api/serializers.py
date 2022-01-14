# from django.contrib.auth import get_user_model

from .models import Comments, Posts
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ['post_id', 'post_title', 'post_link', 'post_date', 'post_upvotes', 'post_author_name']


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['Comment_id', 'Comment_content', 'comment_author_name', 'comment_date']


class PostvoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ['post_upvotes']