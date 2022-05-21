from django.urls import path

from . import views

app_name = "gallery"

urlpatterns = [
    path("", views.GalleryViews.as_view(), name="galleries")
]
