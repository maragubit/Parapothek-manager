# Generated by Django 2.0.2 on 2019-02-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0015_auto_20190202_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='media',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='puntuacion',
            field=models.ManyToManyField(blank=True, to='fichas.Puntuar'),
        ),
    ]
