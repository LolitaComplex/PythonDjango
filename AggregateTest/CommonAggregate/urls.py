from django.urls import path 
from . import views

urlpatterns = [
    path("", views.bookAvg),
    path("order_price", views.orderBookAvg),
    path("update_price", views.updatePrice),
    path("values", views.values),
    path("orderBy", views.orderBy),
    path("selectRelated", views.selectRelated),
    path("selectRelatedAuthor", views.selectRelatedAuthor),
    path("defer", views.defer)
]