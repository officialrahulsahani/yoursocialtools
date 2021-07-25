from django.contrib import admin
from django.urls import path
from django.urls import path, include
from common import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('', include('common.urls')),
    path('youtube/', include('youtube.urls')),
    path('facebook/', include('facebook.urls')),


]
