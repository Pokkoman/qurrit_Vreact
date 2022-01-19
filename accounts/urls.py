from django.urls import path
from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('isexist', views.user_email_check, name='check_list'),
    path('login', views.userlogin, name='login'),
    path('logout', views.userlogout, name='logout'),
    path('profile', views.user_profile, name='user_profile'),
    path('getusername', views.getUsername, name='username_from_programID')


]
