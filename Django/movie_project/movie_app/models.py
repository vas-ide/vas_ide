from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    rating = models.IntegerField()
    budget = models.IntegerField(default="0")

    def __str__(self):
        return f"{self.name}-{self.year}-{self.rating}"


# from movie_app.models import Movie





