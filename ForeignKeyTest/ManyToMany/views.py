from django.http import HttpResponse
from .models import New, Tag

# Create your views here.

def manytoMany(request):
    new = New(name = "IG夺冠")
    new.save()

    tag = Tag(name = "游戏")
    tag.save()

    return HttpResponse("多对多")

def query(request):
    new = New.objects.first()

    tag = Tag.objects.last()
    new.tag_set.add(tag)
    tag.news.add(new)

    return HttpResponse("查询新闻")
