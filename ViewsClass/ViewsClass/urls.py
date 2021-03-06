"""ViewsClass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
from django.views.generic import TemplateView 


urlpatterns = [
    path("get/", views.BaseView.as_view()),
    path("get/<bookId>/", views.BaseView.as_view()),
    path("tempate_view/", TemplateView.as_view(template_name = 'tempate_view.html')),
    path("about_view/", views.AboutView.as_view()),
    path("list_view/", include("ListView.urls"))
]
