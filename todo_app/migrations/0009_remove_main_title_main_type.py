# Generated by Django 2.2.3 on 2019-07-15 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0008_main_title_main_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main_title',
            name='main_type',
        ),
    ]