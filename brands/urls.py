from django.urls import path
from . import views

app_name = "brands"
urlpatterns = [
    path('brands/', views.BrandsListView.as_view(), name="list_view"),
    path('brands/<slug:slug>', views.BrandsDetailView.as_view(), name='detail_view'),
]