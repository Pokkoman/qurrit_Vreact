from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api

from .models import Program
from .serializers import ProgramSerializer
# Create your views here.

def index(request):
    return HttpResponse("hello ")

@api_view(['GET'])
def getProgram_list(request):
    
    program_list= Program.objects.all()
    program_list_serializer = ProgramSerializer(program_list,many = True)


    return Response(program_list_serializer.data)

@api_view(['GET'])
def getProgram(request,id):

    program = Program.objects.get(id=id)
    program_serializer = ProgramSerializer(program,many = False)

    return Response(program_serializer.data)

@api_view(['POST'])
def createProgram(request):

    data = request.data

    new_program = Program.objects.create(
        name = data['name'],
        trainer_name = data['trainer_name'],
        exercise_id = data['exercise_id'],
        sets = data['sets'],
        reps = data['reps'],
        rest = data['rest'],

    )

    new_program_serialize = ProgramSerializer(new_program,many= False)

    return Response(new_program_serialize.data)