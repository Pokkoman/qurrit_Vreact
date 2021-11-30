from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

import api

from .models import *
from .serializers import *
# Create your views here.

def index(request):
    return HttpResponse("hello ")

@api_view(['GET'])
def getProgramList(requests):

    program_list = Program.objects.all()

    program_list_serialize = ProgramSerializer(program_list,many=True)

    print(program_list_serialize.data)

    return Response(program_list_serialize.data)

@api_view(['GET'])
def getWorkouts(requests,id):

    workout_list = Workout.objects.all().filter(program_id=id)

    workout_list_serialize = WorkoutSerializer(workout_list,many=True)

    exercise_list_id = []
    for workout in workout_list:
        exercise_list_id.extend(workout.exercise_id) 

    exercise_list_id = set(exercise_list_id)

    exercise_list_serialize = []
    for id in exercise_list_id:

        exercise = Exercise.objects.get(id = id)
        exercise_serialize = ExerciseSerializer(exercise,many=False)
        exercise_list_serialize.append(exercise_serialize.data)

    return Response([workout_list_serialize.data,exercise_list_serialize])

@api_view(['GET'])
def search(requests,name):  

    program_list = Program.objects.all().filter(program_name__icontains = name)

    program_list_serialized = ProgramSerializer(program_list,many=True)

    return Response(program_list_serialized.data)


#def createProgram(requests):

    data = [
        { 
            'program_name' : 'TestProgam2',
            'trainer_name' : 'Trainer2'
        },
        { #Workout 1

            'name' : 'workout21',
            'exercise_id' : [1,2,3],
            'sets' : [3,3,3],
            'reps' : [10,10,10],
            'rest' : [60,60,60]
        },
        { #Workout 2

            'name' : 'workout22',
            'exercise_id' : [1,2,3],
            'sets' : [3,3,3],
            'reps' : [10,10,10],
            'rest' : [60,60,60]
        },
        { #Workout 3

            'name' : 'workout23',
            'exercise_id' : [1,2,3],
            'sets' : [3,3,3],
            'reps' : [10,10,10],
            'rest' : [60,60,60]
        },
        { #Workout 4

            'name' : 'workout24',
            'exercise_id' : [1,2,3],
            'sets' : [3,3,3],
            'reps' : [10,10,10],
            'rest' : [60,60,60]
        },
    ]

    
    new_program = Program.objects.create(
        program_name = data[0]['program_name'],
        trainer_name = data[0]['trainer_name']
    )

    for workout in data[1:]:

        new_workout = Workout.objects.create(
            program_id = new_program,
            name = workout['name'],
            exercise_id = workout['exercise_id'],
            sets = workout['sets'],
            reps = workout['reps'],
            rest = workout['rest']
        )


    return HttpResponse("hello")