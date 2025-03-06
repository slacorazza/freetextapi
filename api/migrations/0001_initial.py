# Generated by Django 5.1.6 on 2025-03-06 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('material_code', models.CharField(blank=True, max_length=255, null=True)),
                ('material_name', models.CharField(max_length=255)),
                ('current_stock', models.IntegerField()),
                ('is_free_text', models.BooleanField()),
                ('unit_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.CharField(max_length=255)),
                ('material_code', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('order_date', models.DateTimeField()),
                ('employee_id', models.CharField(max_length=10)),
                ('employee_name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('is_free_text', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_name', models.CharField(max_length=255)),
                ('sugerencia_1', models.CharField(blank=True, max_length=255, null=True)),
                ('puntaje_1', models.IntegerField(blank=True, null=True)),
                ('material_code_sugerencia_1', models.CharField(max_length=255)),
                ('sugerencia_2', models.CharField(blank=True, max_length=255, null=True)),
                ('puntaje_2', models.IntegerField(blank=True, null=True)),
                ('sugerencia_3', models.CharField(blank=True, max_length=255, null=True)),
                ('puntaje_3', models.IntegerField(blank=True, null=True)),
                ('producto_nuevo', models.BooleanField()),
                ('material_code', models.CharField(blank=True, max_length=255, null=True)),
                ('predicciones', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
    ]
