from django.urls import path 
from . import views

app_name = "Front"

urlpatterns = [
    path("", views.getIndexPage),
    path("login/", views.getLoginPage, name="MyLogin")
]