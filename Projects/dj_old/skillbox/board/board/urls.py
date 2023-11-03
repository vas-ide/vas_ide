"""board URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. context_generator.py an import:  from my_app import views
    2. context_generator.py a URL to urlpatterns:  path('', views.sessions, name='sessions')
Class-based views
    1. context_generator.py an import:  from other_app.views import Home
    2. context_generator.py a URL to urlpatterns:  path('', Home.as_view(), name='sessions')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. context_generator.py a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from advertisement import views




urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", index_page)
    path("", include("advertisement.urls")),
]
