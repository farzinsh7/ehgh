from django.views.generic import ListView
from . import models
from home.models import SiteInformation

# Create your views here.
class AboutView(ListView):
    model = models.AboutCompany
    queryset = models.AboutCompany.objects.first()
    template_name = 'about.html'
    context_object_name = "about"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = SiteInformation.objects.first()
        return context