from django.shortcuts import render
from rest_framework import viewsets

from crud.models import Restaurante
from crud.serializers import RestauranteSerializer


class RestauranteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
