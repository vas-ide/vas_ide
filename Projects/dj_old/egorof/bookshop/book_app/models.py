from django.db import models



class Book(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=70)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()

    def __str__(self):
        return f"{self.title}-{self.rating}"


# from book_app.models import Book





