# Generated by Django 2.2.3 on 2019-07-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0013_contact_me'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='txt',
            name='bytext',
        ),
        migrations.AlterField(
            model_name='contact_me',
            name='img',
            field=models.ImageField(upload_to='contact_photo'),
        ),
    ]
