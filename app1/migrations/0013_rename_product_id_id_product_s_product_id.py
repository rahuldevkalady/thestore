# Generated by Django 4.2.6 on 2023-11-23 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_rename_product_id_product_s_product_id_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_s',
            old_name='product_id_id',
            new_name='product_id',
        ),
    ]
