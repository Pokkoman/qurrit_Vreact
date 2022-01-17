
from django.shortcuts import render
import stripe
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Customer, Trainer
from api.models import Workout, Program

# Create your views here.

stripe.api_key = 'sk_test_tR3PYbcVNZZ796tH88S4VQ2u'


@api_view(['POST'])
def create_payment(requests):
    try:
        # data = requests.data

        data = {
            'programId': 2,
            'userId': 2
        }

        program = Program.objects.get(id=data['programId'])
        cost = program.cost

        intent = stripe.PaymentIntent.create(
            amount=cost,
            currency='inr',
            automatic_payment_methods={
                'enabled': True
            },
        )

        customer = Customer.objects.get(id=data['userId'])
        customer.programs_bought.append(data['programId'])
        customer.save()

        return Response({
            'clientSecret': intent['client_secret']
        })

    except Exception as e:
        print(e)
        return Response(str(e))
