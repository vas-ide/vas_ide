# Generated by Django 4.1.7 on 2023-05-16 17:pillow_ticket

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0012_director'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
    ]
