# Generated by Django 2.2.3 on 2019-07-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_main_txt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='txt',
            name='text',
        ),
        migrations.AddField(
            model_name='txt',
            name='texth1',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='txt',
            name='texth3',
            field=models.CharField(default=True, max_length=255),
            preserve_default=False,
        ),
    ]