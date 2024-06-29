from django.urls import path
from . import views

app_name = "houses"
urlpatterns = [
    path('houses/', views.HousesListView.as_view(), name="list_view"),
    path('houses/<slug:slug>', views.HousesDetailView.as_view(), name="detail_view"),
]