"""HttpTest URL Configuration

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
from django.urls import path
from . import views

app_name = "Method"

urlpatterns = [
    path('', views.index, name="RequestGet"),
    path('requestGet', views.requestGet),
    path('requestPostForm', views.requestPostForm),
    path('requestPostJson', views.requestPostJson),
    path('requestPostText', views.requestPostText),
    path('requestPostMultipart', views.requestPostMultipart),
    path("littleFileDownload", views.littleFileDownload),
    path("littleFileMakeByTemplatesDownload", views.littleFileMakeByTemplatesDownload),
    path("bigFileDownload", views.bigFileDownload),
    path("bigFileOtherDownload", views.bigFileOtherDownload),
    path("bigFileBadDownload", views.bigFileBadDownload),
    path("bigFileCsvDownload", views.bigFileCsvDownload),
    path("download/<fileName>", views.downloadMidia)
]
