from statistics import mode
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=CASCADE)
    programs_bought = ArrayField(models.IntegerField())
    image = models.URLField(max_length=200, blank=True)


class Trainer(models.Model):

    user = models.OneToOneField(User, on_delete=CASCADE)
    programs_created = ArrayField(models.IntegerField())
    wallet = models.IntegerField(default=0, blank=True, null=True)
    image = models.URLField(max_length=200, blank=True)
