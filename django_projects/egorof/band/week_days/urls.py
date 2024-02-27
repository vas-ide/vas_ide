from django.urls import path
from . import views


urlpatterns = [
    path('kianu', views.kianu_reeves),
    path('guinness', views.guinnes_world_records),
    path('<int:day_week>', views.get_info_about_day_by_number),
    path('<str:day_week>', views.get_info_about_day, name="day-name"),
]
