


from django.contrib import admin
from django.urls import path, include
from horoscope import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/aries', views.aries),
    path('horoscope/taurus', views.taurus),
    path('horoscope/gemini', views.gemini),
    path('horoscope/cancer', views.cancer),
    path('horoscope/leo', views.leo),
    path('horoscope/virgo', views.virgo),
    path('horoscope/libra', views.libra),
    path('horoscope/scorpio', views.scorpio),
    path('horoscope/sagittarius', views.sagittarius),
    path('horoscope/capricorn', views.capricorn),
    path('horoscope/aquarius', views.aquarius),
    path('horoscope/pisces', views.pisces),


]
