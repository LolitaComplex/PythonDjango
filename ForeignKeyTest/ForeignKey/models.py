from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length = 100, null = False)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete = models.CASCADE, related_name = "books")
    author = models.ForeignKey("Author.Author", on_delete = models.SET_NULL, default = None, null = True)

    class Meta:
        db_table = "book"

    def __str__(self):
        return "Book:{{name:{name}, content:{content}, \n category: {{ \
            categoryName:{categoryName}}} author: {author}}}".format(name\
             = self.name, content = self.content,categoryName = self.category.name,\
              author = self.author)

class Category(models.Model):
    name = models.CharField(max_length = 100, null = False)

    class Meta:
        db_table = "category"

