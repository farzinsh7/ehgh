from django.urls import path
from .views import CompanyDetailView

app_name = "company"
urlpatterns = [
    path('company/<slug:slug>', CompanyDetailView.as_view(), name = "detail_view"),
]