from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets


from Profile import views





urlpatterns = [
    #re_path(r'Profile/$', CustonAuthToken.as_view()),
    re_path(r'example_lista3/$', views.ExampleList3.as_view()),
    #re_path(r'example_detail2/(?P<id>\d+)/$',views.ExampleDetail2.as_view()),
    re_path(r'CiudadM/$', views.CiudadList.as_view()),
    re_path(r'GeneroM/$', views.GeneroList.as_view()),
    re_path(r'OcupacionM/$', views.OcupacionList.as_view()),
    re_path(r'EstadoM/$', views.EstadoList.as_view()),
    re_path(r'Estado_civilM/$', views.Estado_civilList.as_view()),
]