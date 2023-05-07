from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True)
    rating = models.IntegerField()
    budget = models.IntegerField(default="0")
    slug = models.SlugField(default='', null=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one-movie', args=[self.slug ])

    def __str__(self):
        return f"{self.name}-{self.year}-{self.rating}"

# from movie_app.models import Movie
