from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ["name", "year", "rating"]
# admin.site.register(Movie, MovieAdmin)
# or

class RatingFilter(admin.SimpleListFilter):
    title = "Rating-filter"
    parameter_name = "Rating-settings"
    def lookups(self, request, model_admin):
        return [
            ("<40", "Low rating"),
            ("from 40 to 59", "Middle rating"),
            ("from 60 to 79", "Good rating"),
            (">=80", "The best film"),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == "<40":
            return queryset.filter(rating__lt=40)
        elif self.value() == "from 40 to 59":
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        elif self.value() == "from 60 to 79":
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        elif self.value() == ">=80":
            return queryset.filter(rating__gt=79)




@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "budget", "currency", "rating",   "rating_status"]
    list_editable = ["year", "currency", "rating"]
    ordering = ["year", "-rating"]
    list_per_page = 15
    actions = ["set_dollars", "set_euro"]
    search_fields = ["name__istartswith", "rating"]
    list_filter = ["name", "year", RatingFilter]

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



