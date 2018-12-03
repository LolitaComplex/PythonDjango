from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def student(request):
    student = Student(name = "龙宫礼奈", age = 150,
         specialty = "柴刀妹", score = 10)
    student.save()

    return HttpResponse("啦啦")

def getStudent(request):
    # student = Student.objects.get(pk = 1)
    student = Student.objects.filter(name="龙宫礼奈")
    print(student)

    # student.delete()
    return HttpResponse("")    