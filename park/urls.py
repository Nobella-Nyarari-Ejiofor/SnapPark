from django.contrib import admin
from django.urls import path , include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('photos.urls')),
    re_path(r'^accounts/' , include ('registration.backends.simple.urls')),
    re_path(r'^logout/$' , TemplateView.as_view(template_name = 'registration/logout.html'), name='logout'),
]
