from django.shortcuts import render
from django.http import HttpResponse , Http404
from django.http import HttpResponseRedirect
from .models import Student,LoggedIssue
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .forms import IssueForm

# Create your views here.

def calculate(current_user):
    print(current_user)
    issue_points_info = LoggedIssue.objects.filter(username=current_user)
    total = 0
    for i in issue_points_info:
        total += i.issue_points
    user_display_info = Student.objects.get(user=current_user)
    user_display_info.function_points = total
    user_display_info.effort = user_display_info.function_points * .5
    user_display_info.save()


def index(request):
    return render(request, 'portalapp/index.html')


def displayusers(request):
    students = User.objects.all()
    context = {'students':students}
    return render(request,'portalapp/user.html',context)

def displaypoints(request,username):
    current_user = request.user
    calculate(current_user)
    points_info = Student.objects.get(user=current_user)
    issue_info = LoggedIssue.objects.filter(username=current_user)

    if issue_info.exists():
        return render(request,'portalapp/points.html',{'points_info':points_info , 'issue_info':issue_info})
    else:
        raise Http404("No issue logged Yet")

def passwordreset(request):
    return render(request,'registration/passwordreset.html')

def logissue(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IssueForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            commit_id_form = cleaned_data.get('commit_id')
            url_form = cleaned_data.get('url')
            obj = LoggedIssue(username=request.user.username,commit_id=commit_id_form,url=url_form)
            try:
                obj.save()
            except:
                return HttpResponse('Already Existing Commit! Please resubmit with proper commit id')
    
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IssueForm()
        return render(request,'portalapp/logissue.html',{'form':form})

