from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        labels = {
            "username": "用户名",
            "password": "密码",
            "nickname": "昵称"
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["nickname"]
        labels = {
            "username": "用户名",
            "password": "密码"
        }