from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator

from .validators import MyUsernameValidator, PhoneNumberValidator
from .models import Guest

class RegisterForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField(label='Username', max_length=100, validators=[MyUsernameValidator()])
    first_name = forms.CharField(label='First name', max_length=50)
    last_name = forms.CharField(label='Last Name', max_length=50)
    email = forms.EmailField(validators=[EmailValidator()])
    phone_number = forms.CharField(validators=[PhoneNumberValidator()], max_length=10)

    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'password']
