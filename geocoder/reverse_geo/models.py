from django.contrib.gis.db import models


class Wards(models.Model):
    gid = models.BigIntegerField()
    county = models.CharField(max_length=40)
    subcounty = models.CharField(max_length=80)
    ward = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.ward

