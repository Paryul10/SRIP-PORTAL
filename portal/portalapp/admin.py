from __future__ import unicode_literals
from django.contrib import admin
from .models import Student, LoggedIssue

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user' ,'name' , 'function_points' , 'effort', 'handle', 'mentor','report' , 'batch']

admin.site.register(Student,StudentAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ['username', 'commit_id',
                     'issue_points', 'mentor','handle' ,'toc', 'remark', 'is_added']
    
    list_filter = ('mentor','is_added')

admin.site.register(LoggedIssue, IssueAdmin)
