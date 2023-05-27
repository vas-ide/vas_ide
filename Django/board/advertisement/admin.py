from django.contrib import admin

from advertisement.models import AdvertisementStatus, Advertisement, AdvertisementType, Region


admin.site.register(Advertisement)
admin.site.register(AdvertisementStatus)
admin.site.register(AdvertisementType)
admin.site.register(Region)