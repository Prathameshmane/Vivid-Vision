from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('base_dash'))
        return super().get(request, *args, **kwargs)