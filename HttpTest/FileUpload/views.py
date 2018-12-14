from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("文件上传主页")


class FileUploadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "file_upload.html")

    def post(self, request, *args, **kwargs):
        uploadFile = request.FILES.get("file")
        with open("File/Test.kt", "wb") as targetFile:
            for chunk in uploadFile.chunks():
                targetFile.write(chunk)
        return HttpResponse("上传成功")