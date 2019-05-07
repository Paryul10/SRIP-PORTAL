from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Student,LoggedIssue
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from .forms import IssueForm

# Create your views here.
def index(request):
    # return HttpResponse("Home Page. After Login")
    return render(request, 'portalapp/index.html')


def displayusers(request):
    students = User.objects.all()
    # usernames = ', ' .join(s.username for s in students)
    context = {'students':students}
    # return  HttpResponse(usernames)
    return render(request,'portalapp/user.html',context)

def displaypoints(request,username):
    current_user = request.user
    data = Student.objects.get(user=current_user)
    context = {'data':data}
    # return HttpResponse("Function Points of user are %s" % p)
    return render(request,'portalapp/points.html',context)

def passwordreset(request):
    return render(request,'registration/passwordreset.html')

# def logissue(request):
#     form = IssueForm()
#     return render(request,'portalapp/logissue.html',{'form':form})


def logissue(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IssueForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # print(cleaned_data)            
            commit_id_form = cleaned_data.get('commit_id')
            url_form = cleaned_data.get('url')
            obj = LoggedIssue(username=request.user.username,commit_id=commit_id_form,url=url_form)
            try:
                obj.save()
            except:
                return HttpResponse('Already Existing Commit! Please resubmit with proper commit id')

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IssueForm()
        return render(request,'portalapp/logissue.html',{'form':form})

    # return render(request, 'issue.html', {'form': form})

    # 521747298a3790fde1710f3aa2d03b55020575aa
