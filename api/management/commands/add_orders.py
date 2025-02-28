import csv
from django.core.management.base import BaseCommand
from api.models import Order
from django.conf import settings
import os
from datetime import datetime

class Command(BaseCommand):
    """
    Django management command to add order data to the database from a CSV file.
    """
    help = 'Add order data to the database from CSV file'

    def handle(self, *args, **kwargs):
        """
        Handle the command to add order data to the database from the CSV file.
        """
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
                customerid = row['customer_id']
                customername = row['customer_name']
                status = row['status']
                is_free_text = row['is_free_text'].lower() == 'true'
                print(order_id, material_code, quantity, unit_price, total_price, order_date, customerid, customername, status, is_free_text)
                # Create the Order

                Order.objects.create(
                    order_id=order_id,
                    material_code=material_code,
                    quantity=quantity,
                    unit_price=unit_price,
                    total_price=total_price,
                    order_date=order_date,
                    costumer_id=customerid,
                    costumer_name=customername,
                    status=status,
                    is_free_text=is_free_text
                )
                print('Order data added successfully')
        self.stdout.write(self.style.SUCCESS('Order data added successfully'))