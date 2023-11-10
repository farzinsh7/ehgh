from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News

# Create your views here.
class NewsListView(ListView):
    queryset = News.objects.published()
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest'] = News.objects.published()[:5]
        return context

class NewsDetailView(DetailView):
    model = News
    context_object_name = 'news'
    queryset = News.objects.published()
    template_name = 'news_detail.html'