from django.shortcuts import render
from .forms import EventsRegistrationForm

# Create your views here.


def register_events(request):
    if request.method == "POST":
        form=EventsRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)    
    else:
        form=EventsRegistrationForm() 
    return render(request,"register_events.html",{"form":form})
