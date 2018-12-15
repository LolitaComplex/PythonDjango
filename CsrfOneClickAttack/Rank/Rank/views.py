from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def redictIndex(request):
    return redirect(reverse("RankIndex"))

def userIndex(request):
    return HttpResponse("用户主页")