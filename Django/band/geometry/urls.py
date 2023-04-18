from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('rectangle/<int:width>/<int:height>/', views.get_rectangle_area),
    path('square/<int:width>/', views.get_square_area),
    path('circle/<int:radius>/', views.get_circle_area),
]
