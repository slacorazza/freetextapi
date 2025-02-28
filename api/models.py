from django.db import models


class Material(models.Model):
    material_name = models.CharField(max_length=255)
    sugerencia_1 = models.CharField(max_length=255, blank=True, null=True)
    puntaje_1 = models.IntegerField( blank=True, null=True)
    material_code_sugerencia_1 = models.CharField(max_length=255)
    sugerencia_2 = models.CharField(max_length=255, blank=True, null=True)
    puntaje_2 = models.IntegerField(blank=True, null=True)
    sugerencia_3 = models.CharField(max_length=255, blank=True, null=True)
    puntaje_3 = models.IntegerField(blank=True, null=True)
    producto_nuevo = models.BooleanField()
    material_code = models.CharField(max_length=255, blank=True, null=True)
    predicciones = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.material_name