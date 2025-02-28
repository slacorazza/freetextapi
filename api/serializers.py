from rest_framework import serializers
from .models import Material

## Serializer are used to convert complex data types, such as querysets and model instances, to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

class MaterialSerializer(serializers.ModelSerializer):
    """
    Serializer for the Material model.

    Converts Material model instances to native Python datatypes that can be easily rendered into JSON, XML, or other content types.

    Meta:
        model (Material): The model that is being serialized.
        fields (list): The list of fields to be included in the serialized output.
    """
    class Meta:
        model = Material
        fields = ['material_name', 'sugerencia_1', 'puntaje_1', 'material_code_sugerencia_1', 'sugerencia_2', 'puntaje_2', 'sugerencia_3', 'puntaje_3', 'producto_nuevo', 'material_code', 'predicciones']