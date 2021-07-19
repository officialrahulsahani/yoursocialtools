from django.forms import ModelForm
from django import forms
from .models import *

class BugReportForm(ModelForm):
    t = [("Functional Error", "Functional Error"), ("Logical Error", "Logical Error"), ("UI Issue", "UI Issue"), ("Performance defects","Performance defects")]
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter Email"}))
    bugtype = forms.ChoiceField(label="Bug Type :", choices=t)
    heading = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Short Title for Bug :"}))
    description = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Describe Bug"}))

    class Meta:
        model = BugReport
        fields = '__all__'