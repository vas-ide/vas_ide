from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class Director(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, default="unknown")
    director_email = models.EmailField(blank=True, default="vas-atc@yandex.ru")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Actor(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, default="unknown")
    actor_email = models.EmailField(blank=True, default="vas-atc@yandex.ru")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

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
    year = models.IntegerField(null=True, blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    budget = models.IntegerField(default='0', blank=True, validators=[MinValueValidator(1)])
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default=USD)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, blank=True)
    actor = models.ForeignKey(Actor, on_delete=models.PROTECT, null=True, blank=True)
    # on_delete=models.PROTECT
    # on_delete=models.CASCADE
    # on_delete=models.SET_NULL


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one-movie', args=[self.slug])

    def __str__(self):
        return f"{self.name}-{self.year}-{self.rating}"

# from movie_app.models import Movie
