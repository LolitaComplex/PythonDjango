from django.urls import path
from . import views

app_name = "Articles"

urlpatterns = [
    path("show", views.ArticleListView.as_view(), name = "ListView"),
    path("createData", views.createData)
]