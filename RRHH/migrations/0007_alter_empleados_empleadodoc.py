# Generated by Django 4.0.1 on 2022-01-16 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0006_alter_empleados_areaid_alter_empleados_subarid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='Empleadodoc',
            field=models.CharField(max_length=50, verbose_name='N°Documento'),
        ),
    ]
