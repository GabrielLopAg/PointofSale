# Generated by Django 3.2 on 2021-06-12 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastos',
            name='fecha_pago',
            field=models.DateField(auto_now=True, verbose_name='Fecha de pago'),
        ),
    ]
