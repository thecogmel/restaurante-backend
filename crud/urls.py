from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from .views import RestauranteViewSet

router = DefaultRouter()

router.register("restaurante", RestauranteViewSet, basename="restaurante")

urlpatterns = [
    path("", include(router.urls)),
]
