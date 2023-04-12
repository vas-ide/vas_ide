from django.contrib import admin
from django.urls import path

from django.urls import path
from rest_framework.routers import SimpleRouter
from youapp.views import OrderViev
from . import views
from django.urls import path, include



urlpatterns = [
    path("", views.Index.as_view()),
]

