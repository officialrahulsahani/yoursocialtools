from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django import forms
from .forms import *



def home(request):
    return render(request, 'common/home.html')

def about(request):
    return render(request, 'common/about.html')

def terms(request):
    return render(request, 'common/terms.html')

def bugreport(request):
    form = BugReportForm()
    if request.method == "POST":
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Bug Has Been Reported Successfully. We will fix this soon.")
            return render(request, 'common/bugreport.html', {"form": form})
    return render(request, 'common/bugreport.html', {"form": form})
    