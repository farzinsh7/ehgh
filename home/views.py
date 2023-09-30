from django.shortcuts import render
from django.views.generic import ListView
from .models import SiteInformation

# Create your views here.
class Index(ListView):
    model = SiteInformation
    template_name = 'index.html'
    queryset = SiteInformation.objects.first()


class SiteHeaderView(ListView):
    model = SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()


class SiteFooterView(ListView):
    model = SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()