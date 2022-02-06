from charset_normalizer import api
from django.http import response
from django.shortcuts import render
import razorpay
from rest_framework.response import Response
from rest_framework.decorators import api_view
from accounts.models import Customer, Trainer
from django.contrib.auth.models import User
from api.models import Workout, Program
import json
from .models import Order

# Create your views here.


@api_view(['POST'])
def create_payment(requests):

    try:
        data = requests.data

        program_id = data['programId']
        user_id = data["userId"]

        program = Program.objects.get(id=data['programId'])

        cost = program.cost

        try:
            user = User .objects.get(id=user_id)
            check_trainer = Customer.objects.get(user=user)

        except Customer.DoesNotExist:
            return Response("Trainer cant buy workouts", status=204)

        client = razorpay.Client(
            auth=("rzp_live_mVIIEneiAN36tn", "xdp4XcZqydO69ESPF0wc5DdV"))

        data = {"amount": cost*100, "currency": "INR"}
        payment = client.order.create(data=data)

        response_data = {
            'payment': payment,
            'programId': program_id,
            'userId': user_id
        }

        ord_id = payment['id']

        order = Order.objects.create(
            order_id=ord_id,
            program_id=program_id,
            user_id=user_id
        )

        order.save()

        return Response(response_data, status=200)

    except Exception as e:
        print(e)
        return Response(str(e), status=422)


@api_view(['POST'])
def successfulPayment(requests):
    res = json.loads(requests.data["response"])

    print(res)

    ord_id = ""
    raz_pay_id = ""
    raz_signature = ""

    # res.keys() will give us list of keys in res
    for key in res.keys():
        if key == 'razorpay_order_id':
            ord_id = res[key]
        elif key == 'razorpay_payment_id':
            raz_pay_id = res[key]
        elif key == 'razorpay_signature':
            raz_signature = res[key]

    data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
    }

    client = razorpay.Client(
        auth=("rzp_live_mVIIEneiAN36tn", "xdp4XcZqydO69ESPF0wc5DdV"))

    check = client.utility.verify_payment_signature(data)

    if check is not None:
        return Response('Something went wrong', status=204)

    order = Order.objects.get(order_id=ord_id)

    userId = order.user_id
    programId = order.program_id

    user = User.objects.get(id=userId)
    program = Program.objects.get(id=programId)
    cost = program.cost

    customer = Customer.objects.get(user=user)
    customer.programs_bought.append(programId)
    customer.save()

    trainer = Trainer.objects.get(
        programs_created__contains=[programId])

    print(trainer)

    trainer.wallet += cost
    trainer.save()

    return Response(status=200)
