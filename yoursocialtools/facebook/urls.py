from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('fb_downloader/', views.fb_downloader, name="fb_downloader"),

]
