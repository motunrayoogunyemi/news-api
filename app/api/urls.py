# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts', views.Postnews1.as_view()),
    path('posts/<int:pk>', views.Postnews2.as_view()),
    path('vote/<int:pk>', views.Upvote.as_view()),
    path('comments', views.Comments1.as_view()),
    path('comments/<int:pk>', views.Comments2.as_view())
]