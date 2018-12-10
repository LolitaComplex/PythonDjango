from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50, null = False)
    content = models.TextField(null = False)
    create_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "article"
