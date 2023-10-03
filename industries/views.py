from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Industry


# Create your views here.
class IndustryistView(ListView):
    queryset = Industry.objects.filter(status="p")
    model = Industry
    template_name = 'industry_list.html'
    context_object_name = 'industry'
    # paginate_by = 1