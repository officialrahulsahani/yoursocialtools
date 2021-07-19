
from django.contrib import admin
from django.urls import path
from common import views
urlpatterns = [
    path('about/', views.about, name="about"),
    path('terms/', views.terms, name="terms"),
    path('bugreport/', views.bugreport, name="bugreport")

]
