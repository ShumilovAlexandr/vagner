from django.urls import path

from . import views

urlpatterns = [
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.photo_filter, name="index")
]

