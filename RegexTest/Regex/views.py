from django.http import HttpResponse
from django.shortcuts import reverse
# Create your views here.

def getContentPage(request, year):
    return HttpResponse("这是%s年" % (year))

def getArticleCategory(request, categories):
    url = reverse("article", kwargs={"categories": categories})
    print(url)
    return HttpResponse(str(categories))