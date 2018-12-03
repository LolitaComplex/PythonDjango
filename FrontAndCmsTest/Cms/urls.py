from django.urls import path 
from . import views

app_name = "Cms"

urlpatterns = [
    path("", views.getIndexPage),
    path("login/", views.getLoginPage, name="MyLogin")
]