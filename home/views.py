from django.shortcuts import render
from django.views.generic import ListView
from . import models
from news.models import News

class IndexView(ListView):
    model = models.HomeData
    template_name = 'index.html'
    context_object_name = "home"
    queryset = models.HomeData.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.filter(status='p').order_by('-publish')[:3]
        return context



class SiteHeaderView(ListView):
    model = models.SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    queryset = models.SiteInformation.objects.first()



class SiteFooterView(ListView):
    model = models.SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    queryset = models.SiteInformation.objects.first()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest'] = News.objects.filter(status='p').order_by('-publish')[:3]
        return context