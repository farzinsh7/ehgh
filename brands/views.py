from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Brands


# Create your views here.
class BrandsListView(ListView):
    queryset = Brands.objects.filter(status="p").order_by('-created')
    model = Brands
    template_name = 'brands_list.html'
    context_object_name = 'brands'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest'] = Brands.objects.filter(status="p").order_by('-created')[:5]
        return context



class BrandsDetailView(DetailView):
    model = Brands
    context_object_name = 'brands'
    queryset = Brands.objects.filter(status='p')
    template_name = 'brands_detail.html'