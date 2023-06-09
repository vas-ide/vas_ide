# Generated by Django 4.1.7 on 2023-05-19 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0021_actor_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]
