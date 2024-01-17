from django.views.generic import TemplateView
from django.shortcuts import render

from .models import PhotoNasa
from .filters import PhotoFilter


def photo_filter(request):
    photos = PhotoFilter(request.GET,
                         queryset=PhotoNasa.objects.all())
    return render(request,
                  'index.html',
                  {'photos': photos})



