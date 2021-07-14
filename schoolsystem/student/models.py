from django.db import models
from django.db.models.base import Model

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveBigIntegerField()
    birth_date=models.DateField()
