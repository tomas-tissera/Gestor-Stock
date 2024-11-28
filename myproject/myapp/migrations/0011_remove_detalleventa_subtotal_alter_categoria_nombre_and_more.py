# Generated by Django 5.1.3 on 2024-11-28 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_venta_productos_alter_venta_total_venta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detalleventa',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='venta',
            name='total_venta',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
