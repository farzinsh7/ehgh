from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class NewsListView(ListView):
    queryset = models.News.objects.published()
    model = models.News
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 9


class NewsDetailView(DetailView):
    model = models.News
    context_object_name = 'news'
    queryset = models.News.objects.published()
    template_name = 'news_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest'] = models.News.objects.published()[:3]
        context['category'] = models.Category.objects.filter(status=True)
        context['tags'] = models.Tags.objects.filter(status=True)
        return context