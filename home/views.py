from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import SiteInformation, HomeData
from industries.models import Industry
from company.models import Company
from news.models import News
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(cache_page(60 * 15), name='dispatch')
class Index(ListView):
    model = HomeData
    template_name = 'index.html'
    context_object_name = "home"
    queryset = HomeData.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industry'] = Industry.objects.filter(status='p')[:4]
        context['company'] = Company.objects.filter(status='p')
        context['news'] = News.objects.published()[:3]
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class SiteHeaderView(ListView):
    model = SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industry'] = Industry.objects.filter(status='p')[:4]
        return context


@method_decorator(cache_page(60 * 15), name='dispatch')
class SiteFooterView(ListView):
    model = SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()


@cache_page(60*15)
def chached(request):
    user_model = get_user_model()
    all_user = user_model.objects.all()
    return HttpResponse('<html><body><h1>{0} users.. chached</h1></body></html>'.format(len(all_user)))


def chacheless(request):
    user_model = get_user_model()
    all_user = user_model.objects.all()
    return HttpResponse('<html><body><h1>{0} users.. chacheless</h1></body></html>'.format(len(all_user)))