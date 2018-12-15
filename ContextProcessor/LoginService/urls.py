from django.urls import path 
from . import views

app_name = "ContextView"

urlpatterns = [
    path("", views.index, name = "Index"),
    path("video", views.videoIndex, name = "VideoIndex"),
    path("book", views.bookIndex, name = "BookIndex"),
    path("login", views.LoginView.as_view(), name = "Login"),
    path("register", views.RegisterView.as_view(), name = "Register"),
    path("debug", views.debugIndex, name = "DebugIndex"),
    path("messages", views.messageIndex, name = "MessageIndex"),
    path("media", views.mediaIndex, name = "MediaIndex")
]