from django.contrib import admin
from . import views
from .views import index
from django.urls import path



urlpatterns = [
    path('', index),
]
