from django.views.generic import TemplateView

from .models import PhotoNasa


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photos'] = PhotoNasa.objects.all()
        return context

