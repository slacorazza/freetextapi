from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Material, Order, Inventory
from .serializers import MaterialSerializer, OrderSerializer, InventorySerializer
from rest_framework.pagination import PageNumberPagination

# Custom view for listing Material objects with optional filtering and pagination
class MaterialList(APIView):
    """
    View to list Material objects with optional filtering and pagination.

    Methods:
        get(request, format=None): Handles GET requests to retrieve a list of materials.
    """

    def get(self, request, format=None):
        """
        Handles GET requests to retrieve a list of materials.

        Query Parameters:
            name (list of str): List of names to filter materials by the first suggestion.
            new (str): Indicates if the material is new ('true' or 'false').
            code (list of str): List of material codes to filter materials.

        Returns:
            Response: Paginated response with serialized material data.
        """
        names = request.query_params.getlist('name')
        new = request.query_params.get('new', None)
        if new:
            new = new.lower() == 'true'
        codes = request.query_params.getlist('code')

        # Filter materials by name, new status, and code
        materials = Material.objects.all()
        if names:
            materials = materials.filter(sugerencia_1__in=names)
        if new is not None:
            materials = materials.filter(producto_nuevo=new)
        if codes:
            materials = materials.filter(material_code__in=codes)

        paginator = PageNumberPagination()
        paginated_materials = paginator.paginate_queryset(materials, request)
        serializer = MaterialSerializer(paginated_materials, many=True)
        return paginator.get_paginated_response(serializer.data)

class KPIList(APIView):
    """
    View to list Material objects with optional filtering and pagination.

    Methods:
        get(request, format=None): Handles GET requests to retrieve a list of materials.
    """

    def get(self, request, format=None):
        return Response({'Total_OC': 147000, 'Total_OC_Amount': '$20.2K', 'Total_OC_FT': 300000, 'Total_OC_FT_Amount': '$30.2K'})
    
class OrderList(APIView):
    """
    View to list Order objects with optional filtering and pagination.

    Methods:
        get(request, format=None): Handles GET requests to retrieve a list of orders.
    """

    def get(self, request, format=None):
        """
        Handles GET requests to retrieve a list of orders.

        Query Parameters:
            material_code (list of str): List of material codes to filter orders.
            costumer_id (list of str): List of costumer IDs to filter orders.
            status (list of str): List of statuses to filter orders.

        Returns:
            Response: Paginated response with serialized order data.
        """
        material_codes = request.query_params.getlist('material_code')
        costumer_ids = request.query_params.getlist('costumer_id')
        statuses = request.query_params.getlist('status')

        # Filter orders by material code, costumer ID, and status
        orders = Order.objects.all()
        if material_codes:
            orders = orders.filter(material_code__in=material_codes)
        if costumer_ids:
            orders = orders.filter(costumer_id__in=costumer_ids)
        if statuses:
            orders = orders.filter(status__in=statuses)

        paginator = PageNumberPagination()
        paginated_orders = paginator.paginate_queryset(orders, request)
        serializer = OrderSerializer(paginated_orders, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class InventoryList(APIView):
    """
    View to list Inventory objects with optional filtering and pagination.

    Methods:
        get(request, format=None): Handles GET requests to retrieve a list of inventory items.
    """

    def get(self, request, format=None):
        """
        Handles GET requests to retrieve a list of inventory items.

        Query Parameters:
            material_code (list of str): List of material codes to filter inventory items.

        Returns:
            Response: Paginated response with serialized inventory data.
        """
        material_codes = request.query_params.getlist('material_code')

        # Filter inventory items by material code
        inventory = Inventory.objects.all()
        if material_codes:
            inventory = inventory.filter(material_code__in=material_codes)

        paginator = PageNumberPagination()
        paginated_inventory = paginator.paginate_queryset(inventory, request)
        serializer = InventorySerializer(paginated_inventory, many=True)
        return paginator.get_paginated_response(serializer.data)