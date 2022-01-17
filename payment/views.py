
from django.shortcuts import render
import stripe
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Customer, Trainer
from api.models import Workout, Program

# Create your views here.

stripe.api_key = 'sk_test_51KIyg3SED7tS9grbSn5duWOKrvE5nXqVDkYHIg6LBeKXJloSmKG6sgw9azzXcadwajn7ajfsXfbtTgtf1FuTUMK900Xnzz04V7'


@api_view(['POST'])
def create_payment(requests):
    try:
        data = requests.data

        program = Program.objects.get(id=data['programId'])
        if program.cost == 0:
            cost = 2
        else:
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
