from django.urls import path
from . import views

urlpatterns = [
    path("", views.FormIndex.as_view())
]