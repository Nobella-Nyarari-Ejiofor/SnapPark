from django.urls import path , re_path
from . import views

urlpatterns =[
   path('', views.welcome , name ='welcome'),
   re_path(r'/logout/$', views.logout, name = "logout")
]