from django.http import HttpResponse
from .models import Student, Teacher, Score, Course
from django.db import transaction

def index(request):
    return HttpResponse("Index")


@transaction.atomic
def createData(request):
    """ 增加数据，调用一次 """
    Student.objects.bulk_create([
        Student(name = "希特勒", gender = 0),
        Student(name = "丘吉尔", gender = 0),
        Student(name = "张伯伦", gender = 0),
        Student(name = "罗斯福", gender = 0),
        Student(name = "奥黛丽赫本", gender = 1),
        Student(name = "玛莲娜梦露", gender = 1)
    ])

    Teacher.objects.bulk_create([
        Teacher(name = "语文老师"), # 0
        Teacher(name = "英语老师"), # 1
        Teacher(name = "数学老师"), # 2
        Teacher(name = "物理老师"), # 3
        Teacher(name = "化学老师"), # 4
        Teacher(name = "生物老师"), # 5
        Teacher(name = "历史老师"), # 6
        Teacher(name = "政治老师"), # 7
        Teacher(name = "地理老师"), # 8
        Teacher(name = "体育老师")  # 9
    ])

    Course.objects.bulk_create(__initCourseList())
    return HttpResponse("CreateData")


def __initSportTeacher(courseList, teacherList):
    """ 体育老师所有科目授课 """
    for teacher in teacherList:
        courseList.append(Course(name = teacher.name[0: 2], teacher = teacher))

def __initCourseList():
    teacherList = list(Teacher.objects.all())
    courseList = []
    for index in range(len(teacherList)):
        teacher = teacherList[index]
        if(index == 0):
            courseList.append(Course(name = "物理", teacher = teacher))
        elif(index == 3):
            courseList.append(Course(name = "生物", teacher = teacher))
        elif(index == 5):
            courseList.append(Course(name = "语文", teacher = teacher))
        elif(index == 7):
            courseList.append(Course(name = "英语", teacher = teacher))
        elif(index == 9):
            __initSportTeacher(courseList, teacherList)
            continue
        courseList.append(Course(name = teacher.name[0: 2], teacher = teacher))
    return courseList


