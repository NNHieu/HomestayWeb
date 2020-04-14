from django import forms
from .models import *


class HomestayForm(forms.ModelForm):

    class Meta:
        model = Homestay
        fields = ['title', 'description', 'main_image']