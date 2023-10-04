from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Company

# Create your views here.
class CompanyListView(ListView):
    queryset = Company.objects.filter(status="p")
    model = Company
    template_name = 'company_list.html'
    context_object_name = 'company'


class CompanyDetailView(DetailView):
    model = Company
    queryset = Company.objects.filter(status='p')
    context_object_name = "company"
    template_name = 'company_detail.html'

