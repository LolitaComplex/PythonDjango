from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=15, validators=(MinLengthValidator(limit_value=7), ))
    telphone = models.CharField(max_length=11, validators=(RegexValidator(regex=r"^1[35678]\d{9}$"),))
    nickname = models.CharField(null=True, max_length=10)
    money = models.FloatField(default=1000)

    class Meta:
        db_table = "user"
