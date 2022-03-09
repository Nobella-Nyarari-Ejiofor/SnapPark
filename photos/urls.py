# from django.urls import path , re_path
# from . import views
# from django.conf.urls.static import static
# from django.conf import settings

# urlpatterns =[

#    # # path('', AdminLogin.as_view(), name="login"),
#    # path('register/',MyRegistrationView.as_view(), name ='register'),
#    path('', views.index, name="index"),
#    # path('comments/', views.comments ,name="comments"),
#    re_path(r'logout/$', views.logout, name = "logout"),
#    re_path(r'^profile/' , views.profile , name ="profile"),
#    # re_path(r'poster/' , views.poster, name ="poster"),
#      path('comment/<post_id>', views.comment, name='comment'),
#     path('like/<post_id>', views.like, name='like'),
#     path('follow/<user_id>', views.follow, name='follow'),

# ]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('comment/<post_id>', views.comment, name='comment'),
    path('like/<post_id>', views.like, name='like'),
    path('follow/<user_id>', views.follow, name='follow'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)