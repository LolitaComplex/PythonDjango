from django.shortcuts import render, redirect, reverse
from django.http.request import QueryDict
# from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_GET, require_POST, require_safe
from django.http import HttpResponse, StreamingHttpResponse, HttpRequest, FileResponse
from django.template import loader
from django.views.decorators.cache import cache_control

import csv
import json


# Create your views here.
def index(request):
    return render(request, "method_index.html")

# @require_http_methods(["GET"])
# @cache_control(public=True, max_age=10)
@require_GET
def requestGet(request):
    getDict = request.GET
    context = {}
    username, icon, fuck = ("username", "icon", "fuck")
    context[username] = getDict.get(username)
    context[icon] = getDict.get(icon)
    context[fuck] = getDict.get(fuck)

    via = request.META.get("Via")
    forwards = request.META.get("Max-Forwards")
    print(via)
    print(forwards)
    print("访问了Django服务器")
    return render(request, "method_get.html", context = context)

@require_POST
def requestPostForm(request):
    postDict = request.POST
    print("%s : %s" % (postDict.get("username"), postDict.get("password")))
    return render(request, "mothod_post.html")

def requestPostJson(request):
    dictBody = json.loads(request.body)
    print(dictBody)
    return render(request, "method_post_json.html")

def requestPostText(request):
    body = request.body
    print(body.decode("utf-8"))
    return render(request, "method_post_text.html")

    
def requestPostMultipart(request):
    body = request.body
    print(body.decode("utf-8"))
    return render(request, "method_post_multipart.html")

def requestTest(request):
    # TODO
    return render(request, "method_request.html")

def littleFileDownload(request):
    """ 普通的输出小文件 """
    response = HttpResponse(content_type = "text/csv")
    response["Content-Disposition"] = 'attachment; filename = "XOD-1452.csv"'

    writer = csv.writer(response) # 初始化csv输出流对象
    writer.writerow(("username", "age", "content")) # 注意这里每一行都是List，也是csv框架接收的参数形式
    writer.writerow(("库比席克", 55, "你为什么没有杀了他？"))

    return response

def littleFileMakeByTemplatesDownload(request):
    """ 通过Template模板生成文本 """
    response = HttpResponse(content_type = "text/csv")
    response["Content-Disposition"] = "attachment; filename='PIX-776.csv'"

    template = loader.get_template("templateModel.txt")
    # 字符串类型
    content = template.render({"list": (
        ("Title", "Author", "Content"),
        ("白夜行", "东野圭吾", "牛逼"),
        ("青年希特勒", "库比席克", "神经质、歇斯底里、有目标并为之付出了奋斗。脱变从那一刻开始")
    )})

    response.write(content)
    return response

def bigFileDownload(request):
    """ 下载大文件 成员赋值"""
    response = StreamingHttpResponse(content_type = "text/csv")
    response["Content-Disposition"] = "attachment; filename='BIG-1234.csv'"
    rows = ("rows {0}, {1}, {2}\n".format(x , x, x) for x in range(500000))
    response.streaming_content = rows
    return response


def bigFileOtherDownload(request):
    """ 下载大文件 构造函数赋值"""

    rows = ("rows {0}, {1}, {2}\n".format(x , x, x) for x in range(500000))

    response = StreamingHttpResponse(rows, content_type = "text/csv")
    response["Content-Disposition"] = "attachment; filename='BIG-134.csv'"

    return response

class Echo:

    def write(self, value):
        return value


def bigFileCsvDownload(request):
    """ 文件下载与上边两个一模一样，不过是一种csv框化的特殊使用方式 """
    # csv的创建writer对象，这里Echo的write()函数返回值决定了writer.writerow()方法的返回值。傻逼
    writer = csv.writer(Echo())
    
    # 这个列表生成器每一个元素都是一个 List
    rows = (["Row: %d" % (x), {"Lily: %d" % (x)}, "Tom: %d" % (x)] for x in range(500000))

    # 这里的writer.writerow很欺骗，实际上不会向哪写入值，而是调用csv库的拼接字符串方法后，返回Echo.write()
    response = StreamingHttpResponse((writer.writerow(row) for row in rows))
    response["Content-Disposition"] = "attachment; filename = 'Best-332.csv'"

    return response

def bigFileBadDownload(request):
    """ 糟糕的下载方式 """
    response = HttpResponse(content_type = "text/csv")
    response["Content-Disposition"] = "attachment; filename='Bad-233.csv'"

    rows = ("rows {0}, {1}, {2}\n".format(x , x, x) for x in range(500000))
    content = ""
    for row in rows:
        content += row

    response.content = content
    return response

def downloadMidia(request, fileName):
    targetFile = open("medias/%s" % (fileName), "rb")
    response = FileResponse(targetFile)
    response["Content-Type"] = "application/octet-steam"
    response["Content-Disposition"] = "attachment; filename=%s" % (fileName)
    return response

    

