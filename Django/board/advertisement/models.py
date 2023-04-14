from django.db import models



class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.CharField(max_length=2000, default="", verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    price = models.FloatField(verbose_name="Цена", default=0)
    views_count = models.IntegerField(verbose_name="Колличество просмотров", default=0)


    def __str__(self):
        return f"Название:{self.title}    Описание:{self.description}"




