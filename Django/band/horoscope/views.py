
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView





# class Leo(View):
#     def get(self, request):
#         ip = request.META.get("REMOTE_ADDR")
#         return render(request, "leo.html", {})
def aries(request):
    return HttpResponse("Aries - Овен - первый знак зодиака, планета Марс(с 21 марта по 20 апреля)")
def taurus(request):
    return HttpResponse("Taurus - Телец - второй знак зодиака, планета Венера(с 21 апреля по 21 мая)")
def gemini(request):
    return HttpResponse("Gemini - Близнецы - третий знак зодиака, планета Меркурий(с 22 мая по 21 июня)")
def cancer(request):
    return HttpResponse("Canser - Рак - четвертый знак зодиака, Луна(с 22 июня по 22 июля)")
def leo(request):
    return HttpResponse("Leo - Лев - пятый знак зодиака, Солнце(с 22 июля по 21 августа)")
def virgo(request):
    return HttpResponse("Virgo - Дева - шестой знак зодиака, планета Меркурий(с 22 августа по 23 сентября)")
def libra(request):
    return HttpResponse("Libra - Весы - седьмой знак зодиака, планета Венера(с 24 сентября по 23 октября)")
def scorpio(request):
    return HttpResponse("Scorpio - Скорпион - восьмой знак зодиака, планета Марс(с 24 октября по 22 ноября)")
def sagittarius(request):
    return HttpResponse("Sagittarius - Стрелец - девятый знак зодиака, планета Юпитер(с 23 ноября по 22 декабря)")
def capricorn(request):
    return HttpResponse("Capricorn - Козерог - десятый знак зодиака, планета Сатурн(с 23 декабря по 20 января)")
def aquarius(request):
    return HttpResponse("Aquarius - Водолей - Одиннадцатый знак Зодиака, планеты Уран и Сатурн(с 21 января по 19 февраля)")
def pisces(request):
    return HttpResponse("Pisces - Рыбы - Двенадцатый знак зодиака, планета Юпитер(с 20 февраля по 20 марта)")


