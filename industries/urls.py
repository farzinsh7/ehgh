from django.urls import path
from .views import IndustryistView, IndustryDetailView

app_name = "industry"
urlpatterns = [
    path('industries/', IndustryistView.as_view(), name="list_view"),
    path('industries/<slug:slug>', IndustryDetailView.as_view(), name='detail_view'),
]