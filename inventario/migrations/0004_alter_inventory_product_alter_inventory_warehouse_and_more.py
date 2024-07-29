# Generated by Django 5.0.7 on 2024-07-29 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_customuser_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='product',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='inventario.product'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='warehouse',
            field=models.ForeignKey(db_column='warehouse_id', on_delete=django.db.models.deletion.CASCADE, to='inventario.warehouse'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(db_column='product_id', on_delete=django.db.models.deletion.CASCADE, to='inventario.product'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='warehouse',
            field=models.ForeignKey(db_column='warehouse_id', on_delete=django.db.models.deletion.CASCADE, to='inventario.warehouse'),
        ),
        migrations.AlterModelTable(
            name='inventory',
            table='inventario_inventory',
        ),
        migrations.AlterModelTable(
            name='product',
            table='inventario_product',
        ),
        migrations.AlterModelTable(
            name='sale',
            table='inventario_sale',
        ),
        migrations.AlterModelTable(
            name='warehouse',
            table='inventario_warehouse',
        ),
    ]
