from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

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
    