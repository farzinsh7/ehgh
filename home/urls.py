from django.urls import path
from home.views import IndexView

app_name = "page"
urlpatterns = [
    path('', IndexView.as_view(), name="home"),
]