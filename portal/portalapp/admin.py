from __future__ import unicode_literals
from django.contrib import admin
from .models import Student, LoggedIssue

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['user' , 'function_points' , 'effort', 'mentor','report' , 'batch']

    # def filter_by_mentors(modeladmin,request,queryset):
    #     for students in queryset:


admin.site.register(Student,StudentAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ['username', 'commit_id',
                    'url', 'issue_points', 'mentor', 'is_added']


admin.site.register(LoggedIssue, IssueAdmin)
