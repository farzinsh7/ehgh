from django.urls import path
from .views import Index, SiteFooterView, SiteHeaderView, chached, chacheless

app_name = "page"
urlpatterns = [
    path('', Index.as_view(), name="home"),
    path('header/', SiteHeaderView.as_view(), name="head"),
    path('footer/', SiteFooterView.as_view(), name="foot"),
    path('chached/', chached, name="chached"),
    path('chacheless/', chacheless, name="chacheless"),
]