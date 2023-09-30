from django.urls import path
from .views import Index, SiteFooterView, SiteHeaderView

app_name = "page"
urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('header/', SiteHeaderView.as_view(), name="head"),
    path('footer/', SiteFooterView.as_view(), name="foot"),
]