# Generated by Django 2.2.3 on 2019-07-13 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0005_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='img',
            field=models.ImageField(default=True, upload_to='photos'),
            preserve_default=False,
        ),
    ]
