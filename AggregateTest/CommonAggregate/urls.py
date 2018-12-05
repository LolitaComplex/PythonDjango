from django.urls import path 
from . import views

urlpatterns = [
    path("", views.bookAvg),
    path("order_price", views.orderBookAvg),
    path("update_price", views.updatePrice)
]