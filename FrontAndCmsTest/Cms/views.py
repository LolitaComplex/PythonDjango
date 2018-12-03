from django.http import HttpResponse

def getIndexPage(request):
    return HttpResponse("后端首页")

def getLoginPage(request):
    return HttpResponse("后端登陆页面")