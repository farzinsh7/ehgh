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


class IndustryDetailView(DetailView):
    model = Industry
    context_object_name = 'industry'
    queryset = Industry.objects.filter(status='p')
    template_name = 'industry_detail.html'