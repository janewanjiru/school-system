from django import forms
from . models import Events

class EventsRegistrationForm(forms.ModelForm):
    class Meta:
        model=Events
        fields="__all__"