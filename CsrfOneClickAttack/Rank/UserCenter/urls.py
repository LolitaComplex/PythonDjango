from django.urls import path
from . import views

app_name = "UserView"

urlpatterns = [
    path("", views.index),
    path("login", views.LoginView.as_view(), name = "Login"),
    path("register", views.RegisterView.as_view(), name = "Register"),
    path("transfer", views.TransferView.as_view(), name = "Transfer"),
    path("logout", views.logout, name = "Logout")
]