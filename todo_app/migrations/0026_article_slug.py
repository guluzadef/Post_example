# Generated by Django 2.2.3 on 2019-07-17 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0025_auto_20190717_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
    ]
