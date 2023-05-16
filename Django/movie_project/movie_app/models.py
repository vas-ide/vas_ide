from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
    EUR = "EUR"
    USD = "USD"
    RUB = "RUB"

    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (USD, 'Dollar-US'),
        (RUB, 'Rubles'),
    ]

    name = models.CharField(max_length=100)
    year = models.IntegerField(null=True, blank=True )
    rating = models.IntegerField()
    budget = models.IntegerField(default='0', blank=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    slug = models.SlugField(default='', null=False, db_index=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one-movie', args=[self.slug])

    def __str__(self):
        return f"{self.name}-{self.year}-{self.rating}"

# from movie_app.models import Movie
