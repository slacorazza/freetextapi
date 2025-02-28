from rest_framework import serializers
from .models import Material


## Serializer are used to convert complex data types, such as querysets and model instances, to native Python datatypes that can then be easily rendered into JSON, XML or other content types.

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['material_name', 'sugerencia_1', 'puntaje_1', 'material_code_sugerencia_1', 'sugerencia_2', 'puntaje_2', 'sugerencia_3', 'puntaje_3', 'producto_nuevo', 'material_code', 'predicciones']