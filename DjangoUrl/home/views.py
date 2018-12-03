from django.http import HttpResponse

def home(request):
    return HttpResponse("豆瓣读书")