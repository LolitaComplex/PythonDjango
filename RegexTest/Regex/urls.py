from django.urls import path, re_path, converters
from . import views

# r开头的字符串是原生字符串，特点是转义的反斜杠没效果。推荐正则前使用

class CategoryConverter(object):
    regex = '[^\+]{1}.+[^\+]{1}'

    def to_python(self, value):
        return value.split("+")

    def to_url(self, value):
        if isinstance(value, list):
            return "+".join(value)
        return str(value)


converters.register_converter(CategoryConverter, "cate")


urlpatterns = [
    re_path(r"^login/(?P<year>\d{4})/$", views.getContentPage),
    path("article/<cate:categories>/", views.getArticleCategory, name="article")
]