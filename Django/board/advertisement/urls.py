from django.urls import path
from . import views



urlpatterns = [
    path("", views.Index.as_view()),
    path("advertisement/", views.Advertisement.as_view()),
    path("advertisement/get/", views.Advertisement.as_view()),
    path("advertisement/post/", views.Advertisement.as_view()),
    path("advertisement/about.html/", views.About.as_view()),
    path("advertisement/categories.html/", views.Categories.as_view()),
    path("advertisement/regions.html/", views.Regions.as_view()),
    path("advertisement/skillbox_main.html/", views.skillbox_main, name="skillbox_main"),
    path("advertisement/python_main.html/", views.python_main, name="python_main"),
    path("advertisement/pandas_main.html/", views.pandas_main, name="pandas_main"),
    path("advertisement/django_main.html/", views.django_main, name="django_main"),
    path("advertisement/git_main.html/", views.git_main, name="git_main"),

]