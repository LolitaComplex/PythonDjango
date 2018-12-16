# Generated by Django 2.1.3 on 2018-12-16 06:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator(message='邮箱格式有误')])),
                ('password', models.CharField(max_length=15, validators=[django.core.validators.MaxLengthValidator(limit_value=15, message='密码长度最大为15个字符'), django.core.validators.MinLengthValidator(limit_value=7, message='密码长度最小为7个字符')])),
                ('telphone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='请输入正确手机号', regex='^1[35678]\\d{9}$')])),
                ('nickname', models.CharField(max_length=10, null=True)),
                ('money', models.IntegerField(default=1000)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
