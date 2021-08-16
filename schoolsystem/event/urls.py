from django.urls import path
from.views import register_events

urlpatterns=[
    path("register",register_events,name="register_event")
]