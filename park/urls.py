from django.contrib import admin
from django.urls import path , include, re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('photos.urls')),
    re_path(r'^accounts/' , include ('registration.backends.simple.urls'))
]
