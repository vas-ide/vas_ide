from django.shortcuts import render
from django.http import HttpResponse


# def get_user_ip(request):
#     # ip = request.META.get("REMOTE_ADDR")
#     return render(request, "advertisement/advertisement_list.html", {"ip_address": ip})


def advertisement_list(request, *args, **kwargs):
    ip = request.META.get("REMOTE_ADDR")
    advertisement = ["Delivery to clinic",
                     "Опрос и первичный осмотр",
                     "Диагностика и анализы",
                     "Вмешательство или процедуры",
                     "Вторичный анализ и осмотр",
                     "Delivery from clinic to home"
    ]
    return render(request, "advertisement/advertisement_list.html", {"ip_address": ip, "advertisement": advertisement})

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


def categories_us(request):
    ip = request.META.get("REMOTE_ADDR")
    categories = ["Delivery to clinic",
                     "Опрос и первичный осмотр",
                     "Диагностика и анализы",
                     "Вмешательство или процедуры",
                     "Вторичный анализ и осмотр",
                     "Delivery from clinic to home"
    ]
    return render(request, "advertisement/categories.html", {"ip_address": ip, "categories": categories})


def about_us(request):
    ip = request.META.get("REMOTE_ADDR")
    return render(request, "advertisement/about.html", {"ip_address": ip})


def contact_us(request):
    ip = request.META.get("REMOTE_ADDR")
    chip = ["Intel", "AMD"]
    video_chip = ["Intel", "AMD", "Nvidia"]
    ssd = ["Samsung", "WD"]
    return render(request, "advertisement/contacts.html", {
        "ip_address": ip,
        "chip": chip, "video_chip": video_chip, "ssd": ssd
    })

def regions_us(request):
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



