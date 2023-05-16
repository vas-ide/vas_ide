from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ["name", "year", "rating"]
# admin.site.register(Movie, MovieAdmin)
# or
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "budget", "currency", "rating",   "rating_status"]
    list_editable = ["year", "currency", "rating"]
    ordering = ["year", "-rating"]
    list_per_page = 15
    actions = ["set_dollars", "set_euro"]

    @admin.display(ordering='rating', description='Оценка')
    def rating_status(self, movie: Movie):
        if movie.rating <= 50:
            return f"Fail."
        elif movie.rating <= 70:
            return f"One time film"
        elif movie.rating <= 85:
            return f"Good film"
        return f"Best content"


    @admin.action(description='Установить валюту в долларах')
    def set_dollars(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.USD)
        self.message_user(
            request,
            f"Было обновлено {count_updated} записей."
        )
    @admin.action(description='Установить валюту в евро')
    def set_euro(self, request, qs: QuerySet):
        count_updated = qs.update(currency=Movie.EUR)
        self.message_user(
            request,
            f"Было обновлено {count_updated} записей.",
            messages.ERROR
        )

