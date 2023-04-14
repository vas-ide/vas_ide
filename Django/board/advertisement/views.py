from urllib import request

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView
from advertisement.models import Advertisement


class Index(View):

    def get(self, request):
        ip = request.META.get("REMOTE_ADDR")
        advertisements = Advertisement.objects.all()
        return render(request, "index.html", {"ip_address": ip, "advertisements": advertisements})


class AdvertisementPage(View):
    def get(self, request):
        title = "Доска обьявлений-ADVERTISMENT"
        name = "Тестовый сайт по шаблонам джанго"
        text = "Это первая страница не тестовом проекте board в тестовом приложении advertisement так-же тут " \
               " идут смешанные пробы Petdoctor в малом колличестве. Это стартовый макет первой версии"
        ip = request.META.get("REMOTE_ADDR")
        return render(request, "advertisement/advertisement.html",
                      {"title": title, "name": name, "text": text, "ip": ip})

    def post(self, request):
        tell = f"Запрос на создание успешной записи обрабатывается !"
        return render(request, "advertisement/advertisement_post.html", {"tell": tell})


# def advertisement(request, *args, **kwargs):
#     ip = request.META.get("REMOTE_ADDR")
#     advertisement = ["Delivery to clinic",
#                      "Опрос и первичный осмотр",
#                      "Диагностика и анализы",
#                      "Вмешательство или процедуры",
#                      "Вторичный анализ и осмотр",
#                      "Delivery from clinic to home"
#     ]
#     return render(request, "advertisement/advertisement.html", {"ip_address": ip, "advertisement": advertisement})

def skillbox_main(request, *args, **kwargs):
    return render(request, "advertisement/skillbox_main.html", {})


def python_main(request, *args, **kwargs):
    return render(request, "advertisement/python_main.html", {})


def pandas_main(request, *args, **kwargs):
    return render(request, "advertisement/pandas_main.html", {})


def django_main(request, *args, **kwargs):
    ip = request.META.get("REMOTE_ADDR")
    return render(request, "advertisement/django_main.html", {"ip_address": ip})


def git_main(request, *args, **kwargs):
    return render(request, "advertisement/git_main.html", {})


class Categories(TemplateView):
    template_name = "advertisement/categories.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Categories"
        context["name"] = "Categories"
        context["steps"] = "Standard diagnostic and treatment sheet"
        context["categories"] = [
            "Delivery to clinic", "Опрос и первичный осмотр", "Диагностика и анализы",
            "Вмешательство или процедуры", "Вторичный анализ и осмотр", "Delivery from clinic to home",
        ]
        return context


# def categories_us(request):
#     ip = request.META.get("REMOTE_ADDR")
#     categories = ["Delivery to clinic",
#                      "Опрос и первичный осмотр",
#                      "Диагностика и анализы",
#                      "Вмешательство или процедуры",
#                      "Вторичный анализ и осмотр",
#                      "Delivery from clinic to home"
#     ]
#     return render(request, "advertisement/categories.html", {"ip_address": ip, "categories": categories})


class About(TemplateView):
    template_name = "advertisement/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "About"
        context["name"] = "О Pet-Doctor."
        context["about"] = "Мы предоставляем большой спектр услуг в области ветеринарии. " \
                           "У нас работают опытные дипломированные специалисты которые проведут " \
                           "грамотную диагностику и окажут своевременоое лучение."
        return context


class Contacts(TemplateView):
    template_name = "advertisement/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Contacts"
        context["name"] = "Контактнаяя информация Pet-Doctor."
        context["doctors"] = ["VKA"]
        context["personal"] = ["VAS"]
        context["car"] = ["Largus", "Rapid"]
        context["phone"] = "+7-999-632-50-22"
        context["email"] = "vas-atc@yandex.ru"
        # context["ip"] = request.META.get("REMOTE_ADDR")
        # context["ip"] = request.META.get("HTTP_X_FORWARDED_FOR")
        return context


class Regions(View):

    def get(self, request):
        ip = request.META.get("REMOTE_ADDR")
        regions = [
            "Краснодарский Край",
            "Краснодар",
            "Ростовская Область",
            "Ростов-на-Дону"
            "Волгоградская Область",
            "Волгоград",
            "Ставропольский Край",
            "Ставрополь",
        ]
        return render(request, "advertisement/regions.html", {"ip_address": ip, "regions": regions})

    def post(self, request):
        print(f"Регион успешно создан")

# def regions_us(request):
#     ip = request.META.get("REMOTE_ADDR")
#     regions = [
#         "Краснодарский Край",
#         "Краснодар",
#         "Ростовская Область",
#         "Ростов-на-Дону"
#         "Волгоградская Область",
#         "Волгоград",
#         "Ставропольский Край",
#         "Ставрополь",
#     ]
#     return render(request, "advertisement/regions.html", {"ip_address": ip, "regions": regions})
