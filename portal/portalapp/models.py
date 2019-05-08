from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    function_points = models.IntegerField(default=0)
    effort = models.FloatField(default=0)

class LoggedIssue(models.Model):
    username = models.CharField(max_length=50)
    commit_id = models.CharField(max_length=40,unique=True)
    url = models.URLField(default="https://www.google.com/")
    issue_points = models.IntegerField(default=0)
    is_added = models.BooleanField(default=False)
    


