from django.contrib import admin
from .models import Movie


# class MovieAdmin(admin.ModelAdmin):
#     list_display = ["name", "year", "rating"]
# admin.site.register(Movie, MovieAdmin)
# or
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ["name", "year", "rating"]
    list_editable = ["year", "rating"]
    ordering = ["year", "-rating"]
    list_per_page = 5