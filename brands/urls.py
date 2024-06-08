from django.urls import path
from .views import BrandsListView, BrandsDetailView

app_name = "brands"
urlpatterns = [
    path('brands/', BrandsListView.as_view(), name="list_view"),
    path('brands/<slug:slug>', BrandsDetailView.as_view(), name='detail_view'),
]