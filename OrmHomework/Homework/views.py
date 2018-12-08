from django.http import HttpResponse
from .models import Student, Teacher, Score, Course
from django.db import transaction, connection
from django.db.models import Avg, Count, Sum, F, Q, Max, Min
import random

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
    __initScoreList()
    return HttpResponse("CreateData")


def __initSportTeacher(courseList, teacherList, teacherSport):
    """ 体育老师所有科目授课 """
    for teacher in teacherList:
        courseList.append(Course(name = teacher.name[0: 2], teacher = teacherSport))

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
            __initSportTeacher(courseList, teacherList, teacherSport = teacher)
            continue
        courseList.append(Course(name = teacher.name[0: 2], teacher = teacher))
    return courseList


def __initScoreList():
    courseSet = Course.objects.all()
    studentSet = Student.objects.all()

    courseLen, studentLen = (len(courseSet), len(studentSet))
    for index in range(50):
        scoreNum = random.randint(1, 150)
        course = courseSet[random.randint(0, courseLen - 1)]
        student = studentSet[random.randint(0, studentLen - 1)]
        print("%s -- %s : %d" % (student.name, course.name, scoreNum))
        exists = Score.objects.filter(course_id = course.id, student_id = student.id).exists()
        if(not exists):
            score = Score(student = student, course = course, number = scoreNum)
            score.save()



def question1(request):
    students = Student.objects  \
        .annotate(scoreAvg = Avg("score__number"))  \
        .filter(scoreAvg__gt = 60)

    for student in students:
        print("%s : %d" % (student.name, student.scoreAvg))

    __printSql()
    return HttpResponse("查询平均成绩大于60分的同学id和平均成绩")


def question2(request):
    students = Student.objects  \
        .annotate(courseCount = Count("score__course_id"), scoreSum = Sum("score__number")) \
        .defer("gender")

    for student in students:
        print(student.__dict__)

    __printSql()
    return HttpResponse("查询所有同学id、姓名、选课的数、总成绩")


def question3(request):
    teachers = Teacher.objects.filter(name__startswith = "数学")
    for teacher in teachers:
        print("%d : %s" % (teacher.id, teacher.name))

    __printSql()
    return HttpResponse("查询性数学老师的个数")


def question4(rquest):
    students = Student.objects  \
        .exclude(score__course__teacher__name__startswith = "数学") \
        .defer("gender")
    for student in students:
        print(student.__dict__)


    __printSql()
    return HttpResponse("查询没学习过数学老师课的同学的id、姓名")


def question5(request):
    students = Student.objects  \
        .filter(score__course_id__in = (1, 2)) \
        .defer("gender").distinct()
    for student in students:
        print("%d : %s" % (student.id, student.name))

    __printSql()
    return HttpResponse("查询学过id为1和2的所有同学的学号、姓名")

def question6(request):
    students = Student.objects  \
        .filter(score__course__teacher__name = "历史老师")\
        .defer("gender")
    for student in students:
        print("%d : %s" % (student.id, student.name))

    __printSql()
    return HttpResponse("查询学过历史老师所教的所有课的同学的学号、姓名")

def question7(reuqest):
    studnets = Student.objects  \
        .exclude(score__number__gte = 120) \
        .defer("gender").distinct()
    for student in studnets:
        print("%d : %s" % (student.id, student.name))

    __printSql()
    return HttpResponse("查询所有课程成绩均小于120分的同学的id和姓名")


def question8(reuqest):
    # students = Student.objects.annotate(courseName = F("score__course__name")) \
    #     .defer("gender").annotate(count = Count("courseName"))
        
    # finishStudent = {}
    # for student in students:
    #     count = finishStudent.get(student.name, 0)
    #     finishStudent[student.name] = count + 1
    # print(finishStudent)

    # Sql函数有distinct属性
    students = Student.objects  \
        .annotate(count = Count("score__course__name", distinct = True))   \
        .defer("gender")

    for student in students:
        print("%s : %d" % (student.name, student.count))

    __printSql()
    return HttpResponse("查询没有完全所有课的同学的id，姓名（完全课代表 语数英物化生历地政 全部有上）")


def question9(request):
    students = Student.objects  \
        .annotate(scoreAvg = Avg("score__number")) \
        .order_by("-scoreAvg")
    for student in students:
        print("%s : %d" % (student.name, student.scoreAvg))

    __printSql()
    return HttpResponse("查询所有学生的姓名、平均分，并且按照平均分从高到低排序")


def question10(request):
    courses = Course.objects    \
        .annotate(maxScore = Max("score__number"), minScore = Min("score__number"), teacherName = F("teacher__name"))   \
        .defer("teacher_id")

    for course in courses:
        print("%s, %s, %s, %s, %s" % (course.id, course.name, course.teacherName, course.maxScore, course.minScore))

    __printSql()
    return HttpResponse("查询各科升级的最高分和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分")


def question11(request):
    courses = Course.objects    \
        .annotate(scoreAvg = Avg("score__number"), teacherName = F("teacher__name"))    \
        .defer("teacher_id").filter(scoreAvg__isnull = False).order_by("scoreAvg")

    for course in courses:
        print("%s, %s, %s, %s" % (course.id, course.name, course.teacherName, course.scoreAvg))
    
    __printSql()
    return HttpResponse("查询每门课程的平均成绩，按照平均成绩进行排序")


def question12(request):
    students = Student.objects  \
        .aggregate(maleNum = Count("gender", filter = Q(gender = 0)), famaleNum = Count("gender", filter = Q(gender = 1)))
    
    print(students)

    __printSql()
    return HttpResponse("统计有多少女生，多少男生")


def question13(request):
    scores = Score.objects \
        .filter(course__teacher__name = "英语老师") \
        .annotate(teacherName = F("course__teacher__name"), courseName = F("course__name"), studentName = F("student__name")) \
        .defer("course_id", "student_id")   \
        # .update(number = F("number") + 10)

    for score in scores:
        print("%s, %s, %s : %d" % (score.studentName, score.courseName, score.teacherName, score.number))

    __printSql()
    return HttpResponse("将英语老师的每一门课程都在原来的基础上加5分")


def question14(reuqest):
    students = Student.objects \
        .annotate(badCount = Count("id", filter = Q(score__number__lte = 90)))   \
        .filter(badCount__gte = 2) \
        .defer("gender")

    for student in students:
        print("%s, %s, %d" % (student.id, student.name, student.badCount))

    __printSql()
    return HttpResponse("查询两门以上不及格的同学的id、姓名、以及不及格课程数")


def question15(reuqest):
    courses = Course.objects  \
        .annotate(personNum = Count("score__student_id"), teacherName = F("teacher__name"))   \
        .defer("teacher_id")

    for course in courses:
        print("%s, %s, %s授课 , 选课人数：%d" % (course.id, course.name, course.teacherName, course.personNum))

    __printSql()
    return HttpResponse("查询每门课的选课人数")


def __printSql():
    print("运行的全部Sql语句：")
    for sql in connection.queries:
        print(sql)


