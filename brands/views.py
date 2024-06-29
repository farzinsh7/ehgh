from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models
from news.models import News
from houses.models import Houses


# Create your views here.
class BrandsListView(ListView):
    model = models.Brands
    queryset = models.Brands.objects.filter(status="p").order_by('-created')
    template_name = 'brands_list.html'
    context_object_name = 'brands'



class BrandsDetailView(DetailView):
    model = models.Brands
    context_object_name = 'brand'
    queryset = models.Brands.objects.filter(status='p')
    template_name = 'brands_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lines'] = Houses.objects.all()
        context['tags'] = models.Tags.objects.filter(status=True)
        context['latest'] = News.objects.filter(status="p").order_by('-publish')[:4]
        return context