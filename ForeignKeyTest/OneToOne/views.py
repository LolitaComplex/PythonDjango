from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Parent

# Create your views here.

def oneToOne(request):
    student = Student(name = "漩涡博人")
    student.save()

    parent = Parent(name = "漩涡鸣人")
    parent.student = student
    parent.save()

    return HttpResponse("一对一")


def query(request):
    student = Student.objects.first()
    parent = Parent.objects.first()

    print(student.parent)
    print(parent.student)

    return HttpResponse("获取一对一")