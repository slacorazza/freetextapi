from rest_framework import serializers
from .models import Material, Order, Inventory

class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for the Order model.

    Converts Order model instances to native Python datatypes that can be easily rendered into JSON, XML, or other content types.

    Meta:
        model (Order): The model that is being serialized.
        fields (list): The list of fields to be included in the serialized output.
    """
    class Meta:
        model = Order
        fields = ['order_id', 'material_code', 'quantity', 'unit_price', 'total_price', 'order_date', 'employee_id', 'employee_name', 'status', 'is_free_text']

class MaterialSerializer(serializers.ModelSerializer):
    """
    Serializer for the Material model.

    Converts Material model instances to native Python datatypes that can be easily rendered into JSON, XML, or other content types.

    Meta:
        model (Material): The model that is being serialized.
        fields (list): The list of fields to be included in the serialized output.
    """
    order = OrderSerializer()

    class Meta:
        model = Material
        fields = ['material_name', 'sugerencia_1', 'puntaje_1', 'material_code_sugerencia_1', 'sugerencia_2', 'puntaje_2', 'sugerencia_3', 'puntaje_3', 'producto_nuevo', 'material_code', 'predicciones', 'order']

class InventorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Inventory model.

    Converts Inventory model instances to native Python datatypes that can be easily rendered into JSON, XML, or other content types.

    Meta:
        model (Inventory): The model that is being serialized.
        fields (list): The list of fields to be included in the serialized output.
    """
    class Meta:
        model = Inventory
        fields = ['material_code', 'material_name', 'current_stock', 'is_free_text', 'unit_price']