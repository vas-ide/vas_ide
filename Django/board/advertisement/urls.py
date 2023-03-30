from django.urls import path
from . import views



urlpatterns = [
    path("", views.advertisement_list, name="advertisement_list"),
    path("skillbox_main.html/", views.skillbox_main, name="skillbox_main"),
    path("python_main.html/", views.python_main, name="python_main"),
    path("pandas_main.html/", views.pandas_main, name="pandas_main"),
    path("django_main.html/", views.django_main, name="django_main"),
    path("git_main.html/", views.git_main, name="git_main"),
    path("about.html/", views.about_us, name="about"),
    path("categories.html/", views.categories_us, name="categories"),
    path("contacts/", views.contact_us, name="contact")
]