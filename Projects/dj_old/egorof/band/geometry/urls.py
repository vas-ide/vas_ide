from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('get_rectangle_area/<int:width>/<int:height>', views.get_rectangle_area),
    path('get_square_area/<int:width>', views.get_square_area),
    path('get_circle_area/<int:radius>', views.get_circle_area),
    path('rectangle/<int:width>/<int:height>', views.rectangle, name="rectangle-name"),
    path('square/<int:width>', views.square, name="square-name"),
    path('circle/<int:radius>', views.circle, name="circle-name"),
]
