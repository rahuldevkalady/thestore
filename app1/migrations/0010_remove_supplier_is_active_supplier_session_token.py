# Generated by Django 4.2.6 on 2023-11-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_rename_product_product_s'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='is_active',
        ),
        migrations.AddField(
            model_name='supplier',
            name='session_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]