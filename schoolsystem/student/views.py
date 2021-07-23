from django.shortcuts import render

# Create your views here.
from .forms import StudentRegistrationForm

def register_student(request):
    form=StudentRegistrationForm()
    return render(request,"register_student.html",{"form":form})
