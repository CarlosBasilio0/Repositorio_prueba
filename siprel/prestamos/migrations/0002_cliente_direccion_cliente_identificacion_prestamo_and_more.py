# Generated by Django 5.2.1 on 2025-05-13 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.TextField(default='Sin dirección'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='identificacion',
            field=models.CharField(default='Sin dirección', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interes', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fecha_prestamo', models.DateField(auto_now_add=True)),
                ('fecha_vencimiento', models.DateField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado'), ('mora', 'En mora')], default='pendiente', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestamos', to='prestamos.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField(auto_now_add=True)),
                ('monto_pagado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pagos', to='prestamos.prestamo')),
            ],
        ),
    ]
