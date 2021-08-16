from django.db import models
from django.db.models import Model


# Create your models here.

class Trainer(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    id_number =models.CharField(max_length=12)
    salary=models.PositiveBigIntegerField()
    job_tittle=models.CharField(max_length=20,)
    Photo=models.ImageField(upload_to='images/')
    Email=models.EmailField()
    Resume=models.FileField(upload_to='documents/%Y/%m/%d')
    Days=models.CharField(max_length=7)




