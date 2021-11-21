from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.db.models.base import Model
from django.contrib.postgres.fields import ArrayField
from rest_framework.serializers import ModelSerializer

# Create your models here.

class Program(models.Model):

    name = models.CharField(max_length=100)
    exercise_id = ArrayField(models.IntegerField())
    sets = ArrayField(models.IntegerField())
    reps = ArrayField(models.IntegerField())
    rest = ArrayField(models.IntegerField())

class Exercise(models.Model):

    name = models.CharField(max_length=100)
    exercise_id = models.IntegerField()
    alt_exercise_id = models.IntegerField(blank=True)
    target_muscles = ArrayField(models.CharField(max_length=50))

class MuscleList(models.Model):

    name = models.CharField(max_length=50)

class AltExerciseList(models.Model):

    name = models.CharField(max_length=100)
    alt_id = models.IntegerField()