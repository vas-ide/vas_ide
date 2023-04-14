
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView




def get_info_about_day(request, day_week):
    if day_week == "monday":
        return HttpResponse("Сделать КТ, Погулять с ребенком.")
    elif day_week == "tuesday":
        return HttpResponse("Узнать результаты КТ, Поехать в Ростов.")
    else:
        return HttpResponseNotFound(f"Неизвестный адрес")
