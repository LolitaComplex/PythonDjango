from django.http import HttpResponse
from .models import Book, Category
from Author.models import Author
# Create your views here.

def bookIndex(request):
    # category = Category(name = "历史")
    # category.save()

    category = Category.objects.get(pk = 1)

    # book = Book(name = "青年希特勒——脱变从此刻开始", content =   \
    #     "由希特勒年轻时好友库比席克编著，讲述了希特勒青年时家庭、   \
    #     学校、爱好、爱情等等经历。半本书都在都在标书希特勒歇斯底里  \
    #     、神经质、好面子", category = category)

    author = Author(name = "丘吉尔")
    author.save()
    book = Book(name = "二战回忆录", content = "讲述了德国复出到签订慕尼黑协议结束，\
        要回了被法国占领的过去领土, 并且占领了奥利地、斯洛伐克全境", category = category, \
        author = author)
    book.save()

    return HttpResponse("图书主页")


def queryBook(request):
    category = Category.objects.get(pk = 1)
    books = category.book_set.all()
    for book in books:
        print(book)
    return HttpResponse("查询图书")
