

from django.urls import path, re_path, register_converter
from . import views
from . import converters


register_converter(converters.FourDigitYearConverter, 'year4')


urlpatterns = [
    path('', views.all_information, name='all-info'),
    path('employee/<int:employee_id>/', views.employee_information, name='employee-info_id'),
    path('employee/<slug:employee_slug>/', views.employee_information_slug, name='employee-info_slug'),
    # re_path(r'archive/(?P<year>[0-9]{4})/', views.archive_year, name="archive_year"),
    path('archive/<year4:year>/', views.archive_year, name="archive_year"),

]


