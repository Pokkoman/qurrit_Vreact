from django.urls import path
from django.conf.urls import url
from django.urls.resolvers import URLPattern
from . import views


urlpatterns = [
    path('checkout', views.create_payment, name='checkout'),
]
