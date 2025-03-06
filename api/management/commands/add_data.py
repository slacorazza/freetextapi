import csv
from django.core.management.base import BaseCommand
from api.models import Material, Inventory, Order
from django.conf import settings
import os
from datetime import datetime

class Command(BaseCommand):
    """
    Django management command to add data to the database from a CSV file.
    """
    help = 'Add data to the database from CSV file'


    def add_inventory(self):
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

    def add_orders(self):
        # Path to the CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'api', 'data', 'orders.csv')

        # Read the CSV file
        with open(csv_file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                order_id = row['order_id']
                material_code = row['material_code']
                quantity = row['quantity']
                unit_price = row['unit_price']
                total_price = row['total_price']
                order_date = datetime.strptime(row['order_date'], '%m/%d/%Y')   
                employeeid = row['employee_id']
                employeename = row['employee_name']
                status = row['status']
                is_free_text = row['is_free_text'].lower() == 'true'
                print(order_id, material_code, quantity, unit_price, total_price, order_date, employeeid, employeename, status, is_free_text)
                # Create the Order

                Order.objects.create(
                    order_id=order_id,
                    material_code=material_code,
                    quantity=quantity,
                    unit_price=unit_price,
                    total_price=total_price,
                    order_date=order_date,
                    employee_id=employeeid,
                    employee_name=employeename,
                    status=status,
                    is_free_text=is_free_text
                )
                print('Order data added successfully')
        self.stdout.write(self.style.SUCCESS('Order data added successfully'))


    
    def add_materials(self):
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
                try:
                    order = Order.objects.filter(material_code=code).first()
                except Order.DoesNotExist:
                    order = None

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
                    predicciones=pred,
                    order=order,
                    )

        self.stdout.write(self.style.SUCCESS('Materials added successfully'))

    def handle(self, *args, **kwargs):
        self.add_inventory()
        self.add_orders()
        self.add_materials()
        self.stdout.write(self.style.SUCCESS('Data added successfully'))