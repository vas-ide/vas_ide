from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('kianu', views.kianu_reeves),
    path('<int:day_week>', views.get_info_about_day_by_number),
    path('<str:day_week>', views.get_info_about_day, name="day-name"),
]
