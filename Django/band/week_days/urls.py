from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('monday/', views.monday),
    path('tuesday/', views.tuesday),
]
