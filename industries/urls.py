from django.urls import path
from .views import IndustryistView 

app_name = "industry"
urlpatterns = [
    path('industries/', IndustryistView.as_view(), name="list_view"),
]