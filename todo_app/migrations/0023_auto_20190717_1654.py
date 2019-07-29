# Generated by Django 2.2.3 on 2019-07-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0022_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default=True, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
