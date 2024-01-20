from django.urls import path

from . import views

urlpatterns = [
    path("", views.photo_filter, name="index")
]

