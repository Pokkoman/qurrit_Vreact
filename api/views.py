from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import *
from .serializers import *
# Create your views here.


def index(request):
    return HttpResponse("hello ")


@api_view(['GET'])
def getProgramList(requests):

    program_list = Program.objects.all()

    program_list_serialize = ProgramSerializer(program_list, many=True)

    return Response(program_list_serialize.data)


@api_view(['GET'])
def getWorkouts(requests, id):

    workout_list = Workout.objects.all().filter(program_id=id)

    workout_list_serialize = WorkoutSerializer(workout_list, many=True)

    exercise_list_id = []
    for workout in workout_list:
        exercise_list_id.extend(workout.exercise_id)

    exercise_list_id = set(exercise_list_id)

    exercise_list_serialize = []
    for id in exercise_list_id:

        exercise = Exercise.objects.get(id=id)
        exercise_serialize = ExerciseSerializer(exercise, many=False)
        exercise_list_serialize.append(exercise_serialize.data)

    return Response([workout_list_serialize.data, exercise_list_serialize])


@api_view(['GET'])
def getExercises(requests):

    exercise_list = Exercise.objects.all()

    exercise_list_serialize = ExerciseSerializer(exercise_list, many=True)

    return Response(exercise_list_serialize.data)


@api_view(['GET'])
def search(requests, name):

    program_list = Program.objects.all().filter(program_name__icontains=name)

    program_list_serialized = ProgramSerializer(program_list, many=True)

    return Response(program_list_serialized.data)


@api_view(['POST'])
def createProgram(requests):

    data = requests.data
    print(data)
    new_program = Program.objects.create(
        program_name=data[0]['program_name'],
        trainer_name=data[0]['trainer_name'],
        duration=data[0]['duration']
    )
    day = 1
    for workout in data[1:]:
        print(workout)
        new_workout = Workout.objects.create(
            program_id=new_program,
            name=workout['name'],
            exercise_id=workout['exercise_id'],
            sets=workout['sets'],
            reps=workout['reps'],
            rest=workout['rest'],
            day=day
        )
        day += 1

    return HttpResponse("hello")
