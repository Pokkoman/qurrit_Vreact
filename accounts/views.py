
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
        customer = Customer.objects.create(
            user=user, programs_bought=[0])
        customer.save()
    elif requests.data['user_type'] == 'Trainer':
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,)

        trainer = Trainer.objects.create(
            user=user, programs_created=[0])
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
                'user_id': usercheck.id,
                'id': userdata_customer.id,
                'username': userdata_customer.user.username,
                'first_name': userdata_customer.user.first_name,
                'last_name': userdata_customer.user.last_name,
                'user_type': "Customer",
                'programs': userdata_customer.programs_bought,
                'image': userdata_customer.image
            }
        elif userdata_trainer is not None:
            data = {
                'user_id': usercheck.id,
                'id': userdata_trainer.id,
                'username': userdata_trainer.user.username,
                'first_name': userdata_trainer.user.first_name,
                'last_name': userdata_trainer.user.last_name,
                'user_type': "Trainer",
                'programs': userdata_trainer.programs_created,
                'image': userdata_trainer.image
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


@api_view(['POST'])
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
    program_id = data['program_id']
    try:
        trainer = Trainer.objects.filter(
            programs_created__contains=[program_id])

        return Response(trainer[0].user.username)

    except Exception as e:
        return Response(str(e), status=204)


@api_view(['POST'])
def getProgramsPurchased(requests):

    data = requests.data
    username = data['username']
    id = data['id']

    usercheck = User.objects.get(username=username, id=id)

    try:
        userdata_customer = Customer.objects.get(user=usercheck)
    except Customer.DoesNotExist:
        userdata_customer = None

    try:
        userdata_trainer = Trainer.objects.get(user=usercheck)
    except Trainer.DoesNotExist:
        userdata_trainer = None

    if userdata_customer is not None:
        response = {
            'user_type': 'Customer',
            'programs_bought': userdata_customer.programs_bought,
            'image': userdata_customer.image
        }

    if userdata_trainer is not None:
        response = {
            'user_type': 'Trainer',
            'programs_bought': userdata_trainer.programs_created,
            'image': userdata_trainer.image
        }

    return Response(response)


@api_view(['POST'])
def resetpassword(requests):

    data = requests.data
    id = data["id"]
    new_password = data['new_password']

    try:

        user = User.objects.get(id=id)

        user.set_password(new_password)
        print(user)
        user.save()

    except Exception as e:
        return Response(str(e), status=500)

    return Response("Password reset", status=200)


@api_view(["POST"])
def updateprofile(requests):

    data = requests.data
    id = data['id']
    image_url = data["url"]

    usercheck = User.objects.get(id=id)

    try:

        try:
            userdata_customer = Customer.objects.get(user=usercheck)
        except Customer.DoesNotExist:
            userdata_customer = None

        try:
            userdata_trainer = Trainer.objects.get(user=usercheck)
        except Trainer.DoesNotExist:
            userdata_trainer = None

        if userdata_customer is not None:
            userdata_customer.image = image_url
            userdata_customer.save()

        if userdata_trainer is not None:
            userdata_trainer.image = image_url
            userdata_trainer.save()

    except Exception as e:
        return Response(str(e), status=500)

    return Response("Image Changed", status=200)
