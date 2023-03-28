from django.shortcuts import render



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








