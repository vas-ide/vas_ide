from django.contrib import admin

from advertisement.models import AdvertisementStatus, Advertisement, AdvertisementType


admin.site.register(Advertisement)
# admin.site.register(AdvertisementStatus)
# admin.site.register(AdvertisementType)