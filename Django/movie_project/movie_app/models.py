from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


class Director(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, default="unknown")
    director_email = models.EmailField(blank=True, default="vas-atc@yandex.ru")
    # slug = models.SlugField(default='', null=False, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.first_name), slugify(self.second_name), slugify(self.id)))
        super(Director, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one-director', args=[self.slug])

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class Actor(models.Model):
    MALE = "M"
    FEMALE = "F"

    GENDERS = [
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина'),
    ]
    first_name = models.CharField(max_length=50, blank=True)
    second_name = models.CharField(max_length=50, default="unknown")
    actor_email = models.EmailField(blank=True, default="vas-atc@yandex.ru")
    gender = models.CharField(max_length=1, choices=GENDERS, blank=True)
    # slug = models.SlugField(default='', null=False, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.first_name), slugify(self.second_name), slugify(self.id)))
        super(Actor, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('one-actor', args=[self.slug])

    def __str__(self):
        if self.gender == self.MALE:
            return f" Актёр: {self.first_name} {self.second_name}"
        elif self.gender == self.FEMALE:
            return f" Актриса: {self.first_name} {self.second_name}"


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
    actors = models.ManyToManyField(Actor)

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
