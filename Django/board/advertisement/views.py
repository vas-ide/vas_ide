import random
from urllib import request

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import generic
from advertisement.models import Advertisement


class Index(View):
    def __init__(self):
        self.context = {
            "regions": [
                "Краснодарский Край",
                "Краснодар",
                "Ростовская Область",
                "Ростов-на-Дону",
                "Волгоградская Область",
                "Волгоград",
                "Ставропольский Край",
                "Ставрополь",
            ],
            "category": [
                "Ветеринарные услуги",
                "Гостиница для домашних животных",
                "Строительные работы",
                "Грузовые перевозки",
                "Пассажирские перевозки",
                "Туристические прогулки",
                "Жилые помещения посуточно",
                "Жилые помещения на длительное время",
            ],
            "advertisements": Advertisement.objects.all(),
        }

    def get(self, request):
        ip = request.META.get("REMOTE_ADDR")
        advertisements = Advertisement.objects.all()
        return render(request, "index.html", context=self.context)

class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = "advertisement/advertisement_in_processing"
    context_object_name = "advertisement_list"
    queryset = Advertisement.objects.all()[:10]



class AdvertisementPage(View):
    def __init__(self):
        self.advertisements = Advertisement.objects.all()
        self.random_advertisement = random.choice(self.advertisements)
        self.context = {
            "title": "Advertisement's",
            "name": "Advertisement-board",
            "header_text": "Это первая страница не тестовом проекте board в тестовом приложении advertisement так-же "
                           "тут идут смешанные пробы Petdoctor в малом колличестве. Это стартовый макет первой версии",
            # "ip": request.META.get("REMOTE_ADDR"),
            "post": f"Запрос на создание успешной записи обрабатывается !",
            "random_adv": self.random_advertisement
        }

    def get(self, request):

        # for i in range(500):
        #     new_adv = Advertisement(title=f"title{i}")
        #     new_adv.save()
        #
        # for i in Advertisement.objects.all():
        #     for j in range(500):
        #         search = Advertisement(title=f"title{j}")
        #         if i.title == search.title:
        #             print(search)
        #             search_id = i.id
        #             Advertisement.objects.get(id=search_id).delete()
        #     # Advertisement.objects.all().delete()
        #
        if request.method == "GET":
            return render(request, "advertisement/advertisement.html", context=self.context)
        elif request.method == "POST":
            return HttpResponseRedirect("/advertisement_in_processing")


def advertisement_in_processing(request):
    return render(request, "advertisement/advertisement_in_processing.html")


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



