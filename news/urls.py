from django.urls import path
from . import views

app_name = "news"
urlpatterns = [
    path('news/', views.NewsListView.as_view(), name="list_view"),
    path('news/<slug:slug>', views.NewsDetailView.as_view(), name='detail_view'),
]