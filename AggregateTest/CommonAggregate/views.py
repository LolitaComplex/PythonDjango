from django.db.models import Avg, F, Q
from django.db import connection
from django.http import HttpResponse
from .models import Book, BookOrder, Author

# Create your views here.
def bookAvg(request):
    priceAvg = Book.objects.aggregate(bookAvg = Avg("price"))
    print("图书平均价格：%s" % (priceAvg))
    print(connection.queries)
    return HttpResponse("聚合函数AVG")

def orderBookAvg(reuqest):
    priceAvg = Book.objects.annotate(boomPriceAvg = Avg("bookorder__price"))
    print("平均价格：")
    for price in priceAvg:
        print("%s ...... %s" % (price, price.bookPriceAvg))
    
    print("SQL语句：")
    for sql in connection.queries:
        print(sql)
    return HttpResponse("取订单表的价格AVG")

def updatePrice(request):
    # Book.objects.update(price = F("price") + 10)
    filter = Author.objects.filter(name = F("email"))
    print(filter)
    books = Book.objects.filter(rating__lt = 3, price__gt = 90)
    books = Book.objects.filter(Q(rating__lt = 3) & Q(price__gt = 90))
    books = Book.objects.filter(Q(rating__lt = 3) | Q(price__gt = 90))
    for book in books:
        print(book)
    print(connection.queries)
    return HttpResponse("F表达式更新")

