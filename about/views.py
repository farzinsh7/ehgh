from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class AboutView(ListView):
    model = models.AboutCompany
    queryset = models.AboutCompany.objects.first()
    template_name = 'about.html'
    context_object_name = "about"