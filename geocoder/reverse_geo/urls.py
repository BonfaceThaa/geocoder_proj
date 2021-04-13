from django.urls import path, include
from rest_framework import routers

from .views import WardsViewset

router = routers.DefaultRouter()
router.register(r'wards', WardsViewset)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
