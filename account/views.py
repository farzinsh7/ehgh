from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
from industries.models import Industry
from news.models import News
from contact_us.models import ContactUS
from company.models import Company
# Create your views here.

class Account(LoginRequiredMixin, ListView):
    model = User
    template_name = 'registration/account.html'
    # queryset = MusicPlayer.objects.all().count    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['industry'] = Industry.objects.filter(status="p").count
        context['news'] = News.objects.filter(status="p").count
        context['company'] = Company.objects.filter(status="p").count
        context['contact'] = ContactUS.objects.all().count

        return context


class CompanyList(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'registration/companies_list.html'
    paginate_by = 10
    queryset = Company.objects.all().order_by("-created")
