from django.db import models


# Create your models here.

class Courses(models.Model):
    course_name=models.CharField(max_length=20)
    Trainer=models.CharField(max_length=12)
    course_code=models.CharField(max_length=12)
    syllabus=models.FileField(upload_to='documents/%y/%m/%d',null=True)
    Description=models.TextField()
