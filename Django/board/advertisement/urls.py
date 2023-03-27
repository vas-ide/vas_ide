from django.urls import path
from . import views



urlpatterns = [
    path("", views.advertisement_list, name="advertisement_list"),
    path("skillbox_main.html/", views.skillbox_main, name="skillbox_main"),
    path("python_main.html/", views.python_main, name="python_main")
]