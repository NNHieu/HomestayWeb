from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'ums'
urlpatterns = [
    path('', views.auth_user, name='auth')
]
