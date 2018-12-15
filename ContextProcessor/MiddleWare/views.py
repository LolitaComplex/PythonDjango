from django.shortcuts import render
from django.middleware.common import CommonMiddleware
from django.middleware.gzip import GZipMiddleware
from django.middleware.cache import UpdateCacheMiddleware, FetchFromCacheMiddleware

# Create your views here.
def index(request):
    inner = InnerTest()
    inner()
    inner()
    inner().print("Test")
    inner.print("Test")

    return render(request, "middleware_index.html")


class InnerTest():

    def __init__(self):
        print("__init__")

    def __call__(self):
        print("__call__")
        return self

    def print(self, params):
        print(params)