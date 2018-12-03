from django.shortcuts import render
from .models import BlogArticles

# Create your views here.
def blogTitle(request):
    blogs = BlogArticles.objects.all()
    return render(request, "blog/titles.html", {"blogs": blogs})

