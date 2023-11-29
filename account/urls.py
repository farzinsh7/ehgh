from django.contrib.auth import views
from django.urls import path
from .views import Account, CompanyList, CompanyCreate, CompanyUpdate


app_name = "account"
urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    # path("password_change/", PasswordChange.as_view(), name="password_change"),
    # path("password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done",),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path("password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done",),
    # path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm",),
    # path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
]

urlpatterns += [
    path("", Account.as_view(), name="dash"),
    path("companies/", CompanyList.as_view(), name="company"),
    path("companies/create", CompanyCreate.as_view(), name="company_create"),
    path('companies/update/<int:pk>', CompanyUpdate.as_view(), name='company_update'),
]