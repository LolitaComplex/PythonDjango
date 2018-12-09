from django.shortcuts import render
from django.http.request import QueryDict
# from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET, require_POST, require_safe
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "method_index.html")

# @require_http_methods(["GET"])
@require_GET
def requestGet(request):
    getDict = request.GET
    context = {}
    username, icon, fuck = ("username", "icon", "fuck")
    context[username] = getDict.get(username)
    context[icon] = getDict.get(icon)
    context[fuck] = getDict.get(fuck)
    return render(request, "method_get.html", context = context)

@require_POST
def requestPost(request):
    postDict = request.POST
    print("%s : %s" % (postDict.get("username"), postDict.get("password")))
    return render(request, "mothod_post.html")

def requestTest(request):
    
    return render(request, "method_request.html")
    

