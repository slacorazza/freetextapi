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
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """
        Returns the string representation of the Material instance.
        """
        return self.material_name
    
class Order(models.Model):
    """
    Model representing an order for a material.
    
    Attributes:
        material (Material): The material for the order.
        quantity (int): The quantity of the material in the order.
        order_date (DateTime): The date of the order.
    """
    id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=255)
    material_code = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
    total_price = models.IntegerField()
    order_date = models.DateTimeField()
    employee_id = models.CharField(max_length=10)
    employee_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    is_free_text = models.BooleanField()


    def __str__(self):
        """
        Returns the string representation of the Order instance.
        """
        return f'{self.material} - {self.quantity} - {self.order_date}'

class Inventory(models.Model):
    """
    Model representing the inventory of a material.
    
    Attributes:
        material (Material): The material in the inventory.
        quantity (int): The quantity of the material in the inventory.
    """
    id = models.AutoField(primary_key=True)
    material_code = models.CharField(max_length=255, blank=True, null=True)
    material_name = models.CharField(max_length=255)
    current_stock = models.IntegerField()
    is_free_text = models.BooleanField()
    unit_price = models.IntegerField()

    def __str__(self):
        """
        Returns the string representation of the Inventory instance.
        """
        return f'{self.material_code} - {self.quantity}'