# Generated by Django 5.1 on 2024-08-23 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_promotionproducts_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotionproducts',
            name='active',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]