from django.shortcuts import render
from django.db.models import Avg
from django.db import connection
from django.http import HttpResponse
from .models import Book

# Create your views here.
def bookIndex(request):
    priceAvg = Book.objects.aggregate(doing = Avg("price"))
    print("图书平均价格：%s" % (priceAvg))
    print(connection.queries)
    return HttpResponse("聚合函数AVG")
