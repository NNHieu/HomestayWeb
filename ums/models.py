from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from .validators import PhoneNumberValidator


# Create your models here.

class Guest(User):
    phone_number = models.CharField(max_length=10, validators=[PhoneNumberValidator()])
