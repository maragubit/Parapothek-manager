# Generated by Django 2.0.2 on 2019-01-29 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0009_inventario_media'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventario',
            name='media',
        ),
    ]
