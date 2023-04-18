from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("<int:sign_zodiac>/", views.get_info_about_sign_zodiac_by_number),
    path("<str:sign_zodiac>/", views.get_info_about_sign_zodiac),
    # path('aries/', views.aries),
    # path('taurus/', views.taurus),
    # path('gemini/', views.gemini),
    # path('cancer/', views.cancer),
    # path('leo/', views.leo),
    # path('virgo/', views.virgo),
    # path('libra/', views.libra),
    # path('scorpio/', views.scorpio),
    # path('sagittarius/', views.sagittarius),
    # path('capricorn/', views.capricorn),
    # path('aquarius/', views.aquarius),
    # path('pisces/', views.pisces),
]
