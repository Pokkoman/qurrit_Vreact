
from django.shortcuts import render
import stripe
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

stripe.api_key = 'sk_test_tR3PYbcVNZZ796tH88S4VQ2u'


@api_view(['POST'])
def create_payment(requests):
    try:
        data = requests.data

        intent = stripe.PaymentIntent.create(
            amount=100,
            currency='inr',
            automatic_payment_methods={
                'enabled': True
            },
        )

        return Response({
            'clientSecret': intent['client_secret']
        })

    except Exception as e:
        print(e)
        return Response(str(e))
