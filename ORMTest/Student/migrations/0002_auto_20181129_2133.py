# Generated by Django 2.1.3 on 2018-11-29 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
