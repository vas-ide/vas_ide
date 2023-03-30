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



# def advertisement_list(request, *args, **kwargs):
#     return HttpResponse("<ul>"
#                         "<li>Delivery to clinic</li>"
#                         "<li>Опрос и первичный осмотр</li>"
#                         "<li>Диагностика и анализы</li>"
#                         "<li>Вмешательство или процедуры</li>"
#                         "<li>Вторичный анализ </li>"
#                         "<li>Delivery from clinic to home</li>"
#                         "</ul>"
#                         )

# def index_page(request):
#     return render(request, "index.html")



def categories_us(request, *args, **kwargs):
    ip = request.META.get("REMOTE_ADDR")
    categories = ["Delivery to clinic",
                     "Опрос и первичный осмотр",
                     "Диагностика и анализы",
                     "Вмешательство или процедуры",
                     "Вторичный анализ и осмотр",
                     "Delivery from clinic to home"
    ]
    return render(request, "advertisement/advertisement_list.html", {"ip_address": ip, "categories": categories})


def about_us(request, *args, **kwargs):
    ip = request.META.get("REMOTE_ADDR")
    return render(request, "advertisement/advertisement_list.html", {"ip_address": ip})


def contact_us(request, *args, **kwargs):
    ip = request.META.get("REMOTE_ADDR")
    return render(request, "advertisement/advertisement_list.html", {"ip_address": ip})







