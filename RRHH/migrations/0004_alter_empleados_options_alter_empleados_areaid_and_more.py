# Generated by Django 4.0.1 on 2022-01-16 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RRHH', '0003_alter_areas_options_alter_subar_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleados',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterField(
            model_name='empleados',
            name='Areaid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='RRHH.areas'),
        ),
        migrations.AlterField(
            model_name='empleados',
            name='SubArid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='RRHH.subar'),
        ),
    ]