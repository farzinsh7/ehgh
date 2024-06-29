from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from brands.models import Brands

# Create your views here.
class HousesListView(ListView):
    model = models.Houses
    queryset = models.Houses.objects.all()
    template_name = 'houses_list.html'
    context_object_name = 'houses'


class HousesDetailView(DetailView):
    model = models.Houses
    context_object_name = 'house'
    queryset = models.Houses.objects.all()
    template_name = 'houses_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = Brands.objects.filter(line=self.object)
        return context
    