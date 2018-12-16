from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.forms import widgets
from django.contrib import messages
from django.contrib.messages.api import get_messages


# Create your views here.
def index(request):
    return redirect(reverse("UserIndex"))


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "login.html")

    def post(self, request, *args, **kwargs):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = loginForm.getUser
            request.session["userId"] = user.pk
            return redirect(reverse("UserIndex"))
        else:
            messages.info(request, loginForm.get_errors()[0])

        return render(request, "login.html")


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "register.html")

    def post(self, request, *args, **kwargs):
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            registerForm.save()
            return HttpResponse("注册成功")
        else:
            messages.info(request, registerForm.get_errors()[0])
        return render(request, "register.html")



class TransferView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "transfer.html")

    def post(self, request, *args, **kwargs):
        return HttpResponse("转账成功")


def logout(request):
    return HttpResponse("注销成功")
