from django.shortcuts import render
from django.views import *
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


import math


def rectangle(request, width: int, height: int):
    return HttpResponse(f"Площадь прямоугольника размером {width}x{height} равна {width * height}")


def square(request, width: int):
    return HttpResponse(f"Площадь квадрата размером {width}x{width} равна {width * width}")


def circle(request, radius: int):
    return HttpResponse(f"Площадь круга радиус {radius} равна {round((radius ** 2) * math.pi, 3)}")


def get_rectangle_area(request, width: int, height: int):
    # redirect_url = reverse("rectangle-name", args=(width, height,))
    # return HttpResponseRedirect(redirect_url)
    return render(request, "geometry/rectangle.html", {})


def get_square_area(request, width: int):
    # redirect_url = reverse("square-name", args=(width,))
    # return HttpResponseRedirect(redirect_url)
    return render(request, "geometry/square.html", {})

def get_circle_area(request, radius: int):
    # redirect_url = reverse("circle-name", args=(radius,))
    # return HttpResponseRedirect(redirect_url)
    return render(request, "geometry/circle.html", {})
