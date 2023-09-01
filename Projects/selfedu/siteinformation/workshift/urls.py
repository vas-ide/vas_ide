


from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_information, name='all-info'),
    path('employee', views.employee_information, name='employee-info'),
]


