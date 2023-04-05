from django.contrib import admin
from youapp.models import Worker
from youapp.models import SalesOrder


admin.site.register(Worker)
admin.site.register(SalesOrder)