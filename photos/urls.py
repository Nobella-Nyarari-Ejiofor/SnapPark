from django.urls import path , re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
   path('', views.welcome , name ='welcome'),
   re_path(r'logout/$', views.logout, name = "logout")
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)