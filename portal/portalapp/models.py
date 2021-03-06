from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime
from django.utils.timezone import make_aware

## Inherits the inbuilt user model.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    function_points = models.FloatField(default=0)
    effort = models.FloatField(default=0)
    name = models.CharField(max_length=100,blank=True,null=True)
    report = models.URLField(default="https://github.com/aditya3498/SRIP2019-Batch1/wiki")
    mentor = models.CharField(max_length=100,blank=True,null=True)
    batch = models.CharField(max_length=100,default="SRIP19-BATCH1")
    handle = models.CharField(max_length=25,unique=True,blank=True,null=True)

    def __str__(self):
        return self.user.username


class LoggedIssue(models.Model):
    username = models.CharField(max_length=50)
    commit_id = models.CharField(max_length=40,unique=True)
    url = models.URLField(default="https://www.google.com/")
    html_ip = models.FloatField(default=0)
    css_ip = models.FloatField(default=0)
    js_ip = models.FloatField(default=0)

    issue_points = models.FloatField(default=0)
    mentor = models.CharField(max_length=100,blank=True,null=True)
    handle = models.CharField(max_length=25,blank=True,null=True,unique=False)
    toc = models.DateTimeField(default=datetime.now)        ## time of creation
    is_added = models.BooleanField(default=False)
    remark = models.CharField(default="-",max_length=1000,unique=False)

    def __str__(self):
        return self.commit_id
    


