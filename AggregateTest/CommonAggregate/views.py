from django.db.models import Avg, F, Q, Count, Prefetch
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


def values(request):
    books = Book.objects.values("id", "name", auhorName = F("author__name"), publisherName = F("publisher__name"))
    print("这是数据库的图示")
    for book in books:
        print(book)

    __printSql()
    return HttpResponse("Values")

def orderBy(reuqest):
    books = Book.objects.annotate(bookCount = Count("bookorder__book_id")) \
        .values("id", "name", "bookCount") \
        .order_by("create_time")

    print("集合函数等等练习：")
    for book in books:
        print("%s ...BookCOunt" % (book))

    __printSql()
    return HttpResponse("OrderBy")

def selectRelated(request):
    print("效率低的方式：")
    books = Book.objects.all()
    for book in books:
        print("%s : %s" % (book, book.author))

    print("高效点的方式：")
    books = Book.objects.all().select_related("author")
    for book in books:  
        print("%s : %s" % (book, book.author))

    __printSql()
    return HttpResponse("StaticRelated")


def selectRelatedAuthor(request):
    authors = Author.objects.all()
    for author in authors:
        print("%s : %s" % (author, author.books.all()))

    print("=" * 50)

    authors = Author.objects.prefetch_related("books")
    for author in authors:
        print("%s : %s" % (author, author.books.all()))

    print("=" * 50)

    prefetch = Prefetch("books", queryset = Book.objects.filter(rating__gte = 5))
    authors = Author.objects.prefetch_related(prefetch)
    for author in authors:
        print("%s : %s" % (author, author.books.all()))

    __printSql()
    return HttpResponse("查询作者")

def defer(request):
    books = Book.objects.select_related("author").defer("name")
    for book in books:
        print(book.rating)
    __printSql()
    return HttpResponse("Defer")


def __printSql():
    print("运行的全部Sql语句：")
    for sql in connection.queries:
        print(sql)


