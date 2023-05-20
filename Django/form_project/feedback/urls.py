from django.contrib import admin
from . import views
from .views import index, hello
from django.urls import path



urlpatterns = [
    path('', index),
    path('hello', hello),
]
