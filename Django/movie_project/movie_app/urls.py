
from . import views
from django.urls import path

urlpatterns = [
    path("", views.show_all_movies, name="all-movies"),
    path("movie/<slug:slug_movie>", views.show_one_movie, name="one-movie"),
    # path("type", views.type_zodiac),
    # path("type/<str:type_zodiac>", views.zodiac_elements_type, name="zodiac_type"),
    # path("<int:sign_zodiac>", views.get_info_about_sign_zodiac_by_number),
    # path("<str:sign_zodiac>", views.get_info_about_sign_zodiac, name="horoscope-name"),
]
