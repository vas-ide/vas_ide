from django.contrib import admin
from django.urls import path, include
from week_days import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo_week/monday', views.monday),
    path('todo_week/tuesday', views.tuesday),
]
