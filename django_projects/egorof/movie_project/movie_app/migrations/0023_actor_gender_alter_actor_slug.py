# Generated by Django 4.1.7 on 2023-05-19 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0022_alter_director_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужчина'), ('F', 'Женщина')], max_length=1),
        ),
        migrations.AlterField(
            model_name='actor',
            name='slug',
            field=models.SlugField(max_length=255, unique=True, verbose_name='URL'),
        ),
    ]