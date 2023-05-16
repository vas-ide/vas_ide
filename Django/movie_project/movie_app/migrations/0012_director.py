# Generated by Django 4.1.7 on 2023-05-16 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0011_movie_director_alter_movie_budget_alter_movie_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('second_name', models.CharField(default='unknown', max_length=50)),
                ('director_email', models.EmailField(blank=True, default='vas-atc@yandex.ru', max_length=254)),
            ],
        ),
    ]
