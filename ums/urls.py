
from django.urls import path, reverse
from django.contrib.auth import views as auth_views

from . import views

app_name = 'ums'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('validate/', views.validate_ajax_answer, name='validate'),
]