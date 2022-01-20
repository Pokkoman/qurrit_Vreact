
from django.shortcuts import render
import razorpay
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Customer, Trainer
from api.models import Workout, Program

# Create your views here.


@api_view(['POST'])
def create_payment(requests):
    try:
        data = requests.data

        program = Program.objects.get(id=data['programId'])
        if program.cost == 0:
            cost = 0
        else:
            cost = program.cost

        customer = Customer.objects.get(id=data['userId'])
        customer.programs_bought.append(data['programId'])
        customer.save()

        return Response({
        })

    except Exception as e:
        print(e)
        return Response(str(e))
