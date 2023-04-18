from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic import TemplateView

week_days_dict = {
    "monday": "Погулять с ребенком.",
    "tuesday": "Погулять с ребенком.",
}


def get_info_about_day(request, day_week: str):
    description = week_days_dict.get(day_week)
    if description:
        return HttpResponse(f"{day_week.capitalize()} - {description}")
    else:
        return HttpResponseNotFound(f"Неизвестный адрес")


def get_info_about_day_by_number(request, day_week: int):
    description = day_week
    if 0 < description < 8:
        return HttpResponse(f"Tooday is {description} week day!")
    else:
        return HttpResponseNotFound(f"В неделе всего 7 дней. Вы указали неправильный день - {day_week}")
