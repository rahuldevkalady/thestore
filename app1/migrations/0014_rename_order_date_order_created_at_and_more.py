# Generated by Django 4.2.6 on 2023-11-27 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_rename_product_id_id_product_s_product_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='cart_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='order_items_id',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='order_item',
            name='unit_price',
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='app1.order_item', to='app1.product_s'),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.customer'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_item',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_item',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.order'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_item',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.product_s'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order_item',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='cart_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product_s')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='app1.cart_item', to='app1.product_s'),
        ),
    ]
