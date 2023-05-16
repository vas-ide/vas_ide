from django.contrib import admin
from .models import Movie


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ["name", "year", "rating"]
# admin.site.register(Movie, MovieAdmin)
# or
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "budget", "currency", "rating",   "rating_status"]
    list_editable = ["year", "currency", "rating"]
    ordering = ["year", "-rating"]
    list_per_page = 5

    @admin.display(ordering='rating', description='Оценка')
    def rating_status(self, movie: Movie):
        if movie.rating <= 50:
            return f"Fail."
        elif movie.rating <= 70:
            return f"One time film"
        elif movie.rating <= 85:
            return f"Good film"
        return f"Best content"
