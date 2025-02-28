from django.db import models

class Material(models.Model):
    """
    Model representing a material with various suggestions and scores.
    
    Attributes:
        material_name (str): The name of the material.
        sugerencia_1 (str): The first suggestion for the material.
        puntaje_1 (int): The score for the first suggestion.
        material_code_sugerencia_1 (str): The material code for the first suggestion.
        sugerencia_2 (str): The second suggestion for the material.
        puntaje_2 (int): The score for the second suggestion.
        sugerencia_3 (str): The third suggestion for the material.
        puntaje_3 (int): The score for the third suggestion.
        producto_nuevo (bool): Indicates if the material is new.
        material_code (str): The material code.
        predicciones (str): Predictions related to the material.
    """
    material_name = models.CharField(max_length=255)
    sugerencia_1 = models.CharField(max_length=255, blank=True, null=True)
    puntaje_1 = models.IntegerField(blank=True, null=True)
    material_code_sugerencia_1 = models.CharField(max_length=255)
    sugerencia_2 = models.CharField(max_length=255, blank=True, null=True)
    puntaje_2 = models.IntegerField(blank=True, null=True)
    sugerencia_3 = models.CharField(max_length=255, blank=True, null=True)
    puntaje_3 = models.IntegerField(blank=True, null=True)
    producto_nuevo = models.BooleanField()
    material_code = models.CharField(max_length=255, blank=True, null=True)
    predicciones = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        """
        Returns the string representation of the Material instance.
        """
        return self.material_name