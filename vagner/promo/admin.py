from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from django.utils.safestring import mark_safe

from .models import PhotoNasa


@admin.register(PhotoNasa)
class PhotoNasaAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'title', 'show_photo']

    @admin.display(description='Фотография')
    def show_photo(self, obj: PhotoNasa):
        if obj.image:
            return mark_safe(f"<img src='{obj.image.url}' width=60 height=50 />")
