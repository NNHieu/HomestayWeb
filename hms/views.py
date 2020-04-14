from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .forms import *
from .models import *

# Create your views here.
class BrowseView(generic.ListView):
    template_name = 'hms/browse.html'
    context_object_name = 'homestay_list'

    def get_queryset(self):
        return Homestay.objects.all()[:10]


def upload_view(request):
    if request.method == 'POST':
        form = HomestayForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hms:upload_success')
    else:
        form = HomestayForm()
    return render(request, 'hms/upload_homestay.html', {'form': form})


def upload_success_view(request):
    return HttpResponse('Successed')
