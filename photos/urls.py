from django.urls import path , re_path
from . import views
# from .views import AdminLogin, MyRegistrationView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[

   # # path('', AdminLogin.as_view(), name="login"),
   # path('register/',MyRegistrationView.as_view(), name ='register'),
   path('home/', views.home, name="home"),
   path('comments/', views.comments ,name="comments"),
   re_path(r'logout/$', views.logout, name = "logout"),
   re_path(r'profile/' , views.profile , name ="profile"),

   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)