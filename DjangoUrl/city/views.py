from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getDetail(request, detailId):
    name = request.GET["name"]
    return HttpResponse("城市详情 %s \t 名称：%s" % (detailId, name))cd