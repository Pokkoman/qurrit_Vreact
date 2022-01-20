from modulefinder import ReplacePackage
from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User, UserManager
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Program
from .models import *
from django.contrib.auth import authenticate, login, logout

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
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        customer = Customer.objects.create(user=user, programs_bought=[0])
        customer.save()
    elif requests.data['user_type'] == 'Trainer':
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,)

        trainer = Trainer.objects.create(user=user, programs_created=[0])
        trainer.save()

    return HttpResponse('hello')


@api_view(['POST'])
def userlogin(requests):
    username = requests.data['username']
    password = requests.data['password']

    user = authenticate(requests, username=username, password=password)

    if user is not None:

        login(requests._request, user)
        usercheck = User.objects.get(username=username)

        try:
            userdata_customer = Customer.objects.get(user=usercheck)
        except Customer.DoesNotExist:
            userdata_customer = None

        try:
            userdata_trainer = Trainer.objects.get(user=usercheck)
        except Trainer.DoesNotExist:
            userdata_trainer = None

        if userdata_customer is not None:
            data = {
                'id': userdata_customer.id,
                'username': userdata_customer.user.username,
                'first_name': userdata_customer.user.first_name,
                'last_name': userdata_customer.user.last_name,
                'user_type': "Customer",
                'programs': userdata_customer.programs_bought
            }
        elif userdata_trainer is not None:
            data = {
                'id': userdata_trainer.id,
                'username': userdata_trainer.user.username,
                'first_name': userdata_trainer.user.first_name,
                'last_name': userdata_trainer.user.last_name,
                'user_type': "Trainer",
                'programs': userdata_trainer.programs_created
            }

        print("user logged in")
        return Response(data)
    else:
        return Response('error')


@api_view(["POST"])
def userlogout(requests):

    logout(requests._request)

    return HttpResponse('Logout')


@api_view(['GET'])
def user_email_check(requests):

    check_list = User.objects.values('username', 'email')

    return Response(check_list)


@api_view(['GET'])
def user_profile(requests):

    data = requests.data
    username = data['username']

    try:
        user = User.objects.get(username=username)
        trainer = Trainer.objects.get(user=user)

        response = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'programs': trainer.programs_created}
    except Exception as e:
        return Response(None, status=204)

    return Response(response)


@api_view(['POST'])
def getUsername(requests):

    data = requests.data
    # program_id = data['program_id']
    try:
        program_id = 12
        trainer = Trainer.objects.filter(
            programs_created__contains=[program_id])

        return Response(trainer[0].user.username)

    except Exception as e:
        return Response(None, status=204)
