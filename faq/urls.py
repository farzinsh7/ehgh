from django.urls import path
from . import views

app_name = "faq"
urlpatterns = [
    path('faq/', views.FaqView.as_view(), name = "page"),
]