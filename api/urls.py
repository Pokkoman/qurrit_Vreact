from django.urls import path
from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('programs', views.getProgramList, name='program_list'),
    path('programs/create', views.createProgram, name='create_program'),
    path('programs/search/<str:name>', views.search, name='search'),
    path('programs/<str:id>', views.getWorkouts, name='workout_list'),
    path('exercises', views.getExercises, name='exercise_list'),


]
