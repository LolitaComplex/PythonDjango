from django.shortcuts import render
from django.views.generic.base import View
from .forms import RegisterForm, LoginForm
from .models import User
from django.shortcuts import redirect, reverse
from django.http import HttpResponse


# Create your views here.
def index(request):
    userId = request.session.get("userId")
    context = {}
    try:
        user = User.objects.get(pk = userId)
        context["user"] = user
        context["isLogin"] = True
    except :
        context["isLogin"] = False
    return render(request, "login_service_index.html", context = context)


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "login.html", context = {"form": LoginForm()})

    def post(self, request, *args, **kwargs):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data.get("username")
            password = loginForm.cleaned_data.get("password")
            user = User.objects.filter(username = username, password = password).first()
            if user :
                request.session["userId"] = user.id
                return redirect(reverse("ContextView:Index"))
            else :
                return HttpResponse("账号不存在")
        else :
            print(loginForm.get_json_data())
            return HttpResponse("登陆失败")


class RegisterView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "register.html", context = {"form": RegisterForm()})
    
    def post(self, request, *args, **kwargs):
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            username = registerForm.cleaned_data.get("username")
            isExists = User.objects.filter(username = username).exists()
            if not isExists:
                registerForm.save()
                return redirect(reverse("ContextView:Login"))
            else :
                return HttpResponse("用户名已存在")
        else :
            print(registerForm.get_json_data())
            return HttpResponse("注册失败")



def videoIndex(request):
    return render(request, "login_service_video_index.html")

def bookIndex(request):
    return render(request, "login_service_book_index.html")

from django.template.context_processors import debug, request
from django.contrib.auth.context_processors import auth


def debugIndex(request):
    users = User.objects.all()
    for user in users:
        print(user)
    return render(request, "debug_service.html")


# from django.contrib.messages.context_processors import messages
from django.contrib import messages
from django.contrib.messages.api import get_messages
from django.contrib.messages import DEFAULT_TAGS, DEFAULT_LEVELS

def messageIndex(request):

    messages.set_level(request, 10)

    messages.info(request, "InfoMessage")
    messages.debug(request, "DebugMessage")
    messages.warning(request, "WarningMessage")
    messages.success(request, "SuccessMessage")
    messages.error(request, "ErrorMessage")

    messageList = get_messages(request)
    
    for mes in messageList:
        print(mes.__dict__)

    print(DEFAULT_TAGS)
    print(DEFAULT_LEVELS)
    return render(request, "messge_service.html")