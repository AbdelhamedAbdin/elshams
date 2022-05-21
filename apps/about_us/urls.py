from . import views
from django.urls import path

app_name = "about_us"

urlpatterns = [
    path("", views.AboutUs.as_view(), name="about-us"),
]