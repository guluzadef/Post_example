# Generated by Django 2.2.3 on 2019-07-17 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0027_auto_20190717_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
