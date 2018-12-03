from django.urls import path
from . import views

urlpatterns = [
    path("", views.student),
    path("student", views.getStudent),
]