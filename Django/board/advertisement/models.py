from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    description = models.CharField(max_length=2000, default="", verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    price = models.FloatField(verbose_name="Цена", default=0)
    views_count = models.IntegerField(verbose_name="Колличество просмотров", default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name="advertisement_status")
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name="advertisements_type")
    region = models.ManyToManyField("Region", default=None, related_name="advertisement_region")

    def __str__(self):
        return f"Название:{self.title}    Описание:{self.description}"

    class Meta:
        db_table = "advertisements"
        ordering = ["title"]


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название статуса")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "status"


class AdvertisementType(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип обьявления")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "type"


class Region(models.Model):
    name = models.CharField(max_length=150, verbose_name="Регион размещения обьявления ")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "region"


class Author(models.Model):
    nick_name = models.CharField(max_length=150, verbose_name="Псевдоним автора")
    name = models.CharField(max_length=150, blank=True, verbose_name="Имя")
    second_name = models.CharField(max_length=150, blank=True, verbose_name="Фамилия")
    email = models.EmailField(blank=True, verbose_name="Электронная почта")

    def __str__(self):
        return f"{self.nick_name}"

    class Meta:
        db_table = "authors"

class Classification(models.Model):
    name = models.CharField(max_length=150, verbose_name="Классификация (Рубрика объявления)")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "classifications"
