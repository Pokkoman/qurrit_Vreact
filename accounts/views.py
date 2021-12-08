from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['POST'])
def register(requests):

    print(requests.data)

    username = requests.data['username']
    password = requests.data['password']
    email = requests.data['email']
    first_name = requests.data['first_name']
    last_name = requests.data['last_name']

    user = User.objects.create(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )

    user.save()
    return HttpResponse('hello')


def login(requests):
    pass
