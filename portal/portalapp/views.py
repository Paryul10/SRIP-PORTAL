from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from .models import Student, LoggedIssue
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .forms import IssueForm, ReportForm, HandleForm

# Create your views here.'

## Calculates the latest function points and the equivalent effort. It is called only when a user clicks on View Performance.
def calculate(current_user):
    div_fac = 27
    mul_fac = 3
    j = 0.45
    power = mul_fac * j

    issue_points_info = LoggedIssue.objects.filter(username=current_user)
    len_com = len(issue_points_info)

    ## Each issue points are update according to the total sum of html, css , js
    for i in range(len_com):
        issue_points_info[i].issue_points = issue_points_info[i].html_ip + issue_points_info[i].css_ip + issue_points_info[i].js_ip
        issue_points_info[i].save()

    index = len_com - 1
    if len_com >=1:
        i = len_com - 1
        while i>=0:
            if issue_points_info[i].is_added == True:
                total = issue_points_info[i].issue_points
                index = i
                break
            else:
                index = i
                total = 0
            i -= 1
    else:
        total = 0
        
    user_display_info = Student.objects.get(user=current_user)
    user_display_info.function_points = issue_points_info[index].html_ip + issue_points_info[index].css_ip + issue_points_info[index].js_ip

    html_mh = ((((issue_points_info[index].html_ip) ** power) * 160)/27)
    css_mh = ((((issue_points_info[index].css_ip) ** power) * 160)/27)
    js_mh = ((((issue_points_info[index].js_ip) ** power) * 160)/27)

    user_display_info.effort = html_mh + css_mh + js_mh
    user_display_info.save()

## Home Page
def index(request):
    if request.user.is_authenticated:
        current_user = request.user
        info = Student.objects.get(user=current_user)
        return render(request, 'portalapp/index.html', {'info': info})
    else:
        return render(request, 'portalapp/index.html')

## My part code
def displayusers(request):
    students = User.objects.all()
    context = {'students': students}
    return render(request, 'portalapp/user.html', context)

## Displays points of a user. 
def displaypoints(request, username):
    current_user = request.user
    calculate(current_user)
    info = Student.objects.get(user=current_user)
    issue_info = LoggedIssue.objects.filter(username=current_user)

    length = len(issue_info)
    # for i in range(length):
    #     print(issue_info[i].remark)


    if issue_info.exists():
        return render(request, 'portalapp/points.html', {'info': info, 'issue_info': issue_info})
    else:
        return HttpResponse("No Commit logged yet!")


def passwordreset(request):
    return render(request, 'registration/passwordreset.html')

## OPens page to accept a commit id and url of the issue.
def logissue(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IssueForm(request.POST)
        if form.is_valid():
            current_user = request.user.username
            cleaned_data = form.cleaned_data
            commit_id_form = cleaned_data.get('commit_id')
            url_form = cleaned_data.get('url')
            mentor_name = Student.objects.get(user=request.user).mentor
            handle_form = Student.objects.get(user=request.user).handle
            obj = LoggedIssue(username=current_user, commit_id=commit_id_form, url=url_form, mentor=mentor_name,handle=handle_form)
            try:
                obj.save()
            except:
                return HttpResponse('Already Existing Commit! Please resubmit with proper commit id')

            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IssueForm()
        return render(request, 'portalapp/logissue.html', {'form': form})


## Form for weekly report
def report(request):

    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            current_user = request.user
            cleaned_data = form.cleaned_data
            report_form = cleaned_data.get('report')
            # print(report_form)
            obj = Student.objects.get(user=current_user)
            # print(obj)
            obj.report = report_form
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = ReportForm()
        return render(request, 'portalapp/report.html', {'form': form})

## Github handle Uploading. The button vanishes after handle is uploaded once.
def uploadhandle(request):

    if request.method == 'POST':
        form = HandleForm(request.POST)
        if form.is_valid():
            current_user = request.user
            cleaned_data = form.cleaned_data
            handle_form = cleaned_data.get('handle')
            obj = Student.objects.get(user=current_user)
            obj.handle = handle_form
            try:
                obj.save()
                return HttpResponseRedirect('/')
            except:
                return HttpResponse('Already Existing Handle! Please check and resubmit')

    else:
        form = HandleForm()

    return render(request, 'portalapp/uploadhandle.html', {'form': form})
