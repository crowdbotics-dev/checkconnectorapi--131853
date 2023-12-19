from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Alpha123ViewSet

router = DefaultRouter()
router.register("alpha123", Alpha123ViewSet, basename="alpha123")

urlpatterns = [
    path("connectors/", include(router.urls)),
]
