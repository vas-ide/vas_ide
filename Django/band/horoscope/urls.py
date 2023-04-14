


from django.contrib import admin
from django.urls import path, include
from horoscope.views import leo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/leo', leo),

]
