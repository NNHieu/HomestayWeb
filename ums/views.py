from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


# Create your views here.
def login_view(request):
    return render(request, 'ums/login.html', {})


def auth_user(request):
    username = request.POST['uname']
    password = request.POST['psw']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse('login')
    else:
        return HttpResponse('invalid login')