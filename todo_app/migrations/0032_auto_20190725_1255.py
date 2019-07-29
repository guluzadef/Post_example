# Generated by Django 2.2.3 on 2019-07-25 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0031_updatepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-id']},
        ),
    ]
