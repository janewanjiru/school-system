from django.db import models
from django.db.models.base import Model

# Create your models here.

class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=20)
    age=models.PositiveBigIntegerField()
    date_of_birth=models.DateField()
    email=models.EmailField()
    student_id=models.CharField(max_length=15)
    student_image=models.ImageField(upload_to='images/')
    city=models.CharField(max_length=10)
    medical_report=models.FileField(upload_to='documents/%Y/%m/%d')
    admission_date=models.CharField(max_length=15)
    class_name=models.CharField(max_length=10)
    room_no=models.CharField(max_length=14)
    guardian_phonenumber=models.CharField(max_length=15)
    guardian_name=models.CharField(max_length=20)
    academic_year=models.DateField(max_length=16)
    passport=models.CharField(max_length=20)
    academic_year=models.DateField(max_length=8)
    gender_choice=((u'F',u'Female'),(u'M',u'Male'))
    gender=models.CharField(max_length=6,choices=gender_choice)
    language_choice=((u'E',u'English'),(u'k',u'Kiswahili'),(u'F',u'French'))
    languages=models.CharField(max_length=15,choices=language_choice)
    nationality_choice=((u'k',u'Kenya'),(u'u',u'Ugandan'),(u'R',U'Rwandese'),(u'S',u'sudanese'),(u'S',u'SouthSudanese'))
    nationality=models.CharField(max_length=15,choices=nationality_choice)

   
    


