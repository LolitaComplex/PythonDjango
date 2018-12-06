# Generated by Django 2.1.3 on 2018-12-05 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommonAggregate', '0005_book_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='CommonAggregate.Author'),
        ),
    ]
