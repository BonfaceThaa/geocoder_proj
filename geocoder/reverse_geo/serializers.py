from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Wards


class WardSerializer(GeoFeatureModelSerializer):
    '''

    '''

    class Meta:
        model = Wards
        fields = '__all__'
        geo_field = 'geom'
