# Generated by Django 5.0.6 on 2024-07-09 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_price_product_unit_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='mambership',
            new_name='membership',
        ),
    ]
