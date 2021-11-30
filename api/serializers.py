from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import *


class WorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class ExerciseSerializer(ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'