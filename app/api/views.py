from lib2to3.pytree import Base
import schedule, time, threading
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, Http404
from api.models import Posts, Comments
from api.serializers import PostSerializer, CommentSerializer, PostvoteSerializer
from django.db import connection

from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class Postnews1(APIView):

    def get(self, request):
        myposts = Posts.objects.all()
        serializer = PostSerializer(myposts, many=True)   
        return Response(serializer.data)
        

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class Postnews2(APIView):

    def get_post(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        myposts = self.get_post(pk)
        serializer = PostSerializer(myposts)
     
        return Response(serializer.data)
        

    def put(self, request, pk):
        myposts = self.get_post(pk)
        serializer = PostSerializer(myposts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        myposts = self.get_post(pk)
        myposts.delete()
        return Response(f'successfully deleted {myposts}')


class Comments1(APIView):

    def get(self, request):
        mycomments = Comments.objects.all()
        serializer = CommentSerializer(mycomments, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class Comments2(APIView):

    def get_comment(self, pk):
        try:
            return Comments.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        mycomments = self.get_comment(pk)
        serializer = CommentSerializer(mycomments)
        return Response(serializer.data)

    def put(self, request, pk):
        mycomments = self.get_comment(pk)
        serializer = CommentSerializer(mycomments, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mycomments = self.get_comment(pk)
        mycomments.delete()
        return Response(f'successfully deleted {mycomments}')


class Upvote(APIView):

    def get_vote(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except:
            raise Http404

    # def post(self, request):
    #     serializer = PostvoteSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.total_upvotes()
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request, pk):
        vote = self.get_vote(pk)
        vote.total_upvotes()
        return Response({f'Post {vote} has been successfully upvoted'})



        

