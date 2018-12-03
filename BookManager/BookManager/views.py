from django.shortcuts import render
from django.db import connection
from django.shortcuts import redirect, reverse

def __getCorsor():
    return connection.cursor()

def __close(func):
    cursor = __getCorsor()
    try:
        return func(cursor)
    finally:
        cursor.close()


def index(request):
    def func(cursor):
        cursor.execute("select * from book")
        rows = cursor.fetchall()
        context = {
            "books": rows
        }
        print(context)

        return render(request, "index.html", context = context)

    return __close(func)


def bookManager(request):
    return render(request, "book_manager.html")

def addBook(request):
    def func(cursor):
        getParms = request.GET
        sql = "insert into book(name, author) values ('%s', '%s')" \
            % (getParms.get("name"), getParms.get("author"))

        cursor.execute(sql)
        return redirect(reverse("index"))

    return __close(func)


def updateBook(request):
    def func(cursor):
        sql = "update book set name='冰与火之歌' where name='None'"
        cursor.execute(sql)
        return redirect(reverse("index"))

    return __close(func)
   

def deleteBook(request):
    return render(request, "deleteBook.html")