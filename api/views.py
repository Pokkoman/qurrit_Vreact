from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import *
from .serializers import *
from accounts.models import Trainer
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
def searchall(requests):
    program_list = Program.objects.all()
    program_list_serialized = ProgramSerializer(program_list, many=True)

    return Response(program_list_serialized.data)


@api_view(['GET'])
def search(requests, name):

    program_list = Program.objects.all().filter(program_name__icontains=name)

    program_list_serialized = ProgramSerializer(program_list, many=True)

    return Response(program_list_serialized.data)


@api_view(['POST'])
def createProgram(requests):

    data = requests.data

    trainer_id = data['trainerId']
    new_program = Program.objects.create(
        program_name=data['programName'],
        trainer_name=data['trainerName'],
        duration=data['duration'],
        cost=data['cost'],
        image=data['imageURL']

    )
    day = 1
    for workout in data['workoutList']:

        exercise_id = []
        sets = []
        reps = []
        rests = []
        for exercise in workout['exerciseList']:
            exercise_id.append(exercise['exerciseId'])
            sets.append(exercise['sets'])
            reps.append(exercise["reps"])
            rests.append(exercise['rest'])

        new_workout = Workout.objects.create(
            program_id=new_program,
            name=workout['workoutName'],
            exercise_id=exercise_id,
            sets=sets,
            reps=reps,
            rest=rests,
            day=day
        )
        day += 1

        new_workout.save()
        new_program.save()

    trainer = Trainer.objects.all().get(id=trainer_id)
    trainer.programs_created.append(new_program.id)
    trainer.save()

    return HttpResponse("Program created")
