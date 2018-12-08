from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("createData", views.createData),
    path("question1", views.question1), 
    path("question2", views.question2), 
    path("question3", views.question3), 
    path("question4", views.question4), 
    path("question5", views.question5), 
    path("question6", views.question6), 
    path("question7", views.question7), 
    path("question8", views.question8), 
    path("question9", views.question9), 
    path("question10", views.question10), 
    path("question11", views.question11), 
    path("question12", views.question12), 
    path("question13", views.question13), 
    path("question14", views.question14), 
    path("question15", views.question15)
]