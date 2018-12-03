from django.http import HttpResponse
from django.shortcuts import redirect, reverse

def getIndexPage(request):
    dictGet = request.GET
    print(request.resolver_match.namespace)
    if (dictGet.get("username")):
        return HttpResponse("前端首页")
    else:
        return redirect(reverse("Front:MyLogin"))

def getLoginPage(request):
    return HttpResponse("前端登陆页")