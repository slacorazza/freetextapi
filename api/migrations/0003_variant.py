# Generated by Django 5.1.6 on 2025-02-27 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_activity_case_index_alter_activity_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activities', models.CharField(max_length=2000)),
                ('cases', models.CharField(max_length=200)),
            ],
        ),
    ]
