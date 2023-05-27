from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.CharField(max_length=2000, default="", verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
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
