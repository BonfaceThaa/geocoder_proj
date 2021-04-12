from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.gis.geos import Point

from .serializers import WardSerializer
from .models import Wards


class WardsViewset(viewsets.ModelViewSet):
    serializer_class = WardSerializer
    queryset = Wards.objects.all()

    @action(detail=False, methods=['get'])
    def get_admin(self, request):
        lat = request.GET.get('lat', None)
        long = request.GET.get('long', None)
        if lat and long:
            reverse_location = Point(float(long), float(lat))
            reverse_ward = Wards.objects.filter(geom__contains=reverse_location)
            serializer = self.get_serializer_class()
            serialized = serializer(reverse_ward, many=True)

            return Response(serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


