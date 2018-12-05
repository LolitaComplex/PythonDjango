from django.db import models

class Author(models.Model):
    """作者模型"""
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()

    class Meta:
        db_table = 'author'

class Publisher(models.Model):
    """出版社模型"""
    name = models.CharField(max_length=300)

    class Meta:
        db_table = 'publisher'


class Book(models.Model):
    """图书模型"""
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.FloatField()
    rating = models.FloatField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return "Book:{{name:{name}, pages:{pages}, price:{price}, rating:{rating}, author:{author}}}"\
            .format(name = self.name, pages = self.pages, price = self.price, rating = self.rating, author = self.author)


    class Meta:
        db_table = 'book'

class BookOrder(models.Model):
    """图书订单模型"""
    book = models.ForeignKey("Book",on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        db_table = 'book_order'