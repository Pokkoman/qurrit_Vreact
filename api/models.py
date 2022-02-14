from typing import Callable
from unicodedata import name
from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.db.models.base import Model
from django.contrib.postgres.fields import ArrayField
from django.db.models.deletion import CASCADE
from rest_framework.serializers import ModelSerializer

# Create your models here.


class Exercise(models.Model):

    name = models.CharField(max_length=100)
    target_muscles = ArrayField(models.CharField(max_length=50))

    def __str__(self):
        return self.name


class MuscleList(models.Model):

    name = models.CharField(max_length=50)


class Program(models.Model):

    program_name = models.CharField(max_length=200)
    trainer_name = models.CharField(max_length=150)
    duration = models.IntegerField()
    cost = models.IntegerField()
    image = models.URLField(max_length=200, blank=True)
    description = models.CharField(max_length=5000, blank=True)

    def __str__(self):
        return self.program_name


class Workout(models.Model):

    program_id = models.ForeignKey(Program, on_delete=CASCADE)
    name = models.CharField(max_length=100)
    day = models.IntegerField()
    exercise_id = ArrayField(models.IntegerField())
    sets = ArrayField(models.IntegerField())
    reps = ArrayField(models.IntegerField())
    rest = ArrayField(models.IntegerField())

    def __str__(self):
        return self.name
