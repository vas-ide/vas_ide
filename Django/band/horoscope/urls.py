from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="horoscope-index"),
    path("type", views.type_zodiac),
    path("type/<str:type_zodiac>", views.zodiac_elements_type, name="zodiac_type"),
    path("<int:sign_zodiac>", views.get_info_about_sign_zodiac_by_number),
    path("<str:sign_zodiac>", views.get_info_about_sign_zodiac, name="horoscope-name"),
]
