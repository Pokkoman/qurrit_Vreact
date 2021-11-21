from django.urls import path
from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [

    path('',views.index,name= 'index'),
    path('programs',views.getProgram_list,name='programs_list'),

]
