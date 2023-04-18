from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView

week_days_dict = {
    "monday": "Сделать КТ, Погулять с ребенком.",
    "tuesday": "Узнать результаты КТ, Поехать в Ростов.",
}


def get_info_about_day(request, day_week: str):
    description = week_days_dict.get(day_week)
    if description:
        return HttpResponse(f"{description}")
    else:
        return HttpResponseNotFound(f"Неизвестный адрес")


def get_info_about_day_by_number(request, day_week: int):
    if day_week:
        return HttpResponse(f"Tooday is {day_week} week day!")
    else:
        return HttpResponseNotFound(f"Неизвестный адрес")
