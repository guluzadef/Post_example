# Generated by Django 2.2.3 on 2019-07-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0007_auto_20190715_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_title',
            name='main_type',
            field=models.IntegerField(choices=[(1, 'Ana sehife'), (2, 'About'), (3, 'Contact')], default=1),
        ),
    ]