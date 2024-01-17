import django_filters

from .models import PhotoNasa


class PhotoFilter(django_filters.FilterSet):

    class Meta:
        model = PhotoNasa
        fields = ['title']



