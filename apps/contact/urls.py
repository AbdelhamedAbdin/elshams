from . import views
from django.urls import path

app_name = "contact"

urlpatterns = [
    path("", views.ContactUs.as_view(), name="contact-us")
]
