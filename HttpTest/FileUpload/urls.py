from django.urls import path
from . import views
from .views import FileUploadView

urlpatterns = [
    path("", views.index), 
    path("upload", FileUploadView.as_view())
]