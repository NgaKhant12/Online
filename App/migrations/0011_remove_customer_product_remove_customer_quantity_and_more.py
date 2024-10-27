# Generated by Django 5.1 on 2024-10-25 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_customer_product_customer_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='product',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]