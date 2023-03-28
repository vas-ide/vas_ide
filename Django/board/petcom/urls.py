from django.urls import path
from . import views

urlpatterns = [
    path("about.html/", views.about_us, name="about"),
    path("categories.html/", views.categories_us, name="categories"),
    path("contacts/", views.contact_us, name="contact"),
]