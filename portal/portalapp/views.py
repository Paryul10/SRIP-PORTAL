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
    # print(current_user)
    # print("---------------------------------------------------")
    p = Student.objects.get(user=current_user).function_points
    # print("---------------------------------------------------")
    # e = Points.objects.get(pk=user_id).effort
    return HttpResponse("Function Points of user %s" % p)

    