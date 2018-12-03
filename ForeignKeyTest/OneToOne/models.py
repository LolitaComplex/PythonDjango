from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 50, null = False)

    class Meta:
        db_table = "student"

class Parent(models.Model):
    name = models.CharField(max_length = 50, null = False)
    student = models.OneToOneField("Student", on_delete = models.CASCADE, related_name = "parent")

    class Meta:
        db_table = "parent"
