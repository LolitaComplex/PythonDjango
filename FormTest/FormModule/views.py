from django.shortcuts import render
from django.http import HttpResponse
from .forms import MessageForm
from django.views.generic.base import View

# Create your views here.

class FormIndex(View):


    def get(self, request, *args, **kwargs):
        return render(request, "form_index.html", context = {"form": MessageForm()})


    def post(self, request, *args, **kwargs):
        form = MessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            email = form.cleaned_data.get("email")
            reply = form.cleaned_data.get("reply")

            print("标题: %s, 内容: %s, 邮箱: %s, 回复: %s" % (title, content ,email, reply))
            return HttpResponse("提交成功")
        else :
            print(form.errors.get_json_data())
            return HttpResponse("提交失败")



