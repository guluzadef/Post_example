# Generated by Django 2.2.3 on 2019-07-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0032_auto_20190725_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='about',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
