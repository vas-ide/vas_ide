from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField()

    def __str__(self):
        return f"{self.name}-{self.rating}%"










