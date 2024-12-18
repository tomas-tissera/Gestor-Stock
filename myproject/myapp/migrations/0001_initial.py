# Generated by Django 5.1.3 on 2024-11-22 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electrónico')),
                ('rol', models.CharField(choices=[('Empleados', 'Empleados'), ('Encargado', 'Encargado')], default='Empleados', max_length=10, verbose_name='Rol')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
            ],
            options={
                'verbose_name': 'Empleados',
                'verbose_name_plural': 'Empleados',
                'ordering': ['-fecha_creacion'],
            },
        ),
    ]
