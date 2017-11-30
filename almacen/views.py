from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import routers, serializers, viewsets

from almacen.models import Producto, Categoria
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response



class ProductoSerializer(ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

