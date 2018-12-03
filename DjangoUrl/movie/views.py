from django.http import HttpResponse

def movie(request):
    return HttpResponse("豆瓣电影")