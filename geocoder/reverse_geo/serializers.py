from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Wards


class WardSerializer(GeoFeatureModelSerializer):
    """
    Class to serialize Wards as GeoJSON compatible data
    """

    class Meta:
        model = Wards
        fields = '__all__'
        geo_field = 'geom'
        auto_bbox = True
