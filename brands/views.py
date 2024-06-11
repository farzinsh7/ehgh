from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Brands, Line, Tags


# Create your views here.
class BrandsListView(ListView):
    model = Brands
    queryset = Brands.objects.filter(status="p").order_by('-created')
    template_name = 'brands_list.html'
    context_object_name = 'brands'



class BrandsDetailView(DetailView):
    model = Brands
    context_object_name = 'brand'
    queryset = Brands.objects.filter(status='p')
    template_name = 'brands_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lines'] = Line.objects.filter(status=True)
        context['tags'] = Tags.objects.filter(status=True)
        context['latest'] = Brands.objects.filter(status="p").order_by('-created')[:4]
        return context