


from . import views
from django.urls import path


urlpatterns = [
    path('', views.all_information, name='all-info'),
    path('employee/<int:employee_id>', views.employee_information, name='employee-info_id'),
    path('employee/<slug:employee_slug>', views.employee_information_slug, name='employee-info_slug'),
    # path('employee', views.employee_information, name='employee-info'),
]


