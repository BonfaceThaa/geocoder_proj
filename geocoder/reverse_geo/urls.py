from django.urls import path, include
from rest_framework import routers

from .views import WardsViewset

routers = routers.DefaultRouter()
routers.register(r'wards', WardsViewset)

urlpatterns = [
    path('', include(routers.urls)),
    path('api/v1/', include('rest_framework.urls', namespace='rest_framework'))
]