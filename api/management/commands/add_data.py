import csv
from django.core.management.base import BaseCommand
from api.models import Material
from django.conf import settings
import os

class Command(BaseCommand):
    """
    Django management command to add data to the database from a CSV file.
    """
    help = 'Add data to the database from CSV file'


    def handle(self, *args, **kwargs):
        """
        Handle the command to add data to the database from the CSV file.
        """
        # Path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'api', 'data', 'resultadopython.csv')

        # Read the CSV file
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)


            for row in reader:
                name = row['material_name']
                sug_1 = row['sugerencia_1']
                punt_1 = row['puntaje_1']
                code = row['material_code_sugerencia_1']
                sug_2 = row['sugerencia_2']
                punt_2 = row['puntaje_2']
                sug_3 = row['sugerencia_3']
                punt_3 = row['puntaje_3']
                new = row['producto_nuevo']
                mat_code = row['material_code']
                pred = row['predicciones']

                # Create the Material
                Material.objects.create(
                    material_name=name,
                    sugerencia_1=sug_1,
                    puntaje_1=punt_1,
                    material_code_sugerencia_1=code,
                    sugerencia_2=sug_2,
                    puntaje_2=punt_2,
                    sugerencia_3=sug_3,
                    puntaje_3=punt_3,
                    producto_nuevo=new,
                    material_code=mat_code,
                    predicciones=pred
                )

        self.stdout.write(self.style.SUCCESS('Data added successfully'))