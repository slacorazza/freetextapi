import csv
from django.core.management.base import BaseCommand
from api.models import Inventory
from django.conf import settings
import os

class Command(BaseCommand):
    """
    Django management command to add inventory data to the database from a CSV file.
    """
    help = 'Add inventory data to the database from CSV file'

    def handle(self, *args, **kwargs):
        """
        Handle the command to add inventory data to the database from the CSV file.
        """
        # Path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'api', 'data', 'inventory.csv')

        # Read the CSV file
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                material_code = row['material_code']
                material_name = row['material_name']
                current_stock = row['current_stock']
                is_free_text = row['is_free_text'].lower() == 'true'
                unit_price = row['unit_price']

                # Create the Inventory
                Inventory.objects.create(
                    material_code=material_code,
                    material_name=material_name,
                    current_stock=current_stock,
                    is_free_text=is_free_text,
                    unit_price=unit_price
                )

        self.stdout.write(self.style.SUCCESS('Inventory data added successfully'))