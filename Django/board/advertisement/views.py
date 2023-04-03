from urllib import request

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic import TemplateView


class Advertisement(TemplateView):
    template_name = "advertisement/advertisement.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["title"] = "Доска обьявлений-ADVERTISMENT"
        context["name"] = "Тестовый сайт по шаблонам джанго"
        context["text"] = "Это первая страница не тестовом проекте board в тестовом приложении advertisement так-же тут " \
                          " идут смешанные пробы Petdoctor в малом колличестве. Это стартовый макет первой версии"
        return context


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
            "Delivery to clinic",
            "Опрос и первичный осмотр",
            "Диагностика и анализы",
            "Вмешательство или процедуры",
            "Вторичный анализ и осмотр",
            "Delivery from clinic to home",
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


class About(View):
    def get(self, request):
        return render(request, "advertisement/about.html",  {})
# def about_us(request):
#     ip = request.META.get("REMOTE_ADDR")
#     return render(request, "advertisement/about.html", {"ip_address": ip})


def contact_us(request):
    ip = request.META.get("REMOTE_ADDR")
    chip = ["Intel", "AMD"]
    video_chip = ["Intel", "AMD", "Nvidia"]
    ssd = ["Samsung", "WD"]
    return render(request, "advertisement/contacts.html", {
        "ip_address": ip,
        "chip": chip, "video_chip": video_chip, "ssd": ssd
    })


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
        return render(request, "advertisement/regions.html",  {"ip_address": ip, "regions": regions})

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



