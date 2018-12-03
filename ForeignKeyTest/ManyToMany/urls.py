from django.urls import path 
from . import views

urlpatterns = [
    path("", views.manytoMany),
    path("query", views.query)
]