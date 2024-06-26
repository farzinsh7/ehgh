from django.views.generic import ListView
from . import models

# Create your views here.
class FaqView(ListView):
    model = models.Faq
    queryset = models.Faq.objects.all()
    template_name = 'faq.html'
    context_object_name = "faq"