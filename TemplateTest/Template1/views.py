from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
# JavaMills：1543132231697

class Person:
    def __init__(self, name):
        self.personName = name

def index(request, articalId = 1):
    context = {
        "time": datetime.now(),
        "age": 123,
        "username": "Doing",
        "person": Person("龙宫礼奈"),
        "dict": {
            "key": "Value"
        },
        "list":["纳兹", "爆衣"]
    }

    return render(request, "index.html", context = context)