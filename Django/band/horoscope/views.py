from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import TemplateView

# class Leo(View):
#     def get(self, request):
#         ip = request.META.get("REMOTE_ADDR")
#         return render(request, "leo.html", {})

zodiac_dict = {
    "aries": "Aries - Овен - первый знак зодиака, планета Марс(с 21 марта по 20 апреля)",
    "taurus": "Taurus - Телец - второй знак зодиака, планета Венера(с 21 апреля по 21 мая)",
    "gemini": "Gemini - Близнецы - третий знак зодиака, планета Меркурий(с 22 мая по 21 июня)",
    "cancer": "Canser - Рак - четвертый знак зодиака, Луна(с 22 июня по 22 июля)",
    "leo": "Leo - Лев - пятый знак зодиака, Солнце(с 22 июля по 21 августа)",
    "virgo": "Virgo - Дева - шестой знак зодиака, планета Меркурий(с 22 августа по 23 сентября)",
    "libra": "Libra - Весы - седьмой знак зодиака, планета Венера(с 24 сентября по 23 октября)",
    "scorpio": "Scorpio - Скорпион - восьмой знак зодиака, планета Марс(с 24 октября по 22 ноября)",
    "sagittarius": "Sagittarius - Стрелец - девятый знак зодиака, планета Юпитер(с 23 ноября по 22 декабря)",
    "capricorn": "Capricorn - Козерог - десятый знак зодиака, планета Сатурн(с 23 декабря по 20 января)",
    "aquarius": "Aquarius - Водолей - Одиннадцатый знак Зодиака, планеты Уран и Сатурн(с 21 января по 19 февраля)",
    "pisces": "Pisces - Рыбы - Двенадцатый знак зодиака, планета Юпитер(с 20 февраля по 20 марта)",
}


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(f"{description}")
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")



def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if 0 < sign_zodiac < 13:
        description = zodiac_dict.get(list(zodiac_dict.keys())[sign_zodiac - 1])
        return HttpResponseRedirect(f"/horoscope/{description}")
    else:
        return HttpResponseNotFound(f"Неизвестный номер знака зодиака {sign_zodiac}")
