from django.shortcuts import render
from django.views import *
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


import math


def rectangle(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")


def square(request, width: int):
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width * width}")


def circle(request, radius: int):
    return HttpResponse(f"Площадь круга радиус {radius} равна {round((radius ** 2) * math.pi, 3)}")


def get_rectangle_area(request, width: int, height: int):
    return HttpResponseRedirect(f"/calculate_geometry/rectangle/{width}/{height}")


def get_square_area(request, width: int):
    return HttpResponseRedirect(f"/calculate_geometry/square/{width}")


def get_circle_area(request, radius: int):
    return HttpResponseRedirect(f"/calculate_geometry/circle/{radius}")
