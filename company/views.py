from django.shortcuts import render
from django.views.generic import DetailView
from .models import Company

# Create your views here.
class CompanyDetailView(DetailView):
    model = Company
    queryset = Company.objects.filter(status='p')
    context_object_name = "company"
    template_name = 'company_detail.html'

