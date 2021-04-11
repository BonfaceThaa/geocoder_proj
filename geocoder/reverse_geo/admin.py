from django.contrib.gis import admin
from .models import Wards

# Register your models here.
admin.site.register(Wards, admin.OSMGeoAdmin)
