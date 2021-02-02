from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    # path('video_feed',views.video_feed,name='video_feed'),
    # path('capture',views.capture_photo,name='capture_photo')
]
