# Generated by Django 5.1.3 on 2024-11-22 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_empleados_user_alter_empleados_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='rol',
            field=models.CharField(blank=True, default='Empleado', max_length=50, null=True),
        ),
    ]
