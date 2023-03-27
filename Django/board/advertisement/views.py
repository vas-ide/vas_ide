from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, "advertisement/advertisement_list.html", {})

def skillbox_main(request, *args, **kwargs):
    return render(request, "advertisement/skillbox_main.html", {})

def python_main(request, *args, **kwargs):
    return render(request, "advertisement/python_main.html", {})

def pandas_main(request, *args, **kwargs):
    return render(request, "advertisement/pandas_main.html", {})

def django_main(request, *args, **kwargs):
    return render(request, "advertisement/django_main.html", {})

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








