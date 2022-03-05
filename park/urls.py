from django.contrib import admin
from django.urls import path , include, re_path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('photos.urls')),
    re_path(r'^accounts/' , include ('registration.backends.simple.urls')),
    re_path(r'^logout/$' , views.LogoutView.as_view(), {"next_page":'/'}),
]
