from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('<day_week>/', views.get_info_about_day),
]
