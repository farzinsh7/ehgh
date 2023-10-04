from django.urls import path
from .views import CompanyDetailView, CompanyListView

app_name = "company"
urlpatterns = [
    path('companies/', CompanyListView.as_view(), name = "list_view"),
    path('companies/<slug:slug>', CompanyDetailView.as_view(), name = "detail_view"),
]