from django.contrib import admin
from django.urls import path
from youtube import views
urlpatterns = [
    path('playtime/', views.playtime, name="playtime"),
    path('<str:playlist_link>/', views.result, name="result"),
    path('yt_downloader', views.ytb_down, name='yt_downloader')


]
