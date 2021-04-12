from django.contrib.gis import admin

from .models import Wards


class WardAdmin(admin.OSMGeoAdmin):
    map_height = 500
    map_width = 500
    modifiable = False


admin.site.register(Wards, WardAdmin)
