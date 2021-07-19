from django.db import models
from django.forms import ModelForm

class BugReport(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    bugtype = models.CharField(max_length=20, default="")
    heading = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=1000, default="")
    def __str__(self):
        return self.heading

