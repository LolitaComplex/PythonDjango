# Generated by Django 2.1.3 on 2018-11-29 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=10)),
                ('specialty', models.CharField(max_length=50)),
                ('score', models.IntegerField(default=0, max_length=3)),
            ],
        ),
    ]
