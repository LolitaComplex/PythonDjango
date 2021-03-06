from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, TransferForm
from django.forms import widgets
from django.contrib import messages
from django.contrib.messages.api import get_messages
from .models import User
from django.db.models import F
from django.db import transaction
from django.utils.decorators import method_decorator
from .decorrators import loginDecorator


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


@method_decorator(loginDecorator, name="dispatch")
class TransferView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "transfer.html")

    def post(self, request, *args, **kwargs):
        transferForm = TransferForm(request.POST)
        if transferForm.is_valid():
            targetUserId = transferForm.getUserId
            currentUsereId = request.session.get("userId")
            money = transferForm.cleaned_data.get("money")
            self.__updateMoney(targetUserId, currentUsereId, money)
            return HttpResponse("转账成功")
        else :
            messages.info(request, transferForm.get_errors()[0])
        return render(request, "transfer.html")

    @transaction.atomic
    def __updateMoney(self, targetUserId, currentUsereId, money):
        User.objects.filter(pk = targetUserId).update(money=F("money") + float(money))
        User.objects.filter(pk = currentUsereId).update(money=F("money") - float(money))


def logout(request):
    request.session.flush()
    return redirect(reverse("RankIndex"))

