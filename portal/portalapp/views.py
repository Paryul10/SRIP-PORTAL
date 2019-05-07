from django.shortcuts import render
from django.http import HttpResponse
from .models import Points
from django.contrib.auth import views as auth_views

# Create your views here.
def index(request):
    # return HttpResponse("Home Page. After Login")
    return render(request, 'portalapp/index.html')


def displayusers(request):
    students = Points.objects.all()
    # usernames = ', ' .join(s.username for s in students)
    context = {'students':students}
    # return  HttpResponse(usernames)
    return render(request,'portalapp/user.html',context)

def displaypoints(request,username):
    p = Points.objects.get(pk=username).function_points
    # e = Points.objects.get(pk=user_id).effort
    return HttpResponse("Function Points of user %s" % p)

    