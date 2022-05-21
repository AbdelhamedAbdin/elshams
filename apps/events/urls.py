from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("past-events/", views.PastEvents.as_view(), name="past-events"),
]
