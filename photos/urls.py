from django.urls import path , re_path
from . import views
from .views import AdminLogin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[

   path('', AdminLogin.as_view(), name="login"),
   re_path(r'logout/$', views.logout, name = "logout"),
   re_path(r'profile/' , views.profile , name ="profile"),
   re_path(r'poster/' , views.poster, name ="poster"),
   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)