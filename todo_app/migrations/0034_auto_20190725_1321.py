# Generated by Django 2.2.3 on 2019-07-25 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0033_auto_20190725_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profil',
            old_name='fullname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='profil',
            name='surname',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
    ]
