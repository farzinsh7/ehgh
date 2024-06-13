from django.urls import path
from . import views

app_name = "page"
urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
    path('header/', views.SiteHeaderView.as_view(), name="head"),
    path('footer/', views.SiteFooterView.as_view(), name="footer"),
]