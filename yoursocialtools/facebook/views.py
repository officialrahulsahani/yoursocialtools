from django.shortcuts import render, redirect
from django.contrib import messages
import os
import fbdown
import requests


# Create your views here.
def fb_downloader(request):
    try:
        if request.method == "POST":
            url = request.POST.get('url')
            homedir = os.path.expanduser("~")
            dirs = homedir + '/Downloads'
            a = fbdown.get(url)
            if 'fb.watch' in url:
                x = requests.get(url)
                url = x.url
            d = fbdown.getdownlink(url)
            return redirect(d)
    except:
        messages.error(request, "This Link is not Valid!")
        return render(request, 'facebook/fb_downloader.html')
    return render(request, 'facebook/fb_downloader.html')