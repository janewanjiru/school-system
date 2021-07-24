from django.db import models
from django.db.models.base import Model

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveBigIntegerField()
    gender=models.CharField(max_length=6)
    date_of_birth=models.DateField()
    email=models.EmailField()
    student_id=models.CharField(max_length=15)
    student_image=models.ImageField()
    city=models.CharField(max_length=10)
    nationality=models.CharField(max_length=15)
    medical_report=models.FileField()
    admission_date=models.CharField(max_length=15)
    class_name=models.CharField(max_length=10)
    room_no=models.CharField(max_length=14)
    guardian_phonenumber=models.CharField(max_length=15)
    guardian_name=models.CharField(max_length=20)
    academic_year=models.DateField()
   
    


