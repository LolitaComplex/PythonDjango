from django.db import models

# Create your models here.
class New(models.Model):
    name = models.CharField(max_length = 50, null = False)

    class Meta:
        db_table = "news"


class Tag(models.Model):
    name = models.CharField(max_length = 50, null = False)
    news = models.ManyToManyField("New", related_name = "tags")

    class Meta:
        db_table = "tags"


