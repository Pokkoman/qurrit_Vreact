from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Order(models.Model):

    order_id = models.CharField(max_length=200)
    program_id = models.IntegerField()
    user_id = models.IntegerField()
