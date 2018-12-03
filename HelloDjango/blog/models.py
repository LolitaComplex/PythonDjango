from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length = 300)
    # User是Django预设好的一个Model，这里表示博客文章与用户是多对1的关系
    author = models.ForeignKey(User, on_delete = None, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)

