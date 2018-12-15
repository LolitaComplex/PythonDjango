from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from django.http import HttpResponse

# Create your views here.
def index(request):
    return redirect(reverse("UserIndex"))

class LoginView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        
        return redirect(reverse("UserIndex"))


class RegisterView(View):

    def get(self, request, *args, **kwargs):

        return render(request, "register.html")

    def post(self, request, *args, **kwargs):

        return HttpResponse("注册成功")


class TransferView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "transfer.html")

    def post(self, request, *args, **kwargs):
        return HttpResponse("转账成功")


def logout(request):
    return HttpResponse("注销成功")