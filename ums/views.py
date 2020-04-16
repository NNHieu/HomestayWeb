import logging

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import *
from .validators import validate_user_id

# Create your views here.
# def login_view(request):
#     return render(request, 'ums/login.html', {})


# def auth_user(request):
#     username = request.POST['uname']
#     password = request.POST['psw']
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return HttpResponse('login')
#     else:
#         return HttpResponse('invalid login')

logger = logging.getLogger('root')


# View cho trang login
def login_view(request):
    error = False
    if request.method == 'POST':
        uid = request.POST['uname']
        pw = request.POST['password']
        user = authenticate(request, username=uid, password=pw)
        if user is not None:
            login(request, user)
            return redirect(request.POST["next"])
        else:
            error = True
            return render(request, 'ums/login.html', {'errors': error, 'next': request.GET['next'], 'first': False})
    return render(request, 'ums/login.html',
                  {'errors': error, 'next': request.GET.get('next', '/homestay'), 'first': True})


@login_required
def logout_view(request):
    logout(request)
    return redirect('hms:index')


def register_view(request):
    error = 0
    if request.method == 'POST':
        form = RegisterForms(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(new_user.password)
            new_user.save()
            login(request, new_user)
            return redirect(request.POST['next'])
    else:
        form = RegisterForms()
    return render(request, 'ums/register.html', {'form': form, 'next': request.GET.get('next', '/homestay')})


def validate_ajax_answer(request):
    print(request.GET)
    check_email = request.GET.get('isEmail', None)
    value = request.GET.get('value', None)
    data = {
        'available': validate_user_id(value, check_email == 'true')
    }
    print(data)
    return JsonResponse(data)
