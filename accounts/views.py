from django.contrib.auth import models
from django.db.models.fields.json import DataContains
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *

# Create your views here.


@api_view(['POST'])
def register(requests):

    print(requests.data)

    username = requests.data['username']
    password = requests.data['password']
    email = requests.data['email']
    first_name = requests.data['first_name']
    last_name = requests.data['last_name']

    if requests.data['user_type'] == 'Customer':
        user = User.objects.create(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
    )
        customer = Customer.objects.create(user = user,programs_bought=[0])
        customer.save()
    elif requests.data['user_type'] == 'Trainer':
        user = Trainer.objects.create(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,)

        trainer = Trainer.objects.create(user = user,programs_created=[0])
        trainer.save()

    return HttpResponse('hello')


@api_view(['GET'])
def user_email_check(requests):

    check_list = User.objects.values('username', 'email')

    return Response(check_list)
