from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Material
from .serializers import MaterialSerializer
from rest_framework.pagination import PageNumberPagination



# Custom view for listing Activity objects with optional filtering and pagination
class MaterialList(APIView):

    def get(self, request, format=None):

        names = request.query_params.getlist('name')
        new = request.query_params.get('new', None)
        if new:
            new = new.lower() == 'true'
        codes = request.query_params.getlist('code')

        # Filter activities by name
        materials = Material.objects.all()
        if names:
            materials = materials.filter(sugerencia_1__in=names)
        if new is not None:
            materials = materials.filter(producto_nuevo=new)
        if codes:
            materials = materials.filter(material_code__in=codes)

        paginator = PageNumberPagination()
        paginated_activities = paginator.paginate_queryset(materials, request)
        serializer = MaterialSerializer(materials, many=True)
        return paginator.get_paginated_response(serializer.data)
    
