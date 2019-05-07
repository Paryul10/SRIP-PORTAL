from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

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

    