from django.contrib import admin
from . import views
from .views import index, hello, done
from django.urls import path



urlpatterns = [
    path('', index),
    path('/done', done),
    # path('hello', hello),
]
