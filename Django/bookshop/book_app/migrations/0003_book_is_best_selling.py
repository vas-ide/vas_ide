# Generated by Django 4.1.7 on 2023-05-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0002_book_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
