# Generated by Django 5.0.2 on 2024-02-14 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_order_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Quantiry',
            new_name='Quantity',
        ),
    ]
