from django.db import models

class Student(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100, null = False)
    age = models.IntegerField(default = 0, null = False)
    specialty = models.CharField(max_length = 50, null = False)
    score = models.IntegerField(default = 0, null = False)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return "Student：{{name:{name}, age:{age}, specialty:{specialty}, score:{score} }}" \
             .format(name=self.name, age = self.age, specialty = self.specialty, score = self.score)

    class Meta:
        db_table = "orm_student"
        ordering = ["-age", "-id"]