# Generated by Django 2.2.3 on 2019-07-17 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0026_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=250, null=True),
        ),
    ]