from django.urls import path
from .views import index, SiteFooterView, SiteHeaderView

app_name = "home"
urlpatterns = [
    path('',index),
    path('header',SiteHeaderView.as_view(), name="head"),
    path('footer',SiteFooterView.as_view(), name="foot"),
]