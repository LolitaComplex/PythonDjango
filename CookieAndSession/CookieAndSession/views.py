from django.shortcuts import render
from django.views.generic.base import View
from django.utils.timezone import make_aware
from datetime import datetime


class CookieView(View):

    def get(self, request, *args, **kwargs):
        response = render(request, "cookie_index.html")
        expires = datetime(year = 2018, month = 12, day = 13,   \
             hour = 22, minute = 0, second = 0)
        expires = make_aware(expires)

        response.set_cookie(key = "gender", value = 1, max_age = 1000, \
            expires = expires, path = "/cms/", domain = "", secure = False, \
            httponly = False)

        cookies = request.COOKIES
        username = cookies.get("key")

        response.delete_cookie("username")
        return response


class SessionView(View):

    def get(self, request, *args, **kwargs):
        response = render(request, "session_index.html")
        # request.session["name"] = "first_session"
        name = request.session.get("name") # 获取
        # name = request.session.pop("name") # 删除
        request.session.keys() # Dict(key)
        request.session.items() # Dict(item)
        request.session.clear() # 清空，数据库字段不会清除，而是置空
        request.session.flush() # 清空，数据库数据会被删除
        request.session.set_expiry(0) # 设置过期时间
        return response