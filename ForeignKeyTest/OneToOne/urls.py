from django.urls import path 
from . import views

urlpatterns = [
    path("", views.oneToOne),
    path("query/", views.query)
]