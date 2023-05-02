# Generated by Django 4.1.7 on 2023-05-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='budget',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='movie',
            name='year',
            field=models.IntegerField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.IntegerField(max_length=3),
        ),
    ]