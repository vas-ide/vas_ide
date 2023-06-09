from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView

week_days_dict = {
    "monday": "Погулять с ребенком.",
    "tuesday": "Погулять с ребенком.",
    "wednesday": "Погулять с ребенком.",
    "thursday": "Погулять с ребенком.",
    "friday": "Погулять с ребенком.",
    "saturday": "Погулять с ребенком.",
    "sunday": "Погулять с ребенком.",
}


def get_info_about_day(request, day_week: str):
    description = week_days_dict.get(day_week)
    if description:
        return render(request, "week_days/greeting.html", {})
    else:
        return HttpResponseNotFound(f"Неизвестный адрес")


def get_info_about_day_by_number(request, day_week: int):
    if day_week > len(week_days_dict):
        return HttpResponseNotFound(f"В неделе всего 7 дней. Вы указали неправильный день - {day_week}")
    redirect_url = reverse("day-name", args=[list(week_days_dict)[day_week - 1]], )
    return HttpResponseRedirect(redirect_url)


def kianu_reeves(request):
    data = {
        "year_born": 1964,
        "city_born": "Beirut",
        "movie_name": "Point Break",
    }
    return render(request, "week_days/keanu_reeves.html", context=data)

def guinnes_world_records(request):
    data = {
        "power_man": "Narve Laeret",
        "bar_name": "Bob's BBQ & Grill",
        "count_needle": 1790,
    }
    return render(request, "week_days/guinnesswoldrecords.html", context=data)

