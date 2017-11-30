from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import routers, serializers, viewsets

from almacen.models import Producto, Categoria
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(ModelSerializer):
    categoria = CategoriaSerializer()
    class Meta:
        model = Producto
        fields = '__all__'


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def list(self, request):
        try:
            parent_id = request.query_params['parent']
            queryset = Producto.objects.filter(categoria_id=parent_id)
        except MultiValueDictKeyError:
            queryset = Producto.objects.all()

        serializer = ProductoSerializer(queryset, many=True)
        return Response(serializer.data)