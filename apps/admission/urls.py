from . import views
from django.urls import path

app_name = "admission"

urlpatterns = [
    path("", views.AdmissionView.as_view(), name="admission"),
]
