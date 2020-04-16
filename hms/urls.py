from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'hms'
urlpatterns = [

    path('', views.BrowseView.as_view(), name='index'),
    # path('upload/', views.upload_view, name='upload'),
    # path('upload/success/', views.upload_success_view, name='upload_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
