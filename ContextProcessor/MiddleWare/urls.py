from django.urls import path
from . import views

app_name = "MiddleWareView"

urlpatterns = [
    path("", views.index, name = "Index")
]