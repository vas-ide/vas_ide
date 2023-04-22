from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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

zodiac_type = {
    "fire": ["aries", "leo", "sagittarius"],
    "earth": ["taurus", "virgo", "capricorn"],
    "air": ["gemini", "libra", "aquarius"],
    "water": ["cancer", "scorpio", "pisces"],
}


def index(request):
    zodiacs = list(zodiac_dict)
    li_elements = ""
    for sign in zodiacs:
        redirect_url = reverse("horoscope-name", args=(sign,))
        li_elements += f"<li><a href='{redirect_url}'>{sign.title()}</a></li>"
    result = f"""
    <ol>
    {li_elements}
    </ol>
    """
    return HttpResponse(result)


def type_zodiac(request):
    zodiacs_type = list(zodiac_type)
    li_elements = ""
    for element in zodiacs_type:
        redirect_url = reverse("zodiac_type", args=(element,))
        li_elements += f"<li><a href='{redirect_url}'>{element.title()}</a></li>"
    result = f"""
    <ol>
    {li_elements}
    </ol>
    """
    return HttpResponse(result)


def zodiac_elements_type(request, type_zodiac: str):
    li_elements = ""
    for element in zodiac_type[f"{type_zodiac}"]:
        redirect_url = reverse("horoscope-name", args=(element,))
        li_elements += f"<li><a href='{redirect_url}'>{element.title()}</a></li>"
    result = f"""
    <ul>
    {li_elements}
    </ul>
    """

    return HttpResponse(f"{result}")


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    if description:
        return HttpResponse(f"{description}")
    else:
        return HttpResponseNotFound(f"Неизвестный знак зодиака {sign_zodiac}")


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    if sign_zodiac > len(zodiac_dict):
        return HttpResponseNotFound(f"Неизвестный номер знака зодиака {sign_zodiac}")
    sign = list(zodiac_dict.keys())[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(sign,))
    return HttpResponseRedirect(redirect_url)
